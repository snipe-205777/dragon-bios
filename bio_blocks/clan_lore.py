from os.path import exists
from bio_blocks.coloured_text import coloured_text

def clan_lore_block(dragon):
    text_colour = coloured_text(dragon)
    lore_title = dragon["clan_lore_title"]
    lore_file = f"clan_lore/{lore_title.lower().replace(' ', '_')}.txt"
    see_also = dragon["clan_lore_see_also"] if dragon["clan_lore_see_also"] else ""

    if lore_title and exists(lore_file):
        with open(lore_file, "r", encoding="utf8") as body:
            lore_body = body.read()
        
        if see_also:
            see_also = f"\n\nSee Also: {see_also}"

        return f"""[center][color={text_colour}][size=5]{lore_title}[/size][/color][/center]

{lore_body}{see_also}"""

    return ""




