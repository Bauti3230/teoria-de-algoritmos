
def programa_feria(dict_act,act,m,n):
    
    OPT = [[0 for _ in range(m)] for _ in range(n+1)]

    for fil in OPT: print(fil)

    i = 0
    for a in act:
        list_act = dict_act[a]
        OPT[1][i] = list_act[0]
        i += 1

    for i in range(2,n+1):
        for a in act:
            if a == 'C':
                OPT[i][0] = dict_act[a][i-1] + max(dict_act['H'][i-2],dict_act['V'][i-2],dict_act['D'][i-2])
            if a == 'H':
                OPT[i][1] = dict_act[a][i-1] + max(dict_act['C'][i-2],dict_act['V'][i-2],dict_act['D'][i-2])
            if a == 'D':
                OPT[i][2] = dict_act[a][i-1] + max(dict_act['H'][i-2],dict_act['V'][i-2])
            if a == 'V':
                OPT[i][3] = dict_act[a][i-1] + max(dict_act['H'][i-2],dict_act['D'][i-2])

    return OPT


if __name__ == "__main__":
    act = ['C','H','D','V']

    dict_act = {}
    dict_act.update({'C':[7,1]})
    dict_act.update({'H':[2,8]})
    dict_act.update({'D':[9,3]})
    dict_act.update({'V':[4,6]})

    programa_feria(dict_act,act,4,2)