def traerLeyes2(leyes):
    print("LEYES: ")
    contador=1
    for l in leyes:
        data = "{0}. Id: {1} | N° de Normativa: {2}| Fecha: {3}| Categoría: {4}| Descripción: {5}| Jurisdicción: {6}| Órgano Legislativo: {7}"
        print(data.format(contador, l[0], l[1], l[2], l[3], l[4], l[5], l[6], l[7]))
        contador = contador +1 