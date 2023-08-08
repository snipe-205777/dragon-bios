from resources.dividers import section_dividers

def credits(dragon):
    if dragon["divider_type"]:
        divider_type = dragon["divider_type"]
    else:
        divider_type = "Swirls"

    return f"""[right][size=1]Credits:
Flight dividers: {section_dividers[divider_type]["Credit"]}[/size][/right]"""
