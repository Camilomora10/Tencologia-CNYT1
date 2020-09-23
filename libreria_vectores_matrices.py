from libreriaComplejos import suma_complejos, resta_complejos, producto_complejos, conjugado_complejos

"""
Introduccion
Antes de empezar se debe tener en cuenta la forma en que los numeros complejos seran representados, 
como se sabe los numeros complejos se caracterizan por tener una parte real  y una imaginaria como se observa a continuacion:
a + bi
lo equivalente para la libreria sera una lista de longitud 2, cuya posicion 0 sera la parte real y la posicion 1 la parte imaginaria;
con respecto al numero anterior el equivalente en la libreria  sera:
[a,b]
Ademas para representar vectores y matrizes lo haremos por medio de listas en donde la longitud 
de la lista seran las filas y las columnas la longitud de las filas.

Una matriz de tamaño 2x2 compleja seria:
         | a + bi   c + di |
         | e + fi   g - hi |
En nuestra libreria sera:
    [ [[a,b],[c,d]], [[e,f],[g,h]] ]
Un vector de 2 elementos complejo seria:
         | a + bi |
         | c + di |
En nuestra libreria sera:
      [ [[a,b]], [[e,f]] ]
"""

def suma_vectores(vector1:list,vector2:list):
    """
    Funcion que suma vectores complejos.
    :param vector1: lista que representa el vector 1 complejo
    :param vector2: lista que representa el vector 2 complejo
    :return: Lista que representa la suma de los 2 vectores  complejos
    """
    fila = len(vector1)
    columnas = len(vector1[0])
    for i in range(fila):
        for j in range(columnas):
            vector1[i][j] = suma_complejos(vector1[i][j], vector2[i][j])
    return vector1

def inverso_aditivo_vector(vector:list):
    """
    Funcion que realiza el inverso aditivo de un vector complejo.
    :param vector: lista que representa el vector complejo
    :return: lista que representa del inverso aditivo del vector.
    """
    for i in range(len(vector)):
        for j in range(len(vector[0])):
            vector[i][j] = producto_complejos(vector[i][j],[-1,0])
    return vector


def multi_escalar(vector:list,num:list) :
    """
    Funcion que realiza la multiplicacion de un escalar complejo por un vector complejo.
    :param vector: lista que representa el vector complejo.
    :param num: lista que representa el escalar complejo.
    :return: lista que representa el vector resultante.
    """
    fila = len(vector)
    col = len(vector[0])
    for i in range(fila):
        for j in range(col):
            vector[i][j] = producto_complejos(vector[i][j],num)
    return vector


def suma_matrices(mat_1:list, mat_2:list):
    """
    Funcion que realiza la suma de 2 matrices complejas.
    Recuerde que para sumar 2 matrices deben tener el mismo tamaño.
    :param mat_1: lista que representa la matriz 1 compleja.
    :param mat_2: lista que representa la matriz 1 compleja.
    :return: Lista que representa la suma de las 2 matrices complejas.
    """
    fila = len(mat_1)
    columnas = len(mat_1[0])
    for i in range(fila):
        for j in range(columnas):
            mat_1[i][j] = suma_complejos(mat_1[i][j], mat_2[i][j])
    return mat_1


def inversa_aditiva_matriz(mat:list):
    """
    Funcion que realiza la inversa aditiva de una matriz compleja.
    :param mat: Lista que representa la matriz compleja
    :return: Lista que representa la inversa aditiva de la matriz compleja.
    """
    res = inverso_aditivo_vector(mat)
    return res

def transpuesta_matriz_vec(mat):
    """
    Funcion que realiza la transpuesta de una matriz o vector complejo.
    :param mat: lista que representa la matriz o vector complejo.
    :return: Lista que representa la transpues de la matriz o vector complejo.
    """
    fila = len(mat)
    columnas = len(mat[0])
    trans = []
    for i in range(columnas):
        trans.append([])
        for j in range(fila):
            trans[i].append(mat[j][i])
    return trans

def multi_escalar_matriz(mat:list,num:list):
    """
    Funcion que realiza la multiplicacion de un escalar complejo por una matriz compleja.
    :param mat: lista que representa la matriz compleja.
    :param num: Lista que representa el escalar complejo.
    :return: Lista que representa la matriz compleja resultante.
    """
    fila = len(mat)
    columnas = len(mat[0])
    resul = []
    for i in range(fila):
        resul.append([])
        for j in range(columnas):
            resul[i].append(producto_complejos(mat[i][j], num))
    return resul

def conjugada_matriz_vec(mat:list):
    """
    Funcion que realiza la conjugada de una matriz o vector complejo.
    :param mat: Lista que representa la matriz o vector complejo.
    :return: lista que representa la matriz o vector resultante.
    """
    fila = len(mat)
    columnas = len(mat[0])
    resul = []
    for i in range(fila):
        resul.append([])
        for j in range(columnas):
            resul[i].append(conjugado_complejos(mat[i][j]))
    return resul

def adjunta_mat_vec(mat:list):
    """
    Funcion que realiza la adjunta de una matriz compleja.
    :param mat: Lista que representa la matriz compleja.
    :return: Lista que representa la matriz adjunta compleja.
    """
    res = conjugada_matriz_vec(transpuesta_matriz_vec(mat))
    return res

def producto_matrices(mat_1:list,mat_2:list):
    """
    Funcion que realiza el producto de dos matrices complejas.
    Recuerde que para multiplicar sus tamaños deben ser compatibles,
    las columnas de la matriz 1 iguales a las filas de la matriz 2.
    :param mat_1: Lista que representa la matriz 1 compleja.
    :param mat_2: Lista que representa la matriz 2 compleja.
    :return: Lista que representa la matriz resultante compleja.
    """
    fila_1 = len(mat_1)
    fila_2 = len(mat_2)
    columna_1 = len(mat_1[0])
    columna_2 = len(mat_2[0])
    matriz = []
    for i in range(fila_1):
        matriz.append([[0,0]]*columna_2)
    for i in range(fila_1):
        for j in range(columna_2):
            for k in range(columna_1):
                matriz[i][j] = suma_complejos(matriz[i][j],producto_complejos(mat_1[i][k],mat_2[k][j]))
    return matriz


def accion_matriz(mat:list,vec:list):
    """
    Funcion que representa la accion de una matriz compleja sobre un vector complejo.
    Recuerde que para poder realizar la operacion las columnas de la matriz
    deben ser iguales a las filas del vecor.
    :param mat: Lista que representa la matriz compleja.
    :param vec: Lista que representa el vector complejo.
    :return: Lista que representa el vector complejo resultante
    """
    respuesta = producto_matrices(mat,vec)
    return respuesta

def producto_interno(vec1:list,vec2:list):
    """
    Funcion que representa el producto interno de dos vectores complejos.
    :param vec1: Lista que representa el vector 1 complejo.
    :param vec2: Lista que representa el vector 2 complejo.
    :return: Lista que representa el vector complejo resultante.
    """
    respuesta = producto_matrices(adjunta_mat_vec(vec1),vec2)
    return respuesta

def norma_vector(vector:list):
    """
    Funcion que realiza la norma de un vector complejo.
    :param vector: Lista que representa el vector complejo.
    :return: Lista que representa la norma del vector complejo.
    """
    fila = len(vector)
    columna = len(vector[0])
    magnitud = 0
    for i in range(fila):
        for j in range(columna):
            magnitud += (vector[i][j][0])**2 + (vector[i][j][1])**2
    rta = [round(magnitud**0.5, 2)]
    return rta

def distance_vectores(vec1:list,vec2:list):
    """
    Funcion que determina la distancia entre dos vectores complejos.
    :param vec1: Lista que representa el vector 1 complejo
    :param vec2: lista que representa el vector 2 complejo
    :return: Lista que representa la distancia de los dos vectores complejos.
    """
    fila = len(vec1)
    columnas = len(vec1[0])
    for i in range(fila):
        for j in range(columnas):
            vec1[i][j] = resta_complejos(vec1[i][j], vec2[i][j])
    res = norma_vector(vec1)
    return res

def matriz_unitaria(matriz:list):
    """
    Funcion que determina si una matriz compleja es unitaria o no.
    :param matriz: lista que representa la matriz compleja
    :return: Bool que representa si es unitaria o no.
    """
    identi = []
    for i in range(len(matriz)):
        identi.append([])
        for j in range(len(matriz[0])):
            if i == j:
                identi[i].append([1, 0])
            else:
                identi[i].append([0,0])
    adjunta = adjunta_mat_vec(matriz)
    opcion1 = producto_matrices(adjunta,matriz)
    opcion2 = producto_matrices(matriz,adjunta)
    if opcion1 == opcion2:
        if opcion1 == identi:
            return True
    else:
        return False

def matriz_hermitania(matriz:list):
    """
    Funcion que determina si una matriz compleja es hermitiana o no.
    :param matriz: Lista que representa la matriz compleja.
    :return: Bool que representa si es hermitiana o no.
    """
    adjunta = adjunta_mat_vec(matriz)
    if adjunta == matriz:
       return True
    else:
       return False

def producto_tensor(mat1:list,mat2:list):
    """
    Funcion que determina el producto tensor entre dos matrices complejas.
    :param mat1: Lista que representa la matriz 1 compleja.
    :param mat2: Lista que representa la matriz 2 compleja.
    :return: Lista que representa la matriz compleja resultante.
    """
    fila1 = len(mat1)
    fila2 = len(mat2)
    col1 = len(mat1[0])
    col2 = len(mat2[0])
    matriz = []
    for i in range(fila1*fila2):
        matriz.append([])
        for j in range(col1*col2):
            matriz[i].append([0,0])
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] = producto_complejos(mat1[i//fila2][j//fila1],mat2[i%fila2][j%fila1])
    return matriz

