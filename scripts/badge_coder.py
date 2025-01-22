import json
import pandas as pd


def code_badge(badge_name):
    badges = pd.read_csv("scripts/badges.csv", header=0, skipinitialspace=True)
    badges = badges.fillna("")
    badges = badges.set_index("Name")

    badge = badges.loc[badge_name]

    text_format = "[center][size=1]" if badge["Caption"] else ""
    alt_text = f' alt="{badge["Alt Text"]}"' if badge["Alt Text"] else ""
    image = f'[img{alt_text}]{badge["Image"]}[/img]' if badge["Image"] else ""
    url_open = f'[url={badge["Link"]}]' if badge["Link"] else ""
    url_close = "[/url]" if badge["Link"] else ""
    brk = "\n" if badge["Image"] else ""
    
    return f'{text_format}{badge["Pre-image"]}{url_open}{image}{url_close}{brk}{badge["Caption"]}'


def code_section(section):
    section_header = f'[size=2][u]{section["header"]}[/u][/size]'
    section_badges = []

    for row in section["badges"]:
        row_badges = []

        for badge in row:
            row_badges.append(code_badge(badge))

        coded_row = "[nextcol]".join(row_badges)
        section_badges.append(coded_row)

    joint_badges = "[/columns][br][br][columns]".join(section_badges)
    section = f"{section_header}\n\n[columns]{joint_badges}[/columns]"
    return section.replace("[br]", "\n")


def compile_badges():
    concerto = {
        "filename": "bio_sections/bonus_section_2/concerto.txt",
        "sections": []
    }

    lsoko = {
        "filename": "bio_sections/bonus_section_2/lsoko.txt",
        "sections": []
    }

    with open("scripts/badge_layout.json", mode="r", encoding="utf-8") as file:
        badge_layout = json.load(file)

        for section in badge_layout:
            if section["host"] == "Concerto":
                concerto["sections"].append(code_section(section))
            elif section ["host"] == "Lsoko":
                lsoko["sections"].append(code_section(section))

    for host in concerto, lsoko:
        with open(host["filename"], "w", encoding="utf-8") as file:
            file.write("\n\n".join(host["sections"]))


if __name__ == "__main__":
    compile_badges()
