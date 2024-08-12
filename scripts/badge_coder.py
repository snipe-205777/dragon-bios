import pandas as pd


def code_badge(badge_name):
    badges = pd.read_csv("scripts/badges.csv", header=0, skipinitialspace=True)
    badges = badges.fillna("")
    badges = badges.set_index("Name")

    badge = badges.loc[badge_name]
    return f'[center][size=1]{badge["Pre-image"]}[url={badge["Link"]}][img alt="{badge["Alt Text"]}"]{badge["Image"]}[/img][/url]\n{badge["Caption"]}'


def compile_badges():
    pass


if __name__ == "__main__":
    compile_badges()
