import sys

def solitario(cartas):
    mazos = []

    mazos.append([cartas[-1]])  

    for c in reversed(cartas[:-1]):  
        agregado = False

        for m in mazos:
            carta_top = m[-1]

            if carta_top > c:
                m.append(c)
                agregado = True
                break  

        if not agregado:
            mazos.append([c])  
    
    print(mazos)
    return len(mazos)

def main():
    with open(sys.argv[1], "r") as arch:
        lista = [int(line.strip()) for line in arch]  
    
    print("Mazos resultantes:", solitario(lista))

if __name__ == "__main__":
    main()