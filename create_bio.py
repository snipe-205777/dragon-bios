import pandas as pd
from bio_blocks.credits import credits
from bio_blocks.dividers import dividers
from bio_blocks.header import create_header

dragon_data = pd.read_excel("bio_info.xlsx", sheet_name="dragons", header=0)

dragon_data = dragon_data.fillna(0)

for i in range(dragon_data.shape[0] - 1):
    dragon = dragon_data.loc[i]

    divider = dividers(dragon)
 
    header = create_header(dragon)
    credit = credits(dragon)
