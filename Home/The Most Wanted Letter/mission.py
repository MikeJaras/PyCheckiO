from itertools import groupby
##import sys #sys not allowed on checkio
from statistics import mode, StatisticsError
from collections import Counter

def checkio(texten):

    myList=""
    data=""
    text=texten.lower()
    text=''.join(sorted(text))
    for c in text:
      if 122 >= ord(c) >= 97:
        myList=myList+c


    for x, y in groupby(myList):
       if sum(1 for _ in y) > 1:
##         print(x)
         try:
             data=mode(myList)
         except StatisticsError as e:
##             print("Oops!",sys.exc_info()[0],"occured.")
##             print(e)
             type(myList)
             count = Counter(myList)
##             print(count)
             mostCommonChar=count.most_common()
             mc = str(mostCommonChar[0]).strip('()')
             data=mc[1]
##             data=myList[0]
         break


    if not data :
        try:
            data=myList[0]
        except IndexError:
            data=""
##    print(data)
    return data



if __name__ == '__main__':
    print("Example:")
    print(checkio("HeLlo World!"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    assert checkio("Z") == "z", "Try empty."
    assert checkio("") == "", "Try empty."
    assert checkio("Lorem ipsum dolor sit amet") == "m", "test #1 from checkio"
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
