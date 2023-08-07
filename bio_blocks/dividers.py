from data import section_dividers

def dividers(dragon):
    divider_type = dragon["divider_type"]
    divider = section_dividers[divider_type][dragon["flight"]]
    return f"[img alt='divider']{divider}[/img]"
