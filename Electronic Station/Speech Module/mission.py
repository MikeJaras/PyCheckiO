FIRST_TEN = [" ","one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = [" ", " ", "twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDREDS = ["null", "one hundred", "two hundred", "three hundred", "four hundred", "five hundred", "six hundred",
            "seven hundred", "eight hundred", "nine hundred"]



def checkio(number):
    part_of_reply_hundreds=""
    part_of_reply_other_tens=""
    part_of_reply_second_ten=""
    part_of_reply_first_ten=""
    part_of_reply_only_zero=""
    # part_of_reply_hundreds="FALSE"
    # part_of_reply_other_tens="FALSE"
    # part_of_reply_second_ten="FALSE"
    # part_of_reply_first_ten="FALSE"
    #
    if number == 0:
        part_of_reply_only_zero="zero"

    if number/100 >= 1:
        x=int(number/100)
        part_of_reply_hundreds=HUNDREDS[x]
        number=number-x*100
    if number > 19:
        x=int(number/10)
        part_of_reply_other_tens=OTHER_TENS[x]
        number=number-x*10
    if number < 10:
        x=int(number)
        part_of_reply_first_ten=FIRST_TEN[x]
        number=number-x
        if number != 0:
            print("error")
    if number > 9 and number < 20:
        x=int(number)-10
        part_of_reply_second_ten=SECOND_TEN[x]
        number=number-x-10
        if number != 0:
            print("error")

    # if part_of_reply_hundreds:
    #     answer=part_of_reply_hundreds
    # if part_of_reply_other_tens:
    #     anwer
    answer=part_of_reply_hundreds + " " + \
           part_of_reply_other_tens + " " + \
           part_of_reply_second_ten + " " + \
           part_of_reply_first_ten + " " + \
           part_of_reply_only_zero
    answer = answer.strip()             # remove leading and trailing space
    answer = " ".join(answer.split())   # remove double space
    #answer=part_of_reply_first_ten
    dummy=""
    return answer

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(999) == 'nine hundred ninety nine', "9th example"
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert checkio(0) == 'zero', "7th example"
    assert checkio(28) == 'twenty eight', "8th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
    print('Done! Go and Check it!')
