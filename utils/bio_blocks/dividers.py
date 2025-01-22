import json


def dividers(dragon):
    if dragon["divider_type"]:
        divider_type = dragon["divider_type"]
    else:
        divider_type = "Swirls"

    with open("utils/resources/dividers.json", mode="r", encoding="utf-8") as file:
        section_dividers = json.load(file)

        divider = section_dividers[divider_type][dragon["flight"]]
        return f"[center][img alt='divider']{divider}[/img][/center]"
