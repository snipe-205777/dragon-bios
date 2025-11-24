import re
from termcolor import cprint


def bio_warnings(name, bio):
    formatted_name = ' ' * (16-len(name)) + name
    warning = []

    missing_alt = "\[img( alt=\"\")?\]"
    matches = re.findall(missing_alt, bio)

    if len(matches) > 0:
        warning.append(f"{formatted_name}: Missing alt text. Count: {len(matches)}")

    if len(bio) > 65535:
        warning.append(f"{formatted_name}: Over character limit. Count: {len(bio)}/65535")
    elif len(bio) > 60000:
        warning.append(f"{formatted_name}: Approaching character limit. Count: {len(bio)}/65535")

    if len(warning) > 0:
        cprint("             WARNING:", "red")
        cprint("\n".join(warning), "red")
