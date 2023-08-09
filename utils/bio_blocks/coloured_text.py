from utils.resources.text_colour import text_colour

def coloured_text(dragon):
    if dragon["divider_type"]:
        divider_type = dragon["divider_type"]
    else:
        divider_type = "Swirls"

    return text_colour[divider_type][dragon["flight"]]
