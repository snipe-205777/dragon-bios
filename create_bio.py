import argparse
from os import path, mkdir
import warnings
from termcolor import cprint
import pandas as pd
from utils.bio_blocks.art import art_block
from utils.bio_blocks.bloodsport_victories import bloodsport_victories
from utils.bio_blocks.bonus_sections import bonus_sections
from utils.bio_blocks.clan_lore import clan_lore_block
from utils.bio_blocks.credits import credits
from utils.bio_blocks.dividers import dividers
from utils.bio_blocks.header import create_header
from utils.bio_blocks.main_content import main_content
from utils.bio_blocks.relationships import relationships_block
from utils.bio_warnings import bio_warnings

with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=UserWarning)
    dragon_data = pd.read_csv("bio_info.csv", skipinitialspace=True)

dragon_data = dragon_data.fillna("")
dragon_data["subgroup"] = dragon_data.apply(lambda row: row["subgroup"].lower().replace(" ", "_"), axis = 1)

def create_bio(dragon):
    divider = dividers(dragon)
 
    header = create_header(dragon)
    main = main_content(dragon)
    relationships = relationships_block(dragon)
    bonus_section_1, bonus_section_2 = bonus_sections(dragon).values()
    clan_lore = clan_lore_block(dragon)
    art = art_block(dragon)
    bloodsport = bloodsport_victories(dragon)
    credit = credits(dragon)

    bio_blocks = [header, main, relationships, bonus_section_1, clan_lore, bonus_section_2, art, bloodsport, credit]

    bio_blocks = [x for x in bio_blocks if x]

    bio = f"\n{divider}\n".join(bio_blocks)

    if not path.exists(f"complete_bios/{dragon['subgroup']}"):
        mkdir(f"complete_bios/{dragon['subgroup']}")

    bio_file = f"complete_bios/{dragon['subgroup']}/{dragon['name'].lower().replace(' ', '_')}.txt"

    if not path.exists(bio_file):
        with open(bio_file, "x", encoding="utf-8") as file:
            message = "bio created"
            color = "green"
    else:
        with open(bio_file, "r", encoding="utf-8") as file:
            if file.read() == bio:
                message = "no changes"
                color = "light_grey"
            else:
                message = "bio updated"
                color = "yellow"

    with open(bio_file, "w", encoding="utf-8") as file:
        file.write(bio)
        cprint(f"{' ' * (16-len(dragon['name']))}{dragon['name']}: {message}", color)

    bio_warnings(dragon["name"], bio)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dragon", help="the dragon to create a bio for")
    args = parser.parse_args()

    if args.dragon:
        match_name = dragon_data[dragon_data["name"] == args.dragon]
        if match_name.empty:
            raise ValueError("No dragon found with this name. This argument is case-sensitive")
        else:
            row = match_name.index[0]
            dragon = dragon_data.loc[row]
            create_bio(dragon)
    else:
        for i in range(dragon_data.shape[0] - 1):
            dragon = dragon_data.loc[i]
            create_bio(dragon)
