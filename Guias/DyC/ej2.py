"""
Se cuenta con un vector de “n” posiciones 
en el que se encuentran algunos de los primeros ”m” 
números naturales ordenados en forma creciente (m >= n). 
En el vector no hay números repetidos. 
Se desea obtener el menor número no incluido. 
Ejemplo: [1, 2, 3, 4, 5, 8, 9, 11, 12, 13, 14, 20, 22]. 
Solución: 6. 
Proponer un algoritmo de tipo división y conquista que 
resuelva el problema en tiempo inferior a lineal. 
Expresar su relación de recurrencia y calcular su 
complejidad temporal.
"""

def binary_search(numbers,start,end):
    if end - start <= 0:
        return None
    
    if end - start == 1:
        return start + 2
    
    mid = (start + end) // 2

    if numbers[mid] == mid + 1:
        return binary_search(numbers,mid+1,end)
    
    return binary_search(numbers,start,mid)

def main():
    args = [1, 2, 3, 4, 5, 8, 9, 11, 12, 13, 14, 20, 22]
    s = 0
    e = len(args)

    print(binary_search(args,s,e-1))