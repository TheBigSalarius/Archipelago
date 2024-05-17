import string


from BaseClasses import Entrance, Item, ItemClassification, Location, MultiWorld, Region, Tutorial
from .Items import event_item_pairs, item_pool, item_table
from .Locations import location_table
from .Regions import create_regions
from .Rules import set_rules
from ..AutoWorld import WebWorld, World
from .Options import riftwizard_options
from worlds.LauncherComponents import Component, components, Type, launch_subprocess
import worlds.LauncherComponents as LauncherComponents
def launch_client():
    from .Client import launch
    launch_subprocess(launch, name="RiftWizard Client")

LauncherComponents.components.append(
    LauncherComponents.Component(
        "Riftwizard Client",
        func=launch_client,
        component_type=LauncherComponents.Type.CLIENT
    )
)
class RiftWizardWeb(WebWorld):
    theme = 'stone'
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Rift Wizard for Archipelago. "
        "This guide covers single-player, multiworld, and related software.",
        "English",
        "rift-wizard_en.md",
        "rift-wizard/en",
        ["Salarius"]
    )]


class RiftWizardWorld(World):
    """
    Rift Wizard is a tough as nails fantasy roguelike featuring challenging turn based combat and deep open ended
    character building. Craft your spellbook from over 100 unique spells and abilities and fight your way through
    a series of procedurally generated challenges to defeat your nemesis.
    """

    option_definitions = riftwizard_options
    game = "Rift Wizard"
    topology_present = False
    data_version = 0
    web = RiftWizardWeb()

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = location_table

    def create_items(self):

        #Progression requirements for Mordred and Procedural goals
        if self.multiworld.goal[self.player] == 1:
            progreq = self.multiworld.difficulty[self.player] * (self.multiworld.floor_goal[self.player]-1)

        if self.multiworld.goal[self.player] == 0:
            progreq = self.multiworld.difficulty[self.player] * 25


        progcheck = 0
        ddcheck = self.multiworld.double_mana_dots[self.player]

        # Create item pool
        pool = []

        # Add any traps first (based on options)
        for i in range(self.multiworld.traps[self.player]):
            item = RiftWizardItem('Trap', self.player)
        #    item2 = RiftWizardItem('Double Mana Dot', self.player)
        #    if self.multiworld.traps[self.player]
        #        pool.append(item2)
            pool.append(item)

        # Add any double dots first (based on options)
        for i in range(self.multiworld.double_mana_dots[self.player]):
            item = RiftWizardItem('Double Mana Dot', self.player)
            pool.append(item)
        #                for amount in range(item_pool.get(name, 0)):
        #                    item = RiftWizardItem(name, self.player)
        #                    pool.append(item)

        # Removes Double Dots/Traps if too many are randomly chosen when floor goal limits the pool
        if self.multiworld.goal[self.player] == 1:
            while len(pool) > (self.multiworld.floor_goal[self.player]-1)*3:
                print(ddcheck *2)
                print(len(pool))
                if (ddcheck *2) > progreq + 1 :
                    item = RiftWizardItem('Double Mana Dot', self.player)
                    ddcheck -= 1
                    pool.remove(item)
                else:
                    item = RiftWizardItem('Trap', self.player)
                    pool.remove(item)

        # Removes Double Dots/Traps if too many are chosen for Mordred goal
        if self.multiworld.goal[self.player] == 0:
            while len(pool) > 75:
                if (ddcheck *2) > progreq + 1 :
                    item = RiftWizardItem('Double Mana Dot', self.player)
                    ddcheck -= 1
                    pool.remove(item)
                else:
                    item = RiftWizardItem('Trap', self.player)
                    pool.remove(item)

        # Always 75 items on Mordred goal so this fills the diff between number of double dots and rest of the locations
        if self.multiworld.goal[self.player] == 0:
            progcheck = (ddcheck *2)
            while progcheck < progreq:
                if len(pool) == 75:
                    item = RiftWizardItem("Trap", self.player)
                    pool.remove(item)
                if len(pool) < 75:
                    item = RiftWizardItem("Mana Dot", self.player)
                    pool.append(item)
                    progcheck += 1
            while len(pool) < 75:
                item = RiftWizardItem("Mana Dot", self.player)
                pool.append(item)

        # Always 75 items on Mordred goal so this fills the diff between number of double dots and rest of the locations
        if self.multiworld.goal[self.player] == 1:
            progcheck = (ddcheck *2)
            while progcheck < progreq:
                if len(pool) == (self.multiworld.floor_goal[self.player]-1)*3:
                    item = RiftWizardItem("Trap", self.player)
                    pool.remove(item)
                if len(pool) < (self.multiworld.floor_goal[self.player]-1)*3:
                    item = RiftWizardItem("Mana Dot", self.player)
                    pool.append(item)
                    progcheck += 1
            while len(pool) < (self.multiworld.floor_goal[self.player]-1)*3:
                item = RiftWizardItem("Mana Dot", self.player)
                pool.append(item)

        # Add the number of consumables equal to the consumable count (number of consumable locations added)
        for i in range(self.multiworld.consumable_count[self.player]):
            item = RiftWizardItem("Consumable", self.player)
            pool.append(item)

        self.multiworld.itempool += pool

        # Pair up our event locations with our event items (Victory in this case)
        for event, item in event_item_pairs.items():
            event_item = RiftWizardItem(item, self.player)
            self.multiworld.get_location(event, self.player).place_locked_item(event_item)

        self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)

    def set_rules(self):
        set_rules(self.multiworld, self.player)

    def create_item(self, name: str) -> Item:
        return RiftWizardItem(name, self.player)

    def create_regions(self):
        create_regions(self.multiworld, self.player)

    def fill_slot_data(self) -> dict:
        # Adds our options to the slot data to be used by the mod
        slot_data = {
            'seed': "".join(self.multiworld.per_slot_randoms
                            [self.player].choice(string.ascii_letters) for i in range(16))
        }
        for option_name in riftwizard_options:
            option = getattr(self.multiworld, option_name)[self.player]
            slot_data[option_name] = option.value
        print(slot_data)
        return slot_data


def create_region(world: MultiWorld, player: int, name: str, locations=None, exits=None):
    ret = Region(name, player, world)
    ret.multiworld = world
    if locations:
        for location in locations:
            loc_id = location_table.get(location, 0)
            location = RiftWizardLocation(player, location, loc_id, ret)
            ret.locations.append(location)
    if exits:
        for exit in exits:
            ret.exits.append(Entrance(player, exit, ret))

    return ret


class RiftWizardLocation(Location):
    game: str = "Rift Wizard"

    def __init__(self, player: int, name: str, address=None, parent=None):
        super(RiftWizardLocation, self).__init__(player, name, address, parent)
        if address is None:
            self.event = True
            self.locked = True


class RiftWizardItem(Item):
    game = "Rift Wizard"

    def __init__(self, name, player: int = None):
        item_data = item_table[name]
        super(RiftWizardItem, self).__init__(
            name,
            ItemClassification.progression if item_data.progression else ItemClassification.filler,
            item_data.code, player
        )
