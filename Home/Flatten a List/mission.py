

def flat_list(array):
    wrklist=[]


    def convert(element):
        for j in element:
            if type(j) == list:
                convert(j)

            else:
                wrklist.append(j)

        return


    for i in array:
        if type(i) == list:
            convert(i)
            # for j in i:
            #     wrklist.append(j)
        else:
            wrklist.append(i)




    return wrklist





if __name__ == '__main__':
    assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
    print('Done! Check it')
