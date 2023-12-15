# Rift Wizard Setup Guide

## Required Software

- [The most recent Archipelago release](https://github.com/ArchipelagoMW/Archipelago/releases)
- A legal copy of [Rift Wizard](https://store.steampowered.com/app/1271280/Rift_Wizard),
installed through Steam on Windows.
- Archipelago Mod from
  the [Rift Wizard Archipelago Releases Page](https://github.com/********************)

## Configuring your YAML file

### What is a YAML file and why do I need one?

Your YAML file contains a set of configuration options which provide the generator with information about how it should
generate your game. Each player of a multiworld will provide their own YAML file. This setup allows each player to enjoy
an experience customized for their taste, and different players in the same multiworld can all have different options.

### Where do I get a YAML file?

You can customize your settings by visiting the [Rift Wizard Settings Page](/games/Rift%20Wizard/player-settings).

##Initial Setup
### Update host.yaml to include the Rift Wizard root directory

1. Look for your Archipelago install files. By default, the installer puts them in `C:\ProgramData\Archipelago`.
2. Open the `host.yaml` file in your favorite text editor (Notepad will work).
3. Put your Rift Wizard root directory in the `root_directory:` under the `riftwizard_options:` section.
   - The Rift Wizard root directory can be found by going to 
   `Steam->Right Click Rift Wizard->Properties->Local Files->Browse Local Files` and copying the path in the address bar.
   - Paste the path in between the quotes next to `root_directory:` in the `host.yaml`.
   - You may have to replace all \\ with \\\\. ********Verify this!**************

###Add Archipelago Mod

1. In the Rift Wizard root directory (See step 3 above) open the **mods** folder.
2. Place the **ArchipelagoMod** folder from the Rift Wizard Archipelago Mod into the mods folder 
   * _Note: To disable the mod the ArchipelagoMod folder can be removed or renamed to anything else._
   * _The Archipelago mod appears to be compatible with all other well known Rift Wizard mods, 
many of which add balancing and improve the game experience._

## Connecting to a Multiworld game

1. Navigate to your Archipelago install folder and run `ArchipelagoRiftWizardClient.exe`
2. Notice the `/connect command` on the server hosting page (It should look like `/connect archipelago.gg:*****`
   where ***** are numbers)
3. Type the connect command into the client OR add the port to the pre-populated address on the top bar (it should
   already say `archipelago.gg`) and click `connect`
4. When prompted to `Enter a slot name:`, enter the name specified in the settings file (.yaml).
   * _It should also display this name on the server hosting page._
