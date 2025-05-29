"""
nostros queremos crear una fragancia, minimizando el costo de 
elaboracion. tenemos un arreglo con el siguiente formato : 
    [(min, max, precios_ml^2),...]
o sea la cantida minima y maxima de ingrediente que podemos poner y
el costo por ml del ingrediente.
a su vez tenemos una avriable X que seria la cantidad de ml en conjutno
que queremos alcanzar.
"""
def perfumista(ingredientres,X):
    ingredientres.sort(key=lambda x: (x[1] - x[0]) * x[2])

    mezcla = []
    cant_total = 0
    costo_total = 0

    for minimo, maximo, costo in ingredientres:

        usar = minimo 

        if cant_total + usar : 
            usar = X - cant_total
        
        cant_total += usar

        costo_total += usar * costo
        mezcla.append((usar, (minimo, maximo, costo)))

        if cantidad_total < X:
            extra_disponible = maximo - usar
            extra_necesario = X - cantidad_total
            usar_extra = min(extra_disponible, extra_necesario)

            cantidad_total += usar_extra
            costo_total += usar_extra * costo
            mezcla[-1] = (usar + usar_extra, (minimo, maximo, costo))

        if cant_total >= X:
            break
    
    return mezcla, costo_total

        
