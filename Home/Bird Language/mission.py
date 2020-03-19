VOWELS = "aeiouy"


def translate(phrase):
    answer = ""
    i = 0

    while i < len(phrase):
        if phrase[i] != " ":
            consonant = True
            test = phrase[i]
            for j in VOWELS:
                test = phrase[i]
                if phrase[i] == j:
                    consonant = False
                    break

            if consonant:
                answer = answer + phrase[i]
                i = i + 2

            else:
                answer = answer + phrase[i]
                i = i + 3
        else:
            answer = answer + phrase[i]
            i = i + 1

    return answer


if __name__ == '__main__':
    print("Example:")
    print(translate("hieeelalaooo"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
    assert translate("hoooowe yyyooouuu duoooiiine?") == "how you doin?", "Joey?"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
