import json
from os.path import exists


def create_side_icons(dragon):
    icon_type = dragon["icon_type"] if dragon["icon_type"] else "Runes"

    with open("utils/resources/flight_icons.json", mode="r", encoding="utf-8") as file:
        flight_icons = json.load(file)
        icon = flight_icons[icon_type][dragon["flight"]]
        flight_icon = f"[img alt='{dragon['flight']} icon']{icon}[/img]"

    icons = [flight_icon]

    for i in range(1,4):
        item = dragon[f"item_{i}"]
        if ".png" in item or ".jpg" in item or ".jpeg" in item:
            alt_text, img_code = item.split(", ")
            icons.append(f"[img alt='{alt_text}']{img_code}[/img]")
        elif item:
            icons.append(f"[item={item}]")

    return "\n\n".join(icons)


def get_bio_text(dragon):
    filename = f"bio_sections/main_content/{dragon['subgroup']}/{dragon['name'].lower().replace(' ', '_')}.txt"

    if not exists(filename):
        filename = f"bio_sections/main_content/{dragon['name'].lower().replace(' ', '_')}.txt"

    if exists(filename):
        with open(filename, "r", encoding="utf8") as bio_text:
            return bio_text.read()
    return ""


def main_content(dragon):
    side_icons = create_side_icons(dragon)
    bio_text = get_bio_text(dragon)
    return f"""[columns]
{side_icons}
[nextcol]
{bio_text}
[/columns]"""
