def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    answer=[]
    for i in text:
        if i != " ":
            answer.append(i)
        else:
            break
##    answer = str(answer)
    answer = ''.join(answer)
    return answer


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word("a word") == "a"
    assert first_word("hi") == "hi"
    print("Coding complete? Click 'Check' to earn cool rewards!")
