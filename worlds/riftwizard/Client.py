from __future__ import annotations

import atexit
import os
import sys
import asyncio

import ModuleUpdate
ModuleUpdate.update()

import Utils
import json
import logging

if __name__ == "__main__":
    Utils.init_logging("RiftWizardClient", exception_logger="Client")

from NetUtils import ClientStatus
from CommonClient import gui_enabled, logger, get_base_parser, ClientCommandProcessor, \
    CommonContext, server_loop

riftwizard_logger = logging.getLogger("RiftWizard")


class RiftWizardClientCommandProcessor(ClientCommandProcessor):
    def _cmd_resync(self):
        """Manually trigger a resync."""
        self.output(f"Syncing items.")
        self.ctx.syncing = True

    def _cmd_deathlink(self):
        """Toggle deathlink from client. Overrides default setting."""
        if isinstance(self.ctx, RiftWizardContext):
            if os.path.exists(self.ctx.send_deathlink_file):
                os.remove(self.ctx.send_deathlink_file)
            self.ctx.deathlink_enabled = not self.ctx.deathlink_enabled
            Utils.async_start(self.ctx.update_death_link(self.ctx.deathlink_enabled), name="Update Deathlink")

    def _cmd_clearcache(self):
        """Manually purge old seed data. (Must Restart Client)"""
        self.output(f"Clearing old saves.")
        options = Utils.get_settings()
        root_directory = os.path.join(options["riftwizard_options"]["root_directory"])
        self.root_game_communication_path = os.path.join(root_directory, "mods", "ArchipelagoMod", "AP")
        for root, dirs, files in os.walk(self.root_game_communication_path, topdown=False):
            for f in files:
                os.remove(root + "/" + f)
            for d in dirs:
                os.rmdir(root + "/" + d)



class RiftWizardContext(CommonContext):
    command_processor: int = RiftWizardClientCommandProcessor
    game = "Rift Wizard"
    items_handling = 0b111  # full remote

    def __init__(self, server_address, password):
        super(RiftWizardContext, self).__init__(server_address, password)
        self.send_index: int = 0
        self.syncing = False
        self.deathlink_enabled = False
        if "appdata" in os.environ:
            options = Utils.get_settings()
            root_directory = os.path.join(options["riftwizard_options"]["root_directory"])
            mod_riftwizard = os.path.join(root_directory, "mods")
            self.root_game_communication_path = os.path.join(root_directory, "mods", "ArchipelagoMod", "AP")
            self.game_communication_path = ""
            if not os.path.exists(self.root_game_communication_path):
                os.makedirs(self.root_game_communication_path)

            if not os.path.isfile(os.path.join(root_directory, "RiftWizard.exe")):
                print_error_and_close("RiftWizardClient couldn't find RiftWizard.exe. "
                                      "Ensure host.yaml points to the RiftWizard folder and the game is installed")
            if not os.path.isdir(mod_riftwizard):
                print_error_and_close("RiftWizardClient couldn't find /mods folder in RiftWizard Directory. "
                                      "Reinstall RiftWizard to attempt to fix this error")
            if not os.path.isdir(mod_riftwizard + "/ArchipelagoMod"):
                print_error_and_close("RiftWizardClient couldn't find the Archipelago Mod for RiftWizard. "
                                      "Ensure the Archipelago Mod is in the /mods folder of the RiftWizard Directory")
        else:
            print_error_and_close("RiftWizardClient couldn't detect system type. ")

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super(RiftWizardContext, self).server_auth(password_requested)
        await self.get_username()
        await self.send_connect()

    async def connection_closed(self):
        await super(RiftWizardContext, self).connection_closed()
        self.remove_slot_files()
    @property
    def endpoints(self):
        if self.server:
            return [self.server]
        else:
            return []

    async def shutdown(self):
        await super(RiftWizardContext, self).shutdown()
        self.remove_slot_files()

    def remove_slot_files(self):
        os.remove(self.root_game_communication_path + "/" + "AP_settings.json")

    def on_package(self, cmd: str, args: dict):
        if cmd in {"Connected"}:

            options = Utils.get_settings()
            root_directory = os.path.join(options["riftwizard_options"]["root_directory"])

            # Create file for mod containing slot data
            filename = f"AP_settings.json"
            with open(os.path.join(self.root_game_communication_path, filename), 'w') as f:
                json.dump(args["slot_data"], f)
                f.close()

            seed = args["slot_data"]["seed"]
            print(seed)
            self.game_communication_path = os.path.join(root_directory, "mods", "ArchipelagoMod", "AP", seed)
            print(self.game_communication_path)
            self.send_deathlink_file = os.path.join(self.game_communication_path, "deathlinkout")
            if not os.path.exists(self.game_communication_path):
                os.makedirs(self.game_communication_path)

            # Switches on Deathlink and Tag if option is on (refreshes on connect)
            # Doesn't look ideal, better to check how to add tag by default
            if 'death_link' in args['slot_data'] and args['slot_data']['death_link']:
                self.deathlink_enabled = True
                Utils.async_start(self.update_death_link(self.deathlink_enabled), name="Update Deathlink")

            # Create files of previously checked locations
            for ss in self.checked_locations:
                filename = f"send{ss}"
                with open(os.path.join(self.game_communication_path, filename), 'w') as f:
                    f.close()

        if cmd in {"RoomInfo"}:
            self.seed_name = args["seed_name"]

        # Create files of received items
        if cmd in {"ReceivedItems"}:
            received_ids = [item.item for item in self.items_received]
            for network_item in self.items_received:
                filename = f"AP_{str(network_item.item)}.item"
                path = os.path.join(self.game_communication_path, filename)

                # Writes the current item count for received Mana Dots/Double Mana Dots
                with open(path, 'w') as f:
                    item_count = received_ids.count(network_item.item)
                    f.write(f"{item_count}")
                    f.close()

        # Create file of checked location
        if cmd in {"RoomUpdate"}:
            if "checked_locations" in args:
                for ss in self.checked_locations:
                    filename = f"send{ss}"
                    with open(os.path.join(self.game_communication_path, filename), 'w') as f:
                        f.close()

    def run_gui(self):
        from kvui import GameManager

        class RiftWizardManager(GameManager):
            logging_pairs = [
                ("Client", "Archipelago")
            ]
            base_title = "Archipelago Rift Wizard Client"

        self.ui = RiftWizardManager(self)
        self.ui_task = asyncio.create_task(self.ui.async_run(), name="UI")

    def on_deathlink(self, data: dict):
        # Create deathlink file to have mod process local death (consumes deathlink file)
        with open(os.path.join(self.game_communication_path, "deathlink"), 'w') as f:
            f.close()
        super().on_deathlink(data)

    async def send_death(self, death_text: str = ""):
        # Remove deathlink file (to not repeatedly send) and send deathlink
        os.remove(self.send_deathlink_file)
        await super().send_death(death_text)

async def game_watcher(ctx: RiftWizardContext):
    while not ctx.exit_event.is_set():
        if ctx.syncing == True:
            sync_msg = [{'cmd': 'Sync'}]
            if ctx.locations_checked:
                sync_msg.append({"cmd": "LocationChecks", "locations": list(ctx.locations_checked)})
            await ctx.send_msgs(sync_msg)
            ctx.syncing = False
        sending = []
        victory = False
        for root, dirs, files in os.walk(ctx.game_communication_path):
            for file in files:
                if file.find("send") > -1:
                    st = file.split("send", -1)[1]
                    sending = sending+[(int(st))]
                if file.find("victory") > -1:
                    victory = True
        ctx.locations_checked = sending
        message = [{"cmd": 'LocationChecks', "locations": sending}]
        await ctx.send_msgs(message)
        if ctx.deathlink_enabled and os.path.exists(ctx.send_deathlink_file):
            await ctx.send_death(ctx.auth + " has been lost to the Rift ")
        if not ctx.finished_game and victory:
            await ctx.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
            ctx.finished_game = True
        await asyncio.sleep(0.1)


def print_error_and_close(msg):
    logger.error("Error: " + msg)
    Utils.messagebox("Error", msg, error=True)
    sys.exit(1)

def launch():
    async def main(args):
        ctx = RiftWizardContext(args.connect, args.password)
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="server loop")
        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()
        progression_watcher = asyncio.create_task(
            game_watcher(ctx), name="RiftWizardProgressionWatcher")

        await ctx.exit_event.wait()
        ctx.server_address = None

        await progression_watcher

        await ctx.shutdown()

    import colorama

    parser = get_base_parser(description="Rift Wizard Client, for text interfacing.")

    args, rest = parser.parse_known_args()
    colorama.init()
    asyncio.run(main(args))
    colorama.deinit()
