def checkio(words: str) -> bool:
    counter = 0
    result = False
    data = words.split()
    for temp in data:
        if not temp.isdigit():
            counter=counter+1
            if counter >= 3:
                result=True
        else:
            counter=0
    dummy=""
    return result



#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))
    
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
