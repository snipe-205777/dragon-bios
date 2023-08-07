import pandas as pd
from bio_blocks.credits import credits
from bio_blocks.dividers import dividers

dragon_data = pd.read_excel("bio_info.xlsx", sheet_name="dragons", header=0)

dragon_data["divider_type"] = dragon_data["divider_type"].fillna("Swirls")

for i in range(dragon_data.shape[0] - 1):
    dragon = dragon_data.loc[i]

    divider = dividers(dragon)
    credit = credits(dragon)
