from math import ceil
import pandas as pd


def get_relations(dragon):
    relations = pd.read_csv("relationships.csv", header=0, skipinitialspace=True)
    relations = relations.fillna("")
    relations = relations[relations["dragon"] == dragon["name"]]

    if relations.empty:
        return []

    relations["url"] = relations.apply(lambda row: f"[url=/dragon/{row.relation_id}]", axis=1)
    relations["portrait_url"] = relations.apply(lambda row: f"/rendern/portraits/{ceil((row.relation_id+1)/100)}/{row.relation_id}p.png", axis=1)
    relations["image"] = relations.apply(lambda row: f"[item={row.familiar_type}]" if row.familiar_type else f"{row.url}[img alt='{row.relation_name} avatar']{row.portrait_url}[/img][/url]", axis=1)
    relations["code"] = relations.apply(lambda row: f"[center]{row.image}\n[size=2]{row.relation_name}\n[i]{row.relationship}[/i][/size]", axis=1)

    return list(relations["code"])


def relationships_block(dragon):
    relations = get_relations(dragon)

    transparent_placeholder = {
        2: "https://i.postimg.cc/66Msz3P9/2-avatars.png",
        3: "https://i.postimg.cc/xj6rgCZj/3-avatars.png",
        4: "https://i.postimg.cc/jqMVv51S/4-avatars.png"
    }

    if len(relations) > 1:
        placeholder = transparent_placeholder[len(relations)]
        return f"[columns][img alt='transparent placeholder']{placeholder}[/img][nextcol]{'[nextcol]'.join(relations)}[/columns]"
    elif len(relations) == 1:
        return f"{relations[0]}[/center]"
    else:
        return ""
