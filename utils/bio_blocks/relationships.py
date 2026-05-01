from math import ceil
import pandas as pd
from utils.bio_blocks.coloured_text import coloured_text


def relationships_block(dragon):
    relations = pd.read_csv("relationships.csv", header=0, skipinitialspace=True)
    relations = relations.fillna("")
    relations = relations[relations["dragon"] == dragon["name"]]

    if relations.empty:
        return ""

    relations["url"] = relations.apply(lambda row: f"[url=/dragon/{row.relation_id}]", axis=1)
    relations["portrait_url"] = relations.apply(lambda row: f"/rendern/portraits/{ceil((row.relation_id+1)/100)}/{row.relation_id}p.png", axis=1)
    relations["image"] = relations.apply(lambda row: f"[item={row.familiar_type}]" if row.familiar_type else f'{row.url}[img alt="{row.relation_name} avatar"]{row.portrait_url}[/img][/url]', axis=1)
    relations["code"] = relations.apply(lambda row: f"[columns]{row.image}[nextcol]\n\n{row.relation_name}\n[i]{row.relationship}[/i]\n{row.description}[/columns]", axis=1)

    text_colour = coloured_text(dragon)
    
    block = f"""[center][color={text_colour}][size=4]Relationships[/size][/color][/center]

{"\n".join(relations["code"])}"""

    return block
