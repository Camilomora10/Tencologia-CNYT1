import unittest
import math
from vectores_matrices import suma_vectores, inversa_aditiva_matriz, multi_escalar,suma_matrices,inverso_aditivo_vector
from vectores_matrices import multi_escalar_matriz,transpuesta_matriz_vec,conjugada_matriz_vec,adjunta_mat_vec
from vectores_matrices import producto_matrices,accion_matriz,producto_interno,norma_vector,distance_vectores
from vectores_matrices import matriz_unitaria, matriz_hermitania,producto_tensor
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
#Numeros Complejos
a = [ 1,3 ]
b = [ 2,4 ]
c = [ 6,5 ]
d = [ 4,9 ]
e = [5, 6]

class TestLibComplex(unittest.TestCase):

    def testsuma_vectores(self):
        self.assertEqual(suma_vectores([[a, b], [a, b]]), [[2, 6], [4, 8]])
        self.assertEqual(suma_vectores([a, c], [c, b]),[[7, 8], [8, 9]])

    def testinverso_aditivo(self):
        self.assertEqual(inverso_aditivo_vector([a, c]), [[-1, -3], [-6, -5]])
        self.assertEqual(inverso_aditivo_vector([b, a]), [[-2, -4], [-1, -3]])

    def testmulti_escalar(self):
        self.assertEqual(multi_escalar([a, b], b),[[-10, 10], [-12, 16]])
        self.assertEqual(multi_escalar([b, c], c),[[-8, 34], [11, 60]])

    def testsuma_matrices(self):
        self.assertEqual(suma_matrices([[a, a], [b, b]],[[b, a], [a, b]]), [[[3, 7], [2, 6]], [[3, 7], [4, 8]]])
        self.assertEqual(suma_matrices([[c, a], [a, b]],[[b, c], [b, b]]), [[[8, 9], [7, 8]], [[3, 7], [4, 8]]])

    def testInversa_aditiva_matriz(self):
        self.assertEqual(inversa_aditiva_matriz([[a], [b], [c]]),[[[-1, -3]], [[-2, -4]], [[-6, -5]]])
        self.assertEqual(inversa_aditiva_matriz([[a, a, c], [c, b, a], [d, c, b]]),[[[-1, -3], [-1, -3], [-6, -5]], [[-6, -5], [-2, -4], [-1, -3]],
                                                [[-4, -9], [-6, -5], [-2, -4]]])

    def testmulti_escalar_matriz(self):
        self.assertEqual(multi_escalar_matriz([[c, a], [a, d]], d), [[[-21, 74], [-23, 21]], [[-23, 21], [-65, 72]]])
        self.assertEqual(multi_escalar_matriz([[a, a], [b, b]], c),[[[-9, 23], [-9, 23]], [[-8, 34], [-8, 34]]])

    def testtranspuesta_matriz_vec(self):
        self.assertEqual(transpuesta_matriz_vec([[b, a, a], [a, b, a]]),[[[2, 4], [1, 3]], [[1, 3], [2, 4]], [[1, 3], [1, 3]]])
        self.assertEqual(transpuesta_matriz_vec([[a, b, c], [c, b, a]]),[[[1, 3], [6, 5]], [[2, 4], [2, 4]], [[6, 5], [1, 3]]])

    def testconjugada_matriz_vec(self):
        self.assertEqual(conjugada_matriz_vec([[b, a, c], [c, b, d]]),[[[2, -4], [1, -3], [6, -5]], [[6, -5], [2, -4], [4, -9]]])
        self.assertEqual(conjugada_matriz_vec([[a, b, c], [c, b, a]]),[[[1, -3], [2, -4], [6, -5]], [[6, -5], [2, -4], [1, -3]]])

    def testadjunta_mat_vec(self):
        self.assertEqual(adjunta_mat_vec([[b, a, a], [a, b, a]]),[[[2, -4], [1, -3]], [[1, -3], [2, -4]], [[1, -3], [1, -3]]])
        self.assertEqual(adjunta_mat_vec([[a, b, c], [c, b, a]]),[[[1, -3], [6, -5]], [[2, -4], [2, -4]], [[6, -5], [1, -3]]])

    def testproducto_matrices(self):
        self.assertEqual(producto_matrices([[a, a], [b, b]], [[b, a], [a, b]]),[[[-18, 16], [-18, 16]], [[-22, 26], [-22, 26]]])
        self.assertEqual(producto_matrices([[a, a, b], [b, b, a]], [[b, a], [a, b], [b, b]]),[[[-30, 32], [-30, 32]], [[-32, 36], [-32, 36]]])

    def testaccion_matriz(self):
        self.assertEqual(accion_matriz([[a, c, d], [b, c, b], [d, b, e]], [[e], [d], [c]]), [[[-55, 169]], [[-43, 140]], [[-62, 164]]])
        self.assertEqual(accion_matriz([[a, c, e], [a, c, b], [c, b, e]], [[e], [d], [c]]),[[[-34, 156]], [[-42, 129]], [[-28, 156]]])

    def testproducto_interno(self):
        self.assertEqual(producto_interno([[a],[b],[c]],[[a],[b],[c]],[[[91, 0]]])
        self.assertEqual(producto_interno([[a], [b], [c]], [[a], [a], [a]], [[[45, 15]]])

    def testnorma_vector(self):
        self.assertEqual(norma_vector([[a], [b], [c]]), [9.54])
        self.assertEqual(norma_vector([[c], [d], [e]]), [14.8])

    def testdistance_vectores(self):
        self.assertEqual(distance_vectores([[a], [b], [c]], [[c], [c], [d]]), [8.12])
        self.assertEqual(distance_vectores([[a], [a], [a]], [[c], [c], [d]]), [10.15])

    def testmatriz_unitaria(self):
        a = [1, 0]
        b = [0, 0]
        c = [0, 1]
        self.assertEqual(matriz_unitaria([[c, b], [b, c]]),True)
        self.assertEqual(matriz_unitaria([[a, b], [b, a]]),True)

    def testmatriz_hermitania(self):
        a = [7, 0]
        b = [6, 5]
        c = [6, -5]
        d = [-3, 0]
        e = [1, 0]
        f = [0, 0]
        self.assertEqual(matriz_hermitania([[a, b], [c, d]]),True)
        self.assertEqual(matriz_hermitania([[e, f], [f, e]]),True)

    def testproducto_tensor(self):
        mat1 = [[[2, 0]], [[3, 0]]]
        mat2 = [[[4, 0]], [[6, 0]], [[3, 0]]]
        self.assertEqual(producto_tensor(mat1, mat2),[[[8, 0]], [[12, 0]], [[6, 0]], [[12, 0]], [[18, 0]], [[9, 0]]])
        mat1 = [[b, b, c], [a, c, d], [b, a, c]]
        mat2 = [[a, d, c], [a, b, a], [c, a, d]]
        self.assertEqual(producto_tensor(mat1,mat2),
                         [[-10, 10], [-28, 34], [-8, 34], [-10, 10], [-28, 34], [-8, 34], [-9, 23], [-21, 74], [11, 60]]
                         [[-10, 10], [-12, 16], [-10, 10], [-10, 10], [-12, 16], [-10, 10], [-9, 23], [-8, 34], [-9,23]]
                         [[-8, 34], [-10, 10], [-28, 34], [-8, 34], [-10, 10], [-28, 34], [11, 60], [-9, 23], [-21, 74]]
                         [[-8, 6], [-23, 21], [-9, 23], [-9, 23], [-21, 74], [11, 60], [-23, 21], [-65, 72], [-21, 74]]
                         [[-8, 6], [-10, 10], [-8, 6], [-9, 23], [-8, 34], [-9, 23], [-23, 21], [-28, 34], [-23, 21]]
                         [[-9, 23], [-8, 6], [-23, 21], [11, 60], [-9, 23], [-21, 74], [-21, 74], [-23, 21], [-65, 72]]
                         [[-10, 10], [-28, 34], [-8, 34], [-8, 6], [-23, 21], [-9, 23], [-9, 23], [-21, 74], [11, 60]]
                         [[-10, 10], [-12, 16], [-10, 10], [-8, 6], [-10, 10], [-8, 6], [-9, 23], [-8, 34], [-9, 23]]
                         [[-8, 34], [-10, 10], [-28, 34], [-9, 23], [-8, 6], [-23, 21], [11, 60], [-9, 23], [-21, 74]]

if __name__ == 'main':
    unittest.main()
# Author : Yesid Camilo Mora Barbosa