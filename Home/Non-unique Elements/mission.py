#Your optional code here
#You can import some modules or create additional functions


def checkio(x):
    data=[]
    found=False
    if 0 < len(x) < 1000:
        for i in range (len(x)):

            for j in range (len(x)):
                if (i!=j):
                    if x[i] == x[j]:
                        found=True
            if (found):
                data.append(x[i])
                found=False
##        print(data)








    return data

#Some hints
#You can use list.count(element) method for counting.
#Create new list with non-unique elements
#Loop over original list


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")
