"""
tenemos 3 instrancias natacion, ciclismo y una carrera a pie (en ese orden). 
para cada corredor teneos los tiempos en los que cada participante tarda en terminar cada prueba.
se nos dice que para la natacion solo se puede realizar de 1 a la vez, esto no pasa 
con el resto de pruebas.
nosotros queremos minimizar el tiempo de la carrera.

OBS :
    tenemos un cuello de botella, ya que no podemos tener a mas de un participante a la vez 
    en la actividad de natacion.
"""
def triatrol(tiempos):
    """ordenamos por el tiempo restante post natacion, o sea que participantes tardan mas"""
    triatrol.sort(key=lambda x: x[1] + x[2],reverse=True)

    """de esta forma los que mas tardan despues de la natacion arrancan antes"""
    return tiempos