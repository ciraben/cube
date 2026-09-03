import re

# (start or number) + NAME + (end or brackets)
pattern = "(\\d+ )?(?P<card_name>[^\\(\\/]+)($| \\(.+\\)| \\/)"
cardnames = []

# get multiple lines of user input
print("paste arena clipboard export:")
while True:
    if (line := input()) == "":
        break
    cardname = re.match(pattern, line).group("card_name")
    cardnames.append(cardname)

import pyperclip
pyperclip.copy("\n".join(cardnames))
print("\nCard names copied to clipboard.")
