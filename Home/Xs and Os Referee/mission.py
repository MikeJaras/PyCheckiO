def checkio(game_result):
    answer=""
    clean=str(game_result).replace("'","").replace(",","").replace(" ","").replace("[","").replace("]","")

# ------ X ------
    bintal=clean.replace("O","0").replace(".","0").replace("X","1")
    c=int(bintal, base=2)
    if kontroll(c):
        answer="X"

# ------ O ------
    bintal=clean.replace("O","1").replace(".","0").replace("X","0")
    c=int(bintal, base=2)
    if kontroll(c):
        answer="O"

# ------ D ------
    if answer=="":
        answer="D"

    return answer

def kontroll(check_list):
    answer=False
    result=[0b100100100,0b010010010,0b001001001,0b111000000,0b000111000,0b000000111,0b100010001,0b001010100]

    for i in result:
        if check_list & i in result:
            answer=True

    return answer



if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert kontroll(0b100100100) == 1, "binärkoll"

    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
