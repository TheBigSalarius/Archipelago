import typing
from Options import TextChoice, Option, Range, Toggle, DeathLink


class Goal(TextChoice):
    """
    What the goal objective for the game will be.
    Defeating the end boss Mordred on floor 25 will award victory.
    Reach floor awards victory upon reaching a designated floor (Floor Goal).
    """
    display_name = "Goal"
    option_mordred = 0
    option_reach_floor = 1


class FloorGoal(Range):
    """Specifies the floor to complete for victory when "reach floor" goal is set."""
    display_name = "Floor Goal"
    range_start = 10
    range_end = 25
    default = 25


class DoubleManaDots(Range):
    """
    Specifies the amount of Double Mana Dots item to be in the item pool (replaces Mana Dots)
    This can be used to make the overall game easier.
    """
    display_name = "Double Mana Dots"
    range_start = 0
    range_end = 75
    default = 0


riftwizard_options: typing.Dict[str, type(Option)] = {
    "goal": Goal,
    "floor_goal": FloorGoal,
    "double_mana_dots": DoubleManaDots,
    "death_link": DeathLink,
}
