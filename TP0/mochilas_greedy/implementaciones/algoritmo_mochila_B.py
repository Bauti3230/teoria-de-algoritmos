import utiles

def algorithm_bag_B(W, E):
    if W == 0:
        return []
    
    sorted_e = sorted(E,key=lambda x: x[1]/x[0],reverse=True)
    back_pack = []

    for e in sorted_e:
        while e[0] <= W:
            back_pack.append(e)
            W -= e[0]

        if W == 0:
            return back_pack
    
    return back_pack

contra_ejemplo = [(1000,1000),(2000,2000),(60,60),(100,100)]

 
utiles.print_result(algorithm_bag_B(100,contra_ejemplo)) 