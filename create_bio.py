import argparse
import pandas as pd
from bio_blocks.credits import credits
from bio_blocks.dividers import dividers
from bio_blocks.header import create_header
from bio_blocks.main_content import main_content
from bio_blocks.relationships import relationships_block

dragon_data = pd.read_excel("bio_info.xlsx", sheet_name="dragons", header=0)

dragon_data = dragon_data.fillna(0)

def create_bio(dragon):
    divider = dividers(dragon)
 
    header = create_header(dragon)
    main = main_content(dragon)
    relationships = relationships_block(dragon)
    credit = credits(dragon)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dragon", help="the dragon to create a bio for")
    args = parser.parse_args()

    if args.dragon:
        match_name = dragon_data[dragon_data["name"] == args.dragon]
        if match_name.empty:
            raise ValueError("No dragon found with this name. This argument are case-sensitive")
        else:
            row = match_name.index[0]
            dragon = dragon_data.loc[row]
            create_bio(dragon)
    else:
        for i in range(dragon_data.shape[0] - 1):
            dragon = dragon_data.loc[i]
            create_bio(dragon)
