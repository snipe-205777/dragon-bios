import pandas as pd
from badge_layout import badge_layout


def code_badge(badge_name):
    badges = pd.read_csv("scripts/badges.csv", header=0, skipinitialspace=True)
    badges = badges.fillna("")
    badges = badges.set_index("Name")

    badge = badges.loc[badge_name]
    image = f'[img alt="{badge["Alt Text"]}"]{badge["Image"]}[/img]' if badge["Image"] else ""
    return f'[center][size=1]{badge["Pre-image"]}[url={badge["Link"]}]{image}[/url]\n{badge["Caption"]}'


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
    all_sections = []

    for section in badge_layout:
        all_sections.append(code_section(section))

    filename = "bio_sections/bonus_section_2/concerto.txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write("\n\n".join(all_sections))


if __name__ == "__main__":
    compile_badges()
