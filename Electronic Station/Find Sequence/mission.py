###
# You are given a matrix of NxN (4≤N≤10).
# You should check if there is a sequence of 4 or more matching digits.
# The sequence may be positioned:
# horizontally, vertically or diagonally(NW-SE or NE-SW diagonals).
###

def checkio(matrix):
    n = len(matrix[0]) #bredd på första elementet, borde ge höjd och langd.
    vilken_ledd = "none"
    langd = 4 # vilken langd ska serien vara.
    answer = False
# första till sista raden -> line
# skanna line för längsta lika, om fyra -> break

    #hitta horisontala
    j=i=0
    for j in range(n):
        line=""
        for i in range(n):
            line=line+str(matrix[j][i])
        antal=long_repeat(line)
##        if antal == langd:
        if antal >= langd:
            answer = True
##            vilken_ledd = "Horizontal"
            break
##        if antal > langd:
##            answer = True
##            vilken_ledd = "Long Horizontal"
            #break

    #hitta vertikala
    j=i=0
    for j in range(n):
        line=""
        for i in range(n):
            line=line+str(matrix[i][j])
        antal=long_repeat(line)
        if antal >= langd:
            answer = True
            break



    #hitta diagonala vä-hö o hö-vä
    ##        vä-hö
    rep=2*n-1
    j=i=x=y=0
    for j in range(rep):
        line=""
        i=rep-j-1
        if j >= n:
            x=n-1
        else:
            x=j
        if i >= n:
            y=n-1
        else:
            y=i
        diagonal=x+y-2
        for k in range(x+y-2):
            line=line+str(matrix[x-k][y-k])
            cordx=x-k
            cordy=y-k
            apa=0

        antal=long_repeat(line)
        if antal >= langd:
            answer = True
            break


    ##        hö-vä
    rep=2*n-1
    j=i=x=y=0
    for j in range(rep):
        line=""
        i=rep-j-1
        if j >= n:
            x=n-1
        else:
            x=j
        if j >= n:
            y=n-i-1
        else:
            y=0
        diagonal=x-y+1
##        print("\n")
        for k in range(x-y+1):
            cordx=x-k
            cordy=y+k
##            print("x:" + str(cordx) + " y:" + str(cordy) + "  :" + str(diagonal))
            line=line+str(matrix[x-k][y+k])
            apa=0

        antal=long_repeat(line)
        if antal >= langd:
            answer = True
            break




    return answer

def long_repeat(line):
    #returnera langden på den med flest lika.
    x=0
    lista=[0]
    tmp=len(line)
    for i in range(len(line)):
        p=line[i]
        if i+1 < len(line):
            r=line[i+1]
        else:
            r="§"
        x=x+1
#        if line[i] != line[i+1]:
        if line[i] != r:
            lista.append(x)
            x=0
    lista.sort(reverse=True)
    return lista[0]

def hitta_längsta(data):
    x = 0
    return x


def fyll_matris(data, matrisen):
##    for i in range

    return matrisen

def bygg_matrisen(data, n):
#    n = len(data[0]) #bredd på första elementet
    matrisen = [[0] * n for i in range(n)]

    return matrisen

def skriv_ut_matris(data):

    for row in data:
        print(' '.join([str(elem) for elem in row]))

    return


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 1, 1, 1],
        [4, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Horizontal 1"
    assert checkio([
        [4, 1, 4, 1],
        [1, 1, 1, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Horizontal 2"
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical 1"
    assert checkio([
        [2, 1, 1, 1],
        [1, 1, 4, 1],
        [3, 1, 1, 6],
        [7, 1, 2, 5]
    ]) == True, "Vertical 2"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
