from collections import Counter
def frequency_sort(items):
    list = []
    for i in items:
        if i not in list:
            for j in items:
                if i==j:
                    list.append(i)
    return sorting(list)

def sorting(line):
    result = [item for items, c in Counter(line).most_common()
        for item in [items] * c]
    return result

if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    p= list(frequency_sort([4,6,2,2,2,6,4,4,4]))
    print(p.sort)
    s= list(frequency_sort([4,6,2,2,2,6,4,4,4]))
    print(sorting(s))
    assert list(frequency_sort([4,6,2,2,2,6,4,4,4])) == [4,4,4,4,2,2,2,6,6]
    print("Coding complete? Click 'Check' to earn cool rewards!")
