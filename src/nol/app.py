

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
    11: "പതിനൊന്ന്",
    12: "പന്ത്രണ്ട്",
    13: "പതിമൂന്ന്",
    14: "പതിനാല്",
    15: "പതിനഞ്ച്",
    16: "പതിനാറ്",
    17: "പതിനേഴ്",
    18: "പതിനെട്ട്",
    19: "പത്തൊമ്പത്",
    20: "ഇരുപത്",
    30: "മുപ്പത്",
    40: "നാല്പത്",
    50: "അമ്പത്",
    60: "അറുപത്",
    70: "എഴുപത്",
    80: "എൺപത്",
    90: "തൊണ്ണൂറ്",
    100: "നൂറ്",
    200: "ഇരുന്നൂറ്",
    300: "മുന്നൂറ്",
    400: "നാനൂറ്",
    500: "അഞ്ഞൂറ്",
    600: "അറുനൂറ്",
    700: "എഴുന്നൂറ്",
    800: "എണ്ണൂറ്",
    900: "തൊള്ളായിരം",
    1000: "ആയിരം",
    2000: "രണ്ടായിരം",
    3000: "മൂവായിരം",
    4000: "നാലായിരം",
    5000: "അയ്യായിരം",
    6000: "ആറായിരം",
    7000: "ഏഴായിരം",
    8000: "എണ്ണായിരം",
    9000: "ഒമ്പതിനായിരം",
    10000: "പതിനായിരം",
}

ml_words_prefix = {
    21: "ഇരുപത്തി",
    31: "മുപ്പത്തി",
    41: "നാല്പത്തി",
    51: "അൻപത്തി",
    61: "അറുപത്തി",
    71: "എഴുപത്തി",
    81: "എൺപത്തി",
    91: "തൊണ്ണൂറ്റി",
    101: "ഒരുനൂറ്റി",
    201: "ഇരുനൂറ്റി",
    301: "മുന്നൂറ്റി",
    401: "നാനൂറ്റി",
    501: "അഞ്ഞൂറ്റി",
    601: "അറുനൂറ്റി",
    701: "എഴുനൂറ്റി",
    801: "എണ്ണൂറ്റി",
    901: "തൊള്ളായിരത്തി",
    1001: "ആയിരത്തി",
    2001: "രണ്ടായിരത്തി",
    3001: "മൂവായിരത്തി",
    4001: "നാലായിരത്തി",
    5001: "അയ്യായിരത്തി",
    6001: "ആറായിരത്തി",
    7001: "ഏഴായിരത്തി",
    8001: "എണ്ണായിരത്തി",
    9001: "ഒമ്പതിനായിരത്തി",
    10001: "പതിനായിരത്തി",
}

ml_words_suffix = {
    1: "യൊന്ന്",
    2: " രണ്ട്",
    3: " മൂന്ന്",
    4: " നാല്",
    5: "യഞ്ച്",
    6: "യാറ്",
    7: "യേഴ്",
    8: "യെട്ട്",
    9: " ഒമ്പത്",
    1000: "പതിനൊന്നായിരം"
}


def toWords(origNumber):
    nums = [int(digit) for digit in str(origNumber)[::1]]
    # print(nums)
    multply = len(nums)-1
    idx = 0
    # lastIndex = len(nums)-1
    result = ""
    currNumToProess = origNumber
    while (idx < len(nums)):
        num = nums[idx]
        # if (num > 0):
        if (currNumToProess < 21):
            if (currNumToProess > 9 or currNumToProess == origNumber):
                result = result + " " + ml_words[currNumToProess]
            else:
                result = result + ml_words_suffix[currNumToProess]
            break
        elif (num > 0):
            full = 10**multply
            key = full * nums[idx]
            remNumToProess = currNumToProess - key
            # print(remNumToProess)
            if (remNumToProess > 0):
                result = result + " " + ml_words_prefix[key + 1]
            else:
                result = result + " " + ml_words[currNumToProess]
                break
            currNumToProess = remNumToProess
        multply = multply - 1
        idx += 1
    return result


# Testing
n = 10985
while (n < 11112):
    w = toWords(n)
    print("{} - {}".format(n, w))
    n = n + 1
# print(toWords(0))
# print(toWords(10))
# print(toWords(20))
# print(toWords(30))
# print(toWords(40))
