

ml_words = {
    0: "പൂജ്യം",
    1: "ഒന്ന്",
    2: "രണ്ട്",
    3: "മൂന്ന്",
    4: "നാല്",
    5: "അഞ്ച്",
    6: "ആറ്",
    7: "ഏഴ്",
    8: "എട്ട്",
    9: "ഒമ്പത്",
    10: "പത്ത്",
    20: "ഇരുപത്",
    21: "ഇരുപത്തി",
}

ml_words_suffix = {
    1:"യൊന്ന്",
    2: " രണ്ട്",
    3: " മൂന്ന്",
    4: " നാല്",
    5: "യഞ്ച്",
    6: "യാറ്",
    7: "യേഴ്",
    8: "യെട്ട്",
    9: " ഒമ്പത്",
}

def ordinal(num):
    if (num < 0):
        return Exception("Unsupported number")
    elif (num < 21):
        return ml_words[num]
    elif (num < 100):
        tens = (num-(num % 10))+1
        ones = num % 10
        print(tens)
        return ml_words[tens] + ml_words_suffix[ones]


print(ordinal(27))
