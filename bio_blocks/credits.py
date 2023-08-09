from bio_blocks.art import art_block
from bio_blocks.header import create_flags
from resources.dividers import section_dividers
from resources.flight_icons import flight_icons

def credits(dragon):
    lore = f"\nLore: {dragon['bio_credit']}" if dragon["bio_credit"] else ""
    art = "\nArt: Pieces link to artist" if art_block(dragon) else ""
    icon_type = dragon["icon_type"] if dragon["icon_type"] else "Runes"
    divider_type = dragon["divider_type"] if dragon["divider_type"] else "Swirls"
    pride_icons = "\nPride icons: Snipe 205777" if create_flags(dragon) else ""
    bloodsport_crown = "\nHunger Games crown: Aevios 191020" if dragon["bloodsport_victories"] else ""

    return f"""[right][size=1]Credits:
Bio template: Snipe 205777{lore}{art}
Flight icon: {flight_icons[icon_type]["Credit"]}
Flight dividers: {section_dividers[divider_type]["Credit"]}{pride_icons}{bloodsport_crown}[/size][/right]"""
