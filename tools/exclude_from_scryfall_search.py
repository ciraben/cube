def search_term_for(card):
    # accounts for " // " for split cards
    # and cards containing other cardnames, like "sheoldred's edict"
    # only useful for lists below scryfall's max regex per search
    return f"name:/^{card}[$( \\/)]/"

def search_term_no_regex(card):
    # ! ensures exact cardname only
    return f"\"{card}\""

cardnames = []

# get multiple lines of user input
print("paste a \\n-separated list of cardnames:")
while True:
    if (cardname := input()) == "":
        break
    cardnames.append(cardname)

search_terms = (search_term_no_regex(card) for card in cardnames)
all_cards = " or ".join(search_terms)
exclude_all_cards = f"({all_cards})"
print(exclude_all_cards)
