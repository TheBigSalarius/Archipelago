from BaseClasses import MultiWorld
from ..AutoWorld import LogicMixin
from ..generic.Rules import set_rule
from .Options import RiftWizardOptions


class RiftWizardLogic(LogicMixin):
    # Calculates the mana received from Mana Dots and Double Mana dots to match the vanilla amount of mana received
    def _riftwizard_mana(self, player: int, amount: int) -> bool:
        count: int = self.count("Mana Dot", player) + 2*(self.count("Double Mana Dot", player))
        return count >= amount


def set_rules(world: MultiWorld, player: int, options: RiftWizardOptions):

    # Mana is used as progression since the game is very difficult if any lower than the default amount
    set_rule(world.get_location("Level 1 - Mana Dot 1", player), lambda state: True)
    set_rule(world.get_location("Level 1 - Mana Dot 2", player), lambda state: True)
    set_rule(world.get_location("Level 1 - Mana Dot 3", player), lambda state: True)

    if options.end_goal.value == 1 and options.floor_goal.value >= 3 or options.end_goal.value == 0:

        set_rule(world.get_location("Level 2 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 1)))
        set_rule(world.get_location("Level 2 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 1)))
        set_rule(world.get_location("Level 2 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 1)))

    if options.end_goal.value == 1 and options.floor_goal.value >= 4 or options.end_goal.value == 0:

        set_rule(world.get_location("Level 3 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 2)))
        set_rule(world.get_location("Level 3 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 2)))
        set_rule(world.get_location("Level 3 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 2)))

    if options.end_goal.value == 1 and options.floor_goal.value >= 5 or options.end_goal.value == 0:

        set_rule(world.get_location("Level 4 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 3)))
        set_rule(world.get_location("Level 4 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 3)))
        set_rule(world.get_location("Level 4 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 3)))

    if options.end_goal.value == 1 and options.floor_goal.value >= 6 or options.end_goal.value == 0:

        set_rule(world.get_location("Level 5 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 4)))
        set_rule(world.get_location("Level 5 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 4)))
        set_rule(world.get_location("Level 5 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 4)))

    if options.end_goal.value == 1 and options.floor_goal.value >= 7 or options.end_goal.value == 0:

        set_rule(world.get_location("Level 6 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 5)))
        set_rule(world.get_location("Level 6 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 5)))
        set_rule(world.get_location("Level 6 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 5)))

    if options.end_goal.value == 1 and options.floor_goal.value >= 8 or options.end_goal.value == 0:

        set_rule(world.get_location("Level 7 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 6)))
        set_rule(world.get_location("Level 7 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 6)))
        set_rule(world.get_location("Level 7 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 6)))

    if options.end_goal.value == 1 and options.floor_goal.value >= 9 or options.end_goal.value == 0:

        set_rule(world.get_location("Level 8 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 7)))
        set_rule(world.get_location("Level 8 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 7)))
        set_rule(world.get_location("Level 8 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 7)))

    if options.end_goal.value == 1 and options.floor_goal.value >= 10 or options.end_goal.value == 0:

        set_rule(world.get_location("Level 9 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 8)))
        set_rule(world.get_location("Level 9 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 8)))
        set_rule(world.get_location("Level 9 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 8)))

    if options.end_goal.value == 1 and options.floor_goal.value >= 11 or options.end_goal.value == 0:

        set_rule(world.get_location("Level 10 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 9)))
        set_rule(world.get_location("Level 10 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 9)))
        set_rule(world.get_location("Level 10 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 9)))

    if options.end_goal.value == 1 and options.floor_goal.value >= 12 or options.end_goal.value == 0:

        set_rule(world.get_location("Level 11 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 10)))
        set_rule(world.get_location("Level 11 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 10)))
        set_rule(world.get_location("Level 11 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 10)))

    if options.end_goal.value == 1 and options.floor_goal.value >= 13 or options.end_goal.value == 0:

        set_rule(world.get_location("Level 12 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 11)))
        set_rule(world.get_location("Level 12 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 11)))
        set_rule(world.get_location("Level 12 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 11)))

    if options.end_goal.value == 1 and options.floor_goal.value >= 14 or options.end_goal.value == 0:

        set_rule(world.get_location("Level 13 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 12)))
        set_rule(world.get_location("Level 13 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 12)))
        set_rule(world.get_location("Level 13 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 12)))

    if options.end_goal.value == 1 and options.floor_goal.value >= 15 or options.end_goal.value == 0:

        set_rule(world.get_location("Level 14 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 13)))
        set_rule(world.get_location("Level 14 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 13)))
        set_rule(world.get_location("Level 14 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 13)))

    if options.end_goal.value == 1 and options.floor_goal.value >= 16 or options.end_goal.value == 0:

        set_rule(world.get_location("Level 15 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 14)))
        set_rule(world.get_location("Level 15 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 14)))
        set_rule(world.get_location("Level 15 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 14)))

    if options.end_goal.value == 1 and options.floor_goal.value >= 17 or options.end_goal.value == 0:

        set_rule(world.get_location("Level 16 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 15)))
        set_rule(world.get_location("Level 16 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 15)))
        set_rule(world.get_location("Level 16 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 15)))

    if options.end_goal.value == 1 and options.floor_goal.value >= 18 or options.end_goal.value == 0:

        set_rule(world.get_location("Level 17 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 16)))
        set_rule(world.get_location("Level 17 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 16)))
        set_rule(world.get_location("Level 17 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 16)))

    if options.end_goal.value == 1 and options.floor_goal.value >= 19 or options.end_goal.value == 0:

        set_rule(world.get_location("Level 18 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 17)))
        set_rule(world.get_location("Level 18 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 17)))
        set_rule(world.get_location("Level 18 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 17)))

    if options.end_goal.value == 1 and options.floor_goal.value >= 20 or options.end_goal.value == 0:

        set_rule(world.get_location("Level 19 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 18)))
        set_rule(world.get_location("Level 19 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 18)))
        set_rule(world.get_location("Level 19 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 18)))

    if options.end_goal.value == 1 and options.floor_goal.value >= 21 or options.end_goal.value == 0:

        set_rule(world.get_location("Level 20 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 19)))
        set_rule(world.get_location("Level 20 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 19)))
        set_rule(world.get_location("Level 20 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 19)))

    if options.end_goal.value == 1 and options.floor_goal.value >= 22 or options.end_goal.value == 0:

        set_rule(world.get_location("Level 21 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 20)))
        set_rule(world.get_location("Level 21 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 20)))
        set_rule(world.get_location("Level 21 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 20)))

    if options.end_goal.value == 1 and options.floor_goal.value >= 23 or options.end_goal.value == 0:

        set_rule(world.get_location("Level 22 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 21)))
        set_rule(world.get_location("Level 22 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 21)))
        set_rule(world.get_location("Level 22 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 21)))

    if options.end_goal.value == 1 and options.floor_goal.value >= 24 or options.end_goal.value == 0:

        set_rule(world.get_location("Level 23 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 22)))
        set_rule(world.get_location("Level 23 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 22)))
        set_rule(world.get_location("Level 23 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 22)))

    if options.end_goal.value == 1 and options.floor_goal.value >= 25 or options.end_goal.value == 0:

        set_rule(world.get_location("Level 24 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 23)))
        set_rule(world.get_location("Level 24 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 23)))
        set_rule(world.get_location("Level 24 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 23)))

    if options.end_goal.value == 1 and options.floor_goal.value >= 26 or options.end_goal.value == 0:

        set_rule(world.get_location("Level 25 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 24)))
        set_rule(world.get_location("Level 25 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 24)))
        set_rule(world.get_location("Level 25 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 24)))


    # Consumable Locations
    if options.end_goal.value == 0:
        floors = 25
    else:
        floors = options.floor_goal.value - 1

    if options.consumable_count.value >= 1:
        set_rule(world.get_location("Consumable Check 1", player), lambda state: state._riftwizard_mana(player, int(1 * floors / options.consumable_count.value * options.difficulty.value - 3)))

    if options.consumable_count.value >= 2:
        set_rule(world.get_location("Consumable Check 2", player), lambda state: state._riftwizard_mana(player, int(2 * floors / options.consumable_count.value * options.difficulty.value - 3)))

    if options.consumable_count.value >= 3:
        set_rule(world.get_location("Consumable Check 3", player), lambda state: state._riftwizard_mana(player, int(3 * floors / options.consumable_count.value * options.difficulty.value - 3)))

    if options.consumable_count.value >= 4:
        set_rule(world.get_location("Consumable Check 4", player), lambda state: state._riftwizard_mana(player, int(4 * floors / options.consumable_count.value * options.difficulty.value - 3)))

    if options.consumable_count.value >= 5:
        set_rule(world.get_location("Consumable Check 5", player), lambda state: state._riftwizard_mana(player, int(5 * floors / options.consumable_count.value * options.difficulty.value - 3)))

    if options.consumable_count.value >= 6:
        set_rule(world.get_location("Consumable Check 6", player), lambda state: state._riftwizard_mana(player, int(6 * floors / options.consumable_count.value * options.difficulty.value - 3)))

    if options.consumable_count.value >= 7:
        set_rule(world.get_location("Consumable Check 7", player), lambda state: state._riftwizard_mana(player, int(7 * floors / options.consumable_count.value * options.difficulty.value - 3)))

    if options.consumable_count.value >= 8:
        set_rule(world.get_location("Consumable Check 8", player), lambda state: state._riftwizard_mana(player, int(8 * floors / options.consumable_count.value * options.difficulty.value - 3)))

    if options.consumable_count.value >= 9:
        set_rule(world.get_location("Consumable Check 9", player), lambda state: state._riftwizard_mana(player, int(9 * floors / options.consumable_count.value * options.difficulty.value - 3)))

    if options.consumable_count.value >= 10:
        set_rule(world.get_location("Consumable Check 10", player), lambda state: state._riftwizard_mana(player, int(10 * floors / options.consumable_count.value * options.difficulty.value - 3)))

    if options.consumable_count.value >= 11:
        set_rule(world.get_location("Consumable Check 11", player), lambda state: state._riftwizard_mana(player, int(11 * floors / options.consumable_count.value * options.difficulty.value - 3)))

    if options.consumable_count.value >= 12:
        set_rule(world.get_location("Consumable Check 12", player), lambda state: state._riftwizard_mana(player, int(12 * floors / options.consumable_count.value * options.difficulty.value - 3)))

    if options.consumable_count.value >= 13:
        set_rule(world.get_location("Consumable Check 13", player), lambda state: state._riftwizard_mana(player, int(13 * floors / options.consumable_count.value * options.difficulty.value - 3)))

    if options.consumable_count.value >= 14:
        set_rule(world.get_location("Consumable Check 14", player), lambda state: state._riftwizard_mana(player, int(14 * floors / options.consumable_count.value * options.difficulty.value - 3)))

    if options.consumable_count.value >= 15:
        set_rule(world.get_location("Consumable Check 15", player), lambda state: state._riftwizard_mana(player, int(15 * floors / options.consumable_count.value * options.difficulty.value - 3)))

    if options.consumable_count.value >= 16:
        set_rule(world.get_location("Consumable Check 16", player), lambda state: state._riftwizard_mana(player, int(16 * floors / options.consumable_count.value * options.difficulty.value - 3)))

    if options.consumable_count.value >= 17:
        set_rule(world.get_location("Consumable Check 17", player), lambda state: state._riftwizard_mana(player, int(17 * floors / options.consumable_count.value * options.difficulty.value - 3)))

    if options.consumable_count.value >= 18:
        set_rule(world.get_location("Consumable Check 18", player), lambda state: state._riftwizard_mana(player, int(18 * floors / options.consumable_count.value * options.difficulty.value - 3)))

    if options.consumable_count.value >= 19:
        set_rule(world.get_location("Consumable Check 19", player), lambda state: state._riftwizard_mana(player, int(19 * floors / options.consumable_count.value * options.difficulty.value - 3)))

    if options.consumable_count.value >= 20:
        set_rule(world.get_location("Consumable Check 20", player), lambda state: state._riftwizard_mana(player, int(20 * floors / options.consumable_count.value * options.difficulty.value - 3)))

    # Boss Event

    if options.end_goal.value == 1:
        set_rule(world.get_location("Mordred", player),
                 lambda state: state._riftwizard_mana(player, options.floor_goal.value*options.difficulty.value)-3)
    if options.end_goal.value == 0:
        set_rule(world.get_location("Mordred", player), lambda state: state._riftwizard_mana(player, int((options.difficulty.value) * 25)))
