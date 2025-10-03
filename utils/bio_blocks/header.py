import json
from utils.bio_blocks.coloured_text import coloured_text


def create_flags(dragon):
    flags = []

    with open("utils/resources/flags.json", mode="r", encoding="utf-8") as file:
        flag_banners = json.load(file)

        for i in range(1,5):
            flag = dragon[f"flag_{i}"]
            if flag:
                image = flag_banners[flag]
                flags.append(f"[img alt='{flag} flag']{image}[/img]".replace(" alternative", ""))

    return "".join(flags)


def create_header(dragon):
    text_colour = coloured_text(dragon)
    flags = create_flags(dragon)

    header = f"""[columns][img alt='transparent placeholder']https://i.postimg.cc/Tw5VhGwy/60x1.png[/img][nextcol][center][color={text_colour}][font=gabriola][size=7][b]{dragon["name"]}[/b][/size]
[size=6]{dragon["subtitle"]}[/size][/font][/color]
[img alt='transparent placeholder']https://i.postimg.cc/W4km1TtJ/472x1.png[/img][/center][nextcol][right]{flags}[br][img alt='transparent placeholder']https://i.postimg.cc/Tw5VhGwy/60x1.png[/img][/right][/columns]"""
    return header
