def ultimo_idx_compatible(cartel,carteles,i):
    idx = 0
    for j in range(i):
        res = cartel[0] - carteles[j][0] 
        if  res <= 5:
            continue

        idx += 1
    return idx
    
def max_carteles(carteles,m):
    carteles.sort(key=lambda x:x[0])
    
    OPT = [0]*(m+1)

    OPT[0] = 0
    OPT[1] = carteles[0][1]

    for i in range(2,len(carteles)+1):
        idx_cmp = ultimo_idx_compatible(carteles[i-1],carteles,i-1)
        OPT[i] = OPT[i-1]

        if idx_cmp == 0:
            OPT[i] = max(OPT[i],carteles[i-1][1])
            continue

        for j in range(idx_cmp+1):
            res1 = OPT[i]
            res2 = carteles[i-1][1] + OPT[j]
            OPT[i] = max(OPT[i],carteles[i-1][1] + OPT[j])


if __name__ == "__main__":
    arr = [(2.5,300),(6,500),(9.8,284),(12.2,600),(18,250)]
    m = 20

    max_carteles(arr,m)



