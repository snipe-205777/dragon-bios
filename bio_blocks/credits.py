from bio_blocks.header import create_flags
from resources.dividers import section_dividers

def credits(dragon):
    divider_type = dragon["divider_type"] if dragon["divider_type"] else "Swirls"
    pride_icons = "\nPride icons: Snipe 205777" if create_flags(dragon) else ""

    return f"""[right][size=1]Credits:
Flight dividers: {section_dividers[divider_type]["Credit"]}{pride_icons}[/size][/right]"""
