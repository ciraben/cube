import re

pattern = "(.*) //"
card_names = []

with open("failed_uploads.txt", "r") as f:
    for line in f:
        card_names.append(re.match(pattern, line)[1])

with open("corrected_cardnames.txt", "w") as f:
    f.write("\n".join(card_names))
