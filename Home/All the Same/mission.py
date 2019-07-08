from typing import List, Any


#def all_the_same(elements: List[Any]) -> bool:
def all_the_same(elements):
    # your code here
    tmp=len(elements)
    tmp2=type(tmp)

    answer = True
    for i in range(len(elements)):
        x = 0

        while x < len(elements):
            if i == x:
                x = x+1
                if x >= len(elements):
                    break
            p = elements[x]
            r = elements[i]
            if elements[x] != elements[i]:
                answer = False
                break
            x=x+1

    return answer


if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
