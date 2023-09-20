"""
Contains dataclasses jmenu uses to manage data.
This file can be imported and exposes the following classes:

    * MenuItem
    * Restaurant
    * Marker

The following collections are use-case specific to the University of Oulu:

    * MARKERS
    * RESTAURANTS
    * SKIPPED_ITEMS
"""

from collections import namedtuple


_MenuItem = namedtuple("MenuItem", ["name", "diets"])


class MenuItem(_MenuItem):
    """Dataclass for single menu items and their properties

    Attributes:
        name (str):
            name of the dish
        diets (str):
            list of allergen markers
    """


_Restaurant = namedtuple(
    "Restaurant", ["name", "client_id", "kitchen_id", "menu_type", "relevant_menus"]
)


class Restaurant(_Restaurant):
    """Dataclass for relevant restaurant information

    Attributes:
        name (str):
            name of the restaurant
        client_id (str):
            internal jamix identifier used for restaurant providers
        kitchen_id (str):
            internal jamix identifier used to assign menu content
        menu_type (str):
            internal jamix identifier used to classify menus based on content
        relevant_menus (str):
            menu names used for filtering out desserts etc.
    """


_Marker = namedtuple("Marker", ["letters", "explanation"])


class Marker(_Marker):
    """Dataclass for allergen information markings

    Attributes:
        letters (str):
            allergen markings
        explanation (str):
            extended information about the marker
    """


SKIPPED_ITEMS = [
    "proteiinilisäke",
    "Täysjyväriisi",
    "Lämmin kasvislisäke",
    "Höyryperunat",
    "Tumma pasta",
    "Meillä tehty perunamuusi",
    "Mashed Potatoes",
    "Dark Pasta",
    "Whole Grain Rice",
    "Hot Vegetable  Side",  # note the extra space
]

RESTAURANTS = [
    Restaurant("Foobar", 93077, 49, 84, ["Foobar Salad and soup", "Foobar Rohee"]),
    Restaurant("Foodoo", 93077, 48, 89, ["Foodoo Salad and soup", "Foodoo Reilu"]),
    Restaurant("Kastari", 95663, 5, 2, ["Ruokalista"]),
    Restaurant("Kylymä", 93077, 48, 92, ["Kylymä Rohee"]),
    Restaurant("Mara", 93077, 49, 111, ["Salad and soup", "Ravintola Mara"]),
    Restaurant("Napa", 93077, 48, 79, ["Napa Rohee"]),
]

MARKERS = [
    Marker("G", "Gluteeniton"),
    Marker("M", "Maidoton"),
    Marker("L", "Laktoositon"),
    Marker("SO", "Sisältää soijaa"),
    Marker("SE", "Sisältää selleriä"),
    Marker("MU", "Munaton"),
    Marker("[S], *", "Kelan korkeakouluruokailunsuosituksen mukainen"),
    Marker("SIN", "Sisältää sinappia"),
    Marker("<3", "Sydänmerkki"),
    Marker("VEG", "Vegaani"),
]
