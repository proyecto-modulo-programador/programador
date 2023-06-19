def format_data(laws_list):
    print("################\nLEYES: ")
    for law in laws_list:
        print(f"N° Registro: {law[0]} | N° de Normativa: {law[1]} | Fecha: {law[2]} | Palabras clave: '{law[3]}' | Descripción: '{law[4]}' | Tipo normativa: {law[5]} | Categoría: {law[6]} | Jurisdicción: {law[7]} | Órgano legislativo: {law[8]}")
