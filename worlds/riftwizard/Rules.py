from BaseClasses import MultiWorld
from ..AutoWorld import LogicMixin
from ..generic.Rules import set_rule


class RiftWizardLogic(LogicMixin):
    # Calculates the mana recieved from Mana Dots and Double Mana dots to match the vanilla amount of mana recieved
    def _riftwizard_mana(self, player: int, amount: int) -> bool:
        count: int = self.item_count("Mana Dot", player) + 2*(self.item_count("Double Mana Dot", player))
        return count >= amount


def set_rules(world: MultiWorld, player: int):

    # Mana is used as progression since the game is very difficult if any lower than the default amount
    set_rule(world.get_location("Level 1 - Mana Dot 1", player), lambda state: True)
    set_rule(world.get_location("Level 1 - Mana Dot 2", player), lambda state: True)
    set_rule(world.get_location("Level 1 - Mana Dot 3", player), lambda state: True)

    if world.goal[player] == 1 and world.floor_goal[player].value >= 3 or world.goal[player] == 0:

        set_rule(world.get_location("Level 2 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, 3))
        set_rule(world.get_location("Level 2 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, 3))
        set_rule(world.get_location("Level 2 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, 3))

    if world.goal[player] == 1 and world.floor_goal[player].value >= 4 or world.goal[player] == 0:

        set_rule(world.get_location("Level 3 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, 6))
        set_rule(world.get_location("Level 3 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, 6))
        set_rule(world.get_location("Level 3 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, 6))

    if world.goal[player] == 1 and world.floor_goal[player].value >= 5 or world.goal[player] == 0:

        set_rule(world.get_location("Level 4 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, 9))
        set_rule(world.get_location("Level 4 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, 9))
        set_rule(world.get_location("Level 4 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, 9))

    if world.goal[player] == 1 and world.floor_goal[player].value >= 6 or world.goal[player] == 0:

        set_rule(world.get_location("Level 5 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, 12))
        set_rule(world.get_location("Level 5 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, 12))
        set_rule(world.get_location("Level 5 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, 12))

    if world.goal[player] == 1 and world.floor_goal[player].value >= 7 or world.goal[player] == 0:

        set_rule(world.get_location("Level 6 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, 15))
        set_rule(world.get_location("Level 6 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, 15))
        set_rule(world.get_location("Level 6 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, 15))

    if world.goal[player] == 1 and world.floor_goal[player].value >= 8 or world.goal[player] == 0:

        set_rule(world.get_location("Level 7 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, 18))
        set_rule(world.get_location("Level 7 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, 18))
        set_rule(world.get_location("Level 7 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, 18))

    if world.goal[player] == 1 and world.floor_goal[player].value >= 9 or world.goal[player] == 0:

        set_rule(world.get_location("Level 8 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, 21))
        set_rule(world.get_location("Level 8 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, 21))
        set_rule(world.get_location("Level 8 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, 21))

    if world.goal[player] == 1 and world.floor_goal[player].value >= 10 or world.goal[player] == 0:

        set_rule(world.get_location("Level 9 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, 24))
        set_rule(world.get_location("Level 9 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, 24))
        set_rule(world.get_location("Level 9 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, 24))

    if world.goal[player] == 1 and world.floor_goal[player].value >= 11 or world.goal[player] == 0:

        set_rule(world.get_location("Level 10 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, 27))
        set_rule(world.get_location("Level 10 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, 27))
        set_rule(world.get_location("Level 10 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, 27))

    if world.goal[player] == 1 and world.floor_goal[player].value >= 12 or world.goal[player] == 0:

        set_rule(world.get_location("Level 11 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, 30))
        set_rule(world.get_location("Level 11 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, 30))
        set_rule(world.get_location("Level 11 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, 30))

    if world.goal[player] == 1 and world.floor_goal[player].value >= 13 or world.goal[player] == 0:

        set_rule(world.get_location("Level 12 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, 33))
        set_rule(world.get_location("Level 12 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, 33))
        set_rule(world.get_location("Level 12 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, 33))

    if world.goal[player] == 1 and world.floor_goal[player].value >= 14 or world.goal[player] == 0:

        set_rule(world.get_location("Level 13 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, 36))
        set_rule(world.get_location("Level 13 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, 36))
        set_rule(world.get_location("Level 13 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, 36))

    if world.goal[player] == 1 and world.floor_goal[player].value >= 15 or world.goal[player] == 0:

        set_rule(world.get_location("Level 14 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, 39))
        set_rule(world.get_location("Level 14 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, 39))
        set_rule(world.get_location("Level 14 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, 39))

    if world.goal[player] == 1 and world.floor_goal[player].value >= 16 or world.goal[player] == 0:

        set_rule(world.get_location("Level 15 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, 42))
        set_rule(world.get_location("Level 15 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, 42))
        set_rule(world.get_location("Level 15 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, 42))

    if world.goal[player] == 1 and world.floor_goal[player].value >= 17 or world.goal[player] == 0:

        set_rule(world.get_location("Level 16 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, 45))
        set_rule(world.get_location("Level 16 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, 45))
        set_rule(world.get_location("Level 16 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, 45))

    if world.goal[player] == 1 and world.floor_goal[player].value >= 18 or world.goal[player] == 0:

        set_rule(world.get_location("Level 17 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, 48))
        set_rule(world.get_location("Level 17 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, 48))
        set_rule(world.get_location("Level 17 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, 48))

    if world.goal[player] == 1 and world.floor_goal[player].value >= 19 or world.goal[player] == 0:

        set_rule(world.get_location("Level 18 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, 51))
        set_rule(world.get_location("Level 18 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, 51))
        set_rule(world.get_location("Level 18 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, 51))

    if world.goal[player] == 1 and world.floor_goal[player].value >= 20 or world.goal[player] == 0:

        set_rule(world.get_location("Level 19 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, 54))
        set_rule(world.get_location("Level 19 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, 54))
        set_rule(world.get_location("Level 19 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, 54))

    if world.goal[player] == 1 and world.floor_goal[player].value >= 21 or world.goal[player] == 0:

        set_rule(world.get_location("Level 20 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, 57))
        set_rule(world.get_location("Level 20 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, 57))
        set_rule(world.get_location("Level 20 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, 57))

    if world.goal[player] == 1 and world.floor_goal[player].value >= 22 or world.goal[player] == 0:

        set_rule(world.get_location("Level 21 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, 60))
        set_rule(world.get_location("Level 21 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, 60))
        set_rule(world.get_location("Level 21 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, 60))

    if world.goal[player] == 1 and world.floor_goal[player].value >= 23 or world.goal[player] == 0:

        set_rule(world.get_location("Level 22 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, 63))
        set_rule(world.get_location("Level 22 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, 63))
        set_rule(world.get_location("Level 22 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, 63))

    if world.goal[player] == 1 and world.floor_goal[player].value >= 24 or world.goal[player] == 0:

        set_rule(world.get_location("Level 23 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, 66))
        set_rule(world.get_location("Level 23 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, 66))
        set_rule(world.get_location("Level 23 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, 66))

    if world.goal[player] == 1 and world.floor_goal[player].value >= 25 or world.goal[player] == 0:

        set_rule(world.get_location("Level 24 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, 69))
        set_rule(world.get_location("Level 24 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, 69))
        set_rule(world.get_location("Level 24 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, 69))

    if world.goal[player] == 1 and world.floor_goal[player].value >= 26 or world.goal[player] == 0:

        set_rule(world.get_location("Level 25 - Mana Dot 1", player), lambda state: state._riftwizard_mana(player, 72))
        set_rule(world.get_location("Level 25 - Mana Dot 2", player), lambda state: state._riftwizard_mana(player, 72))
        set_rule(world.get_location("Level 25 - Mana Dot 3", player), lambda state: state._riftwizard_mana(player, 72))

    # Boss Event

    if world.goal[player] == 1:
        set_rule(world.get_location("Mordred", player), lambda state: state._riftwizard_mana(
            player, world.floor_goal[player].value*3-6))
    if world.goal[player] == 0:
        set_rule(world.get_location("Mordred", player), lambda state: state._riftwizard_mana(player, 75))
