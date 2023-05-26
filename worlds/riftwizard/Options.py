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

class ConsumableCount(Range):
    """
    Specifies the amount of Consumable checks to be in the item pool (replaces consumables with AP check based on step)
    """
    display_name = "Consumable Count"
    range_start = 0
    range_end = 20
    default = 0


class ConsumableStep(Range):
    """
    Specifies the amount of normal consumable pickups between consumable checks.
    The step amount counts down for each consumable picked up.
    Upon reaching 0 the next consumable pickup grants a check instead of the collectable item.
    """
    display_name = "Consumable Steps"
    range_start = 5
    range_end = 20
    default = 10


riftwizard_options: typing.Dict[str, type(Option)] = {
    "goal": Goal,
    "floor_goal": FloorGoal,
    "double_mana_dots": DoubleManaDots,
    "consumable_count": ConsumableCount,
    "consumable_steps": ConsumableStep,
    "death_link": DeathLink
}
