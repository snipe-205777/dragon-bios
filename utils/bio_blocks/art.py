import pandas as pd
from utils.bio_blocks.coloured_text import coloured_text

def art_block(dragon):
    art = pd.read_csv("art.csv", header=0)
    art = art.fillna("")

    art = art[art["dragon"] == dragon["name"]]

    art["image_code"] = art.apply(lambda row: f"[img alt='{row.alt_text}']{row.image}[/img]", axis = 1)

    art["art_code"] = art.apply(
        lambda row: f"[url={row['artist_link']}]{row['image_code']}[/url]" if row["artist_link"] else row["image_code"],
        axis=1
    )

    art_pieces = "\n".join(art["art_code"].values.tolist())

    if art_pieces:
        text_colour = coloured_text(dragon)

        return f"""[center][color={text_colour}][size=5]Art[/size][/color]
[size=1]All pieces link to artist[/size]

{art_pieces}[/center]"""
    
    return ""
