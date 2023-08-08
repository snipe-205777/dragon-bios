from math import ceil

def get_relations(dragon):
    relations = []
    for i in range(1,4):
        if dragon[f"relationship_{i}_name"]:
            name = dragon[f'relationship_{i}_name']
            role = dragon[f'relationship_{i}_role']
            id = int(dragon[f'relationship_{i}_id'])

            portrait = f"[url=https://www1.flightrising.com/dragon/{id}][img alt='{name} avatar']https://www1.flightrising.com/rendern/portraits/{ceil((id+1)/100)}/{id}p.png[/img][/url]"

            relationship = f"""[center]{portrait}
[size=2]{name}
[i]{role}[/i][/size]"""

            relations.append(relationship)

    return relations

def get_familiar(dragon):
    if dragon["familiar_type"]:
        familiar = f"[item={dragon['familiar_type']}]"
        if dragon["familiar_name"]:
            familiar = f"[center]{familiar}\n[size=2]{dragon['familiar_name']}[/size]"
        return familiar
    return ""

def relationships_block(dragon):
    relations = get_relations(dragon)
    if get_familiar(dragon):
        relations.append(get_familiar(dragon))

    transparent_placeholder = {
        2: "http://i.imgur.com/Qqo72nd.png",
        3: "http://i.imgur.com/sKFPb4R.png",
        4: "http://i.imgur.com/YFy7J4e.png"
    }

    if len(relations) > 1:
        placeholder = transparent_placeholder[len(relations)]

        return f"[columns][img alt='transparent placeholder']{placeholder}[/img][nextcol]{'[nextcol]'.join(relations)}[/columns]"
    elif len(relations) == 1:
        return f"{relations[0]}[/center]"
    else:
        return ""
