def safe_pawns(pawns):
    antal=0
    if pawns != {""} and pawns != "":
        rad=hitta_högsta_nr(pawns)
        while rad > 1 :
            platser_på_rad=hitta_de_på_en_rad(pawns,rad)
#            vakt_plats=vilka_pos_är_vakternas(platser_på_rad)
#            vakt_plats=sortera_bort_dubletter(vakt_plats)
            for varje_bonde in platser_på_rad:
                bonde=[]
                bonde.append(varje_bonde)
                vakt_plats=vilka_pos_är_vakternas(bonde)
                for vakt in vakt_plats:
                    if vakt in pawns:
                        antal = antal +1
                        break #räcker med en vakt så bryt om en hittas.
            rad = rad -1
    print(str(antal) + " " + str(pawns))
    return antal


high=1

def hitta_högsta_nr(positions):
    high=0
    #print(positions)
    for position in positions:
        #print(position[1])
        #print(type(position[1]))
        if int(position[1]) > high:
            high = int(position[1])
    return high

def översätt_bokstav_till_nr(ch):
    character={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8}
    return character[ch]

def översätt_nr_till_bokstav(nr):
    character={1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",7:"g",8:"h"}
    return character[nr]

def leta_över_och_under(number):
    #leta över och under den som har högsta nr
    #för att hitta de med bokstaven bredvid, d -> c & e fast i nr-form.
    if 1 < number < 8:
        guard=[number-1,number+1]
    if number == 1:
        guard=[0,number+1]
    if number == 8:
        guard=[number-1,0]
    return guard

def vilka_pos_är_vakternas(pos):
    #hitta två platser under pos (tex c5) och returnera de (b4,d4) i en lista
    #inparameter är lista med platser
    resultat=[]
    for i in pos:
        pos_ch=översätt_bokstav_till_nr(i[0])
        pos_nr = int(i[1])
        if pos_nr > 1:
            if pos_ch > 1:
                lo = pos_ch-1
                lo_pos = översätt_nr_till_bokstav(lo)+str(pos_nr-1)
                resultat.append(lo_pos)
            if pos_ch < 8:
                hi = pos_ch+1
                hi_pos = översätt_nr_till_bokstav(hi)+str(pos_nr-1)
                resultat.append(hi_pos)

    return resultat

def hitta_de_på_en_rad(bönder,pos):
    # hittar de bönder som är i en viss rad
    lista=[]

    for topp in bönder:
        if int(topp[1]) == pos:
            lista.append(topp)
    return lista

def sortera_bort_dubletter(bönder):
    lista=[]
    for bonde in bönder:
        if bonde not in lista:
            lista.append(bonde)
    return lista

def hur_många_vakterna_finns_i_bondelistan(bondelista,vakter):
    antal=0
    for vakt in vakter:
        if vakt in bondelista:
            antal=antal+1
    return antal



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert vilka_pos_är_vakternas(["c5"]) == ["b4","d4"]
    assert vilka_pos_är_vakternas(["c5","e5"]) == ["b4","d4","d4","f4"]
    assert sortera_bort_dubletter(["b4","d4","d4","f4"]) == ["b4","d4","f4"]
    assert hur_många_vakterna_finns_i_bondelistan({"b4", "d4", "f4", "c3", "e3", "g5", "d2"},["b4","d4","f4"]) == 3
    assert hitta_de_på_en_rad({"b4", "d4", "f4", "c3", "e3", "g5", "d2"},5) == ["g5"]
    assert vilka_pos_är_vakternas({"g5"})
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    assert safe_pawns({""}) == 0
    assert vilka_pos_är_vakternas({"a1"}) == []
    assert vilka_pos_är_vakternas({"a8"}) == ["b7"]
    assert vilka_pos_är_vakternas({"h8"}) == ["g7"]
    assert safe_pawns({"b4","c4","d4","e4","f4","g4","e3"}) == 2
    #assert safe_pawns({"a1","b2","c3","d4","e5","f6","g7","h8"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
