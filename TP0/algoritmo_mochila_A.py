import utiles

def algorithm_bag_A(W, E):
    if W == 0:
        return []
    
    sorted_e = sorted(E,key=lambda x: x[1],reverse=True)
    back_pack = []

    for e in sorted_e:
        while e[0] <= W:
            back_pack.append(e)
            W -= e[0]

        if W == 0:
            return back_pack
    
    return back_pack

contra_ejemplo = [(20,100),(5,20),(5,60),(10,60),(5,10)]

utiles.print_result(algorithm_bag_A(20,contra_ejemplo))