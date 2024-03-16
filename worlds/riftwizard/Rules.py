from BaseClasses import MultiWorld
from ..AutoWorld import LogicMixin
from ..generic.Rules import set_rule
from .Options import riftwizard_options


class RiftWizardLogic(LogicMixin):
    # Calculates the mana received from Mana Dots and Double Mana dots to match the vanilla amount of mana received
    def _riftwizard_mana(self, player: int, amount: int) -> bool:
        count: int = self.count("Mana Dot", player) + 2*(self.count("Double Mana Dot", player))
        return count >= amount


def set_rules(world: MultiWorld, player: int):

    # Mana is used as progression since the game is very difficult if any lower than the default amount
    set_rule(world.get_location("Level 1 - Mana Dot 1", player), lambda state: True)
    set_rule(world.get_location("Level 1 - Mana Dot 2", player), lambda state: True)
    set_rule(world.get_location("Level 1 - Mana Dot 3", player), lambda state: True)

    if world.goal[player] == 1 and world.floor_goal[player].value >= 3 or world.goal[player] == 0:

        set_rule(world.get_location("Level 2 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 1)))
        set_rule(world.get_location("Level 2 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 1)))
        set_rule(world.get_location("Level 2 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 1)))

    if world.goal[player] == 1 and world.floor_goal[player].value >= 4 or world.goal[player] == 0:

        set_rule(world.get_location("Level 3 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 2)))
        set_rule(world.get_location("Level 3 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 2)))
        set_rule(world.get_location("Level 3 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 2)))

    if world.goal[player] == 1 and world.floor_goal[player].value >= 5 or world.goal[player] == 0:

        set_rule(world.get_location("Level 4 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 3)))
        set_rule(world.get_location("Level 4 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 3)))
        set_rule(world.get_location("Level 4 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 3)))

    if world.goal[player] == 1 and world.floor_goal[player].value >= 6 or world.goal[player] == 0:

        set_rule(world.get_location("Level 5 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 4)))
        set_rule(world.get_location("Level 5 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 4)))
        set_rule(world.get_location("Level 5 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 4)))

    if world.goal[player] == 1 and world.floor_goal[player].value >= 7 or world.goal[player] == 0:

        set_rule(world.get_location("Level 6 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 5)))
        set_rule(world.get_location("Level 6 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 5)))
        set_rule(world.get_location("Level 6 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 5)))

    if world.goal[player] == 1 and world.floor_goal[player].value >= 8 or world.goal[player] == 0:

        set_rule(world.get_location("Level 7 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 6)))
        set_rule(world.get_location("Level 7 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 6)))
        set_rule(world.get_location("Level 7 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 6)))

    if world.goal[player] == 1 and world.floor_goal[player].value >= 9 or world.goal[player] == 0:

        set_rule(world.get_location("Level 8 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 7)))
        set_rule(world.get_location("Level 8 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 7)))
        set_rule(world.get_location("Level 8 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 7)))

    if world.goal[player] == 1 and world.floor_goal[player].value >= 10 or world.goal[player] == 0:

        set_rule(world.get_location("Level 9 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 8)))
        set_rule(world.get_location("Level 9 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 8)))
        set_rule(world.get_location("Level 9 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 8)))

    if world.goal[player] == 1 and world.floor_goal[player].value >= 11 or world.goal[player] == 0:

        set_rule(world.get_location("Level 10 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 9)))
        set_rule(world.get_location("Level 10 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 9)))
        set_rule(world.get_location("Level 10 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 9)))

    if world.goal[player] == 1 and world.floor_goal[player].value >= 12 or world.goal[player] == 0:

        set_rule(world.get_location("Level 11 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 10)))
        set_rule(world.get_location("Level 11 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 10)))
        set_rule(world.get_location("Level 11 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 10)))

    if world.goal[player] == 1 and world.floor_goal[player].value >= 13 or world.goal[player] == 0:

        set_rule(world.get_location("Level 12 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 11)))
        set_rule(world.get_location("Level 12 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 11)))
        set_rule(world.get_location("Level 12 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 11)))

    if world.goal[player] == 1 and world.floor_goal[player].value >= 14 or world.goal[player] == 0:

        set_rule(world.get_location("Level 13 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 12)))
        set_rule(world.get_location("Level 13 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 12)))
        set_rule(world.get_location("Level 13 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 12)))

    if world.goal[player] == 1 and world.floor_goal[player].value >= 15 or world.goal[player] == 0:

        set_rule(world.get_location("Level 14 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 13)))
        set_rule(world.get_location("Level 14 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 13)))
        set_rule(world.get_location("Level 14 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 13)))

    if world.goal[player] == 1 and world.floor_goal[player].value >= 16 or world.goal[player] == 0:

        set_rule(world.get_location("Level 15 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 14)))
        set_rule(world.get_location("Level 15 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 14)))
        set_rule(world.get_location("Level 15 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 14)))

    if world.goal[player] == 1 and world.floor_goal[player].value >= 17 or world.goal[player] == 0:

        set_rule(world.get_location("Level 16 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 15)))
        set_rule(world.get_location("Level 16 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 15)))
        set_rule(world.get_location("Level 16 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 15)))

    if world.goal[player] == 1 and world.floor_goal[player].value >= 18 or world.goal[player] == 0:

        set_rule(world.get_location("Level 17 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 16)))
        set_rule(world.get_location("Level 17 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 16)))
        set_rule(world.get_location("Level 17 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 16)))

    if world.goal[player] == 1 and world.floor_goal[player].value >= 19 or world.goal[player] == 0:

        set_rule(world.get_location("Level 18 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 17)))
        set_rule(world.get_location("Level 18 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 17)))
        set_rule(world.get_location("Level 18 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 17)))

    if world.goal[player] == 1 and world.floor_goal[player].value >= 20 or world.goal[player] == 0:

        set_rule(world.get_location("Level 19 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 18)))
        set_rule(world.get_location("Level 19 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 18)))
        set_rule(world.get_location("Level 19 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 18)))

    if world.goal[player] == 1 and world.floor_goal[player].value >= 21 or world.goal[player] == 0:

        set_rule(world.get_location("Level 20 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 19)))
        set_rule(world.get_location("Level 20 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 19)))
        set_rule(world.get_location("Level 20 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 19)))

    if world.goal[player] == 1 and world.floor_goal[player].value >= 22 or world.goal[player] == 0:

        set_rule(world.get_location("Level 21 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 20)))
        set_rule(world.get_location("Level 21 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 20)))
        set_rule(world.get_location("Level 21 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 20)))

    if world.goal[player] == 1 and world.floor_goal[player].value >= 23 or world.goal[player] == 0:

        set_rule(world.get_location("Level 22 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 21)))
        set_rule(world.get_location("Level 22 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 21)))
        set_rule(world.get_location("Level 22 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 21)))

    if world.goal[player] == 1 and world.floor_goal[player].value >= 24 or world.goal[player] == 0:

        set_rule(world.get_location("Level 23 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 22)))
        set_rule(world.get_location("Level 23 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 22)))
        set_rule(world.get_location("Level 23 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 22)))

    if world.goal[player] == 1 and world.floor_goal[player].value >= 25 or world.goal[player] == 0:

        set_rule(world.get_location("Level 24 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 23)))
        set_rule(world.get_location("Level 24 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 23)))
        set_rule(world.get_location("Level 24 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 23)))

    if world.goal[player] == 1 and world.floor_goal[player].value >= 26 or world.goal[player] == 0:

        set_rule(world.get_location("Level 25 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 24)))
        set_rule(world.get_location("Level 25 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 24)))
        set_rule(world.get_location("Level 25 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 24)))


    # Consumable Locations
    if world.goal[player] == 0:
        floors = 25
    else:
        floors = world.floor_goal[player].value - 1

    if world.consumable_count[player].value >= 1:
        set_rule(world.get_location("Consumable Check 1", player), lambda state: state._riftwizard_mana(player, int(1 * floors / world.consumable_count[player].value * world.difficulty[player].value - 3)))

    if world.consumable_count[player].value >= 2:
        set_rule(world.get_location("Consumable Check 2", player), lambda state: state._riftwizard_mana(player, int(2 * floors / world.consumable_count[player].value * world.difficulty[player].value - 3)))

    if world.consumable_count[player].value >= 3:
        set_rule(world.get_location("Consumable Check 3", player), lambda state: state._riftwizard_mana(player, int(3 * floors / world.consumable_count[player].value * world.difficulty[player].value - 3)))

    if world.consumable_count[player].value >= 4:
        set_rule(world.get_location("Consumable Check 4", player), lambda state: state._riftwizard_mana(player, int(4 * floors / world.consumable_count[player].value * world.difficulty[player].value - 3)))

    if world.consumable_count[player].value >= 5:
        set_rule(world.get_location("Consumable Check 5", player), lambda state: state._riftwizard_mana(player, int(5 * floors / world.consumable_count[player].value * world.difficulty[player].value - 3)))

    if world.consumable_count[player].value >= 6:
        set_rule(world.get_location("Consumable Check 6", player), lambda state: state._riftwizard_mana(player, int(6 * floors / world.consumable_count[player].value * world.difficulty[player].value - 3)))

    if world.consumable_count[player].value >= 7:
        set_rule(world.get_location("Consumable Check 7", player), lambda state: state._riftwizard_mana(player, int(7 * floors / world.consumable_count[player].value * world.difficulty[player].value - 3)))

    if world.consumable_count[player].value >= 8:
        set_rule(world.get_location("Consumable Check 8", player), lambda state: state._riftwizard_mana(player, int(8 * floors / world.consumable_count[player].value * world.difficulty[player].value - 3)))

    if world.consumable_count[player].value >= 9:
        set_rule(world.get_location("Consumable Check 9", player), lambda state: state._riftwizard_mana(player, int(9 * floors / world.consumable_count[player].value * world.difficulty[player].value - 3)))

    if world.consumable_count[player].value >= 10:
        set_rule(world.get_location("Consumable Check 10", player), lambda state: state._riftwizard_mana(player, int(10 * floors / world.consumable_count[player].value * world.difficulty[player].value - 3)))

    if world.consumable_count[player].value >= 11:
        set_rule(world.get_location("Consumable Check 11", player), lambda state: state._riftwizard_mana(player, int(11 * floors / world.consumable_count[player].value * world.difficulty[player].value - 3)))

    if world.consumable_count[player].value >= 12:
        set_rule(world.get_location("Consumable Check 12", player), lambda state: state._riftwizard_mana(player, int(12 * floors / world.consumable_count[player].value * world.difficulty[player].value - 3)))

    if world.consumable_count[player].value >= 13:
        set_rule(world.get_location("Consumable Check 13", player), lambda state: state._riftwizard_mana(player, int(13 * floors / world.consumable_count[player].value * world.difficulty[player].value - 3)))

    if world.consumable_count[player].value >= 14:
        set_rule(world.get_location("Consumable Check 14", player), lambda state: state._riftwizard_mana(player, int(14 * floors / world.consumable_count[player].value * world.difficulty[player].value - 3)))

    if world.consumable_count[player].value >= 15:
        set_rule(world.get_location("Consumable Check 15", player), lambda state: state._riftwizard_mana(player, int(15 * floors / world.consumable_count[player].value * world.difficulty[player].value - 3)))

    if world.consumable_count[player].value >= 16:
        set_rule(world.get_location("Consumable Check 16", player), lambda state: state._riftwizard_mana(player, int(16 * floors / world.consumable_count[player].value * world.difficulty[player].value - 3)))

    if world.consumable_count[player].value >= 17:
        set_rule(world.get_location("Consumable Check 17", player), lambda state: state._riftwizard_mana(player, int(17 * floors / world.consumable_count[player].value * world.difficulty[player].value - 3)))

    if world.consumable_count[player].value >= 18:
        set_rule(world.get_location("Consumable Check 18", player), lambda state: state._riftwizard_mana(player, int(18 * floors / world.consumable_count[player].value * world.difficulty[player].value - 3)))

    if world.consumable_count[player].value >= 19:
        set_rule(world.get_location("Consumable Check 19", player), lambda state: state._riftwizard_mana(player, int(19 * floors / world.consumable_count[player].value * world.difficulty[player].value - 3)))

    if world.consumable_count[player].value >= 20:
        set_rule(world.get_location("Consumable Check 20", player), lambda state: state._riftwizard_mana(player, int(20 * floors / world.consumable_count[player].value * world.difficulty[player].value - 3)))

    # Boss Event

    if world.goal[player] == 1:
        set_rule(world.get_location("Mordred", player),
                 lambda state: state._riftwizard_mana(player, world.floor_goal[player].value*(world.difficulty[player].value)-3))
    if world.goal[player] == 0:
        set_rule(world.get_location("Mordred", player), lambda state: state._riftwizard_mana(player, int((world.difficulty[player].value) * 25)))
