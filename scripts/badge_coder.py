import pandas as pd


def code_badge(badge_name):
    badges = pd.read_csv("scripts/badges.csv", header=0, skipinitialspace=True)
    badges = badges.fillna("")
    badges = badges.set_index("Name")

    badge = badges.loc[badge_name]
    return f'[center][size=1]{badge["Pre-image"]}[url={badge["Link"]}][img alt="{badge["Alt Text"]}"]{badge["Image"]}[/img][/url]\n{badge["Caption"]}'


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
    section = f"{section_header}[columns]{joint_badges}[/columns]"
    return section.replace("[br]", "\n")


def compile_badges():
    pass


if __name__ == "__main__":
    compile_badges()
