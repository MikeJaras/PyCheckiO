def sun_angle(time):

    tid  = time_till_minuter(time)
    if syns_solen(tid):
        time = tid_till_vinkel(tid)
    else:
        time = "I don't see the sun!"

    return time




def time_till_minuter(time):
    time_list = time.split(":")
    tid=int(time_list[0])*60+int(time_list[1])
    return tid

def tid_till_vinkel(tid):
    # tid i minuter
    # 18 * 60 = 1080
    # 06 * 60 = 360
    vinkel = (tid - 360)/(1080-360)*180
    return float('{:.5g}'.format(vinkel))

def syns_solen(tid):
    if 360 <= tid <= 1080:
        dag = True
    else:
        dag = False
    return dag

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_till_minuter("06:00") == 360
    assert tid_till_vinkel(720) == 90
    assert tid_till_vinkel(813) == 113.25
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
