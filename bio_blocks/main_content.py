from os.path import exists
from resources.flight_icons import flight_icons

def create_side_icons(dragon):
    icon_type = dragon["icon_type"] if dragon["icon_type"] else "Runes"
    icon = flight_icons[icon_type][dragon["flight"]]
    flight_icon = f"[img alt='{dragon['flight']} icon']{icon}[/img]"

    icons = [flight_icon]

    for i in range(1,4):
        item = dragon[f"item_{i}"]
        if item:
            icons.append(f"[item={item}]")

    return "\n\n".join(icons)

def get_bio_text(dragon):
    filename = f"main_content/{dragon['name'].lower()}.txt"
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
