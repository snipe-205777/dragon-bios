import json
from utils.bio_blocks.art import art_block
from utils.bio_blocks.header import create_flags


def credits(dragon):
    lore = f"\nLore: {dragon['bio_credit']}" if dragon["bio_credit"] else ""
    art = "\nArt: Pieces link to artist" if art_block(dragon) else ""

    with open("utils/resources/flight_icons.json", mode="r", encoding="utf-8") as file:
        flight_icons = json.load(file)
        icon_type = dragon["icon_type"] if dragon["icon_type"] else "Runes"
        icon = flight_icons[icon_type]["Credit"]
    
    with open("utils/resources/dividers.json", mode="r", encoding="utf-8") as file:
        dividers = json.load(file)
        divider_type = dragon["divider_type"] if dragon["divider_type"] else "Swirls"
        divider = dividers[divider_type]["Credit"]

    pride_icons = "\nPride icons: Snipe 205777" if create_flags(dragon) else ""
    bloodsport_crown = "\nHunger Games crown: Aevios 191020" if dragon["bloodsport_victories"] else ""
    extra_credits = f"\n{dragon['extra_credits']}".replace("[br]", "\n") if dragon["extra_credits"] else ""

    return f"""[right][size=1]Credits:
Bio template: Snipe 205777{lore}{art}
Flight icon: {icon}
Flight dividers: {divider}{pride_icons}{bloodsport_crown}{extra_credits}[/size][/right]"""
