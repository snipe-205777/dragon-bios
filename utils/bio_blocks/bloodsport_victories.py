def bloodsport_victories(dragon):
    if dragon["bloodsport_victories"]:
        multiwinner = True if dragon["bloodsport_victories"] > 1 else False

        if multiwinner:
            multiwin = f"\n[size=2]{int(dragon['bloodsport_victories'])} time winner[/size]"
        else:
            multiwin = ""

        return f"[center][img alt='A bloody crown with the word Victor scrawled on it and Arcane Slack Hunger Games written underneath']http://i.imgur.com/fnF3LPe.png[/img]{multiwin}[/center]"

    return ""
