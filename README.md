# Dragon Bios

This repo contains:
- Each dragon's lore and other bio settings
- A script to compile these contents with respect to a template
- The final coded bio created from the script.

## How to run

Use `python create_bio.py` to run the script and create completed bios for all dragons in the spreadsheet.

To only create a bio for a single dragon, add the `-d` or `--dragon` flags to the command, followed by the name of the dragon. The name is case-sensitive. With the flag the command should read `python create_bio.py -d <dragon_name>` or `python create_bio.py --dragon <dragon_name>` (without angle brackets).
