def localizacion(a,b,c):
    """se localiza el dispositivo por medio de las
   fuerzas de las senales captadas y de la ubicacion de
   las antenas
    """
    d = 100
    i = 500
    j = 100
    #se definen las coordenadas de la Antena A
    ax = -500
    ay = -200
    #se define la cobertura Antena A
    ar = a
    #se definen las coordenadas de la Antena B
    bx = d
    by = -100
    #se definen las coordenadas de la Antena C
    br = b
    cx = i
    cy = j
    #se define la cobertura de la Antena c
    cr = c
    #se localiza la ubicacion del receptor
    x = (ar**2 - br**2 + d**2)/float((2*d))
    y = ((ar**2-br**2+i**2+j**2)/(2*j))-((float(i/j))*x)
    print ("Tu estas ubicado en -> (%s,%s)" %(x, y))

localizacion(100.0, 115.5, 142.7)
