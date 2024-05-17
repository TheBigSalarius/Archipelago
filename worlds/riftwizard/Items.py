import typing

from BaseClasses import Item
from typing import Dict


class ItemData(typing.NamedTuple):
    code: typing.Optional[int]
    progression: bool
    event: bool = False


item_table: Dict[str, ItemData] = {
    'Mana Dot': ItemData(18001, True),
    'Double Mana Dot': ItemData(18002, True),
    'Consumable': ItemData(18003, False),
    'Trap': ItemData(18004, False),
    # Event Items
    'Victory': ItemData(None, True, True)

}

item_pool: Dict[str, int] = {

}

event_item_pairs: Dict[str, str] = {
    "Mordred": "Victory"
}
