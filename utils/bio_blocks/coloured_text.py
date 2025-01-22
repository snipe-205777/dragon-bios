import json


def coloured_text(dragon):
    if dragon["divider_type"]:
        divider_type = dragon["divider_type"]
    else:
        divider_type = "Swirls"

    with open("utils/resources/text_colour.json", mode="r", encoding="utf-8") as file:
        text_colour = json.load(file)
        return text_colour[divider_type][dragon["flight"]]
