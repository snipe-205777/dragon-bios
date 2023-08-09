from os.path import exists
from utils.bio_blocks.coloured_text import coloured_text

def bonus_sections(dragon):
    bonuses = {1: "", 2: ""}
    text_colour = coloured_text(dragon)

    for i in range(1,3):
        filename = f"bio_sections/bonus_section_{i}/{dragon['name'].lower()}.txt"
    
        if exists(filename):
            with open(filename, "r", encoding="utf8") as section:
                section_body = section.read()
            section_title = dragon[f"section_{i}_title"]

            if section_title:
                section_heading = f"""[center][color={text_colour}][size=4]{section_title}[/size][/color][/center]\n\n"""
            else:
                section_heading = ""

            bonuses[i] = f"{section_heading}{section_body}"

    return bonuses
