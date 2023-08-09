from utils.resources.dividers import section_dividers

def dividers(dragon):
    if dragon["divider_type"]:
        divider_type = dragon["divider_type"]
    else:
        divider_type = "Swirls"

    divider = section_dividers[divider_type][dragon["flight"]]
    return f"[img alt='divider']{divider}[/img]"
