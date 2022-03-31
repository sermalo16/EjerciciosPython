def escribirArchivo(linea, archivo):
    with open(archivo, 'a') as file:
        file.write("\n" + linea)