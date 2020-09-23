import unittest
import libreriaComplejos
"""
                                              Introduccion
Antes de empezar se debe tener en cuenta la forma en que los numeros complejos seran representados,
como se sabe los numeros complejos se caracterizan por tener una parte real  y una imaginaria como se observa a continuacion:
    a + bi
lo equivalente para la libreria sera una lista de longitud 2, cuya posicion 0 sera la parte real y la posicion 1 la parte imaginaria;
con respecto al numero anterior el equivalente en la libreria  sera:
    [a,b]
Un vector de 2 elementos complejo seria:
    | a + bi |
    | c + di |
En nuestra libreria sera:
   [ [[a,b]], [[e,f]] ]
Un numero en forma polar sera:
   (r, θ) 
"""


class unit_libreriaComplejos(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(libreriaComplejos.suma_complejos([6, 10], [-15, -5], [-9 , 5])
        self.assertEqual(libreriaComplejos.suma_complejos([2, 11], [-14, -4], [-12, 7])
        self.assertEqual(libreriaComplejos.suma_complejos([3,  4], [-2 , -1], [1  , 3])
        self.assertEqual(libreriaComplejos.suma_complejos([7, 10], [12 , -5], [19 , 5])
        self.assertEqual(libreriaComplejos.suma_complejos([6, -2], [11 , -3], [17 ,-5])
        self.assertEqual(libreriaComplejos.suma_complejos([5, -5], [10 , -4], [15 ,-9])
        self.assertEqual(libreriaComplejos.suma_complejos([3, -1], [14 , -5], [17 ,-6])
        self.assertEqual(libreriaComplejos.suma_complejos([1, -3], [15 , -2], [16 ,-5])

    def test_mult(self):
        self.assertEqual(libreriaComplejos.producto_complejos([-1, 2], [1, -22], [43,24])
        self.assertEqual(libreriaComplejos.producto_complejos([-6, 4], [4, -11], [20,82])
        self.assertEqual(libreriaComplejos.producto_complejos([-2, 7], [5, -15], [95,65])
        self.assertEqual(libreriaComplejos.producto_complejos([-4, 9], [8, -35], [283,212])
        self.assertEqual(libreriaComplejos.producto_complejos([6, 10], [15, -5], [140,120])
        self.assertEqual(libreriaComplejos.producto_complejos([6, 11], [11, -6], [132,85])
        self.assertEqual(libreriaComplejos.producto_complejos([6, 13], [12, -5], [137,126])
        self.assertEqual(libreriaComplejos.producto_complejos([6, 12], [13, -3], [114,138])

    def test_resta(self):
        self.assertEqual(libreriaComplejos.resta_complejos([6, 10], [-15, -5], [21,15])
        self.assertEqual(libreriaComplejos.resta_complejos([2, 11], [-14, -4], [16,15])
        self.assertEqual(libreriaComplejos.resta_complejos([3,  4], [-2 , -1], [5,5])
        self.assertEqual(libreriaComplejos.resta_complejos([7, 10], [12 , -5], [-5,15])
        self.assertEqual(libreriaComplejos.resta_complejos([6, -2], [11 , -3], [-5,1])
        self.assertEqual(libreriaComplejos.resta_complejos([5, -5], [10 , -4], [-5,-1])
        self.assertEqual(libreriaComplejos.resta_complejos([3, -1], [14 , -5], [-11,4])
        self.assertEqual(libreriaComplejos.resta_complejos([1, -3], [15 , -2], [-14,-1])

    def test_division(self):
        self.assertEqual(libreriaComplejos.division_complejos([6, 10], [-15, -5],[-0.56,-0.48])
        self.assertEqual(libreriaComplejos.division_complejos([2, 11], [-14, -4],[-0.33,-0.68])
        self.assertEqual(libreriaComplejos.division_complejos([3, 4 ], [-2 , -1],  [-2.0,-1.0])
        self.assertEqual(libreriaComplejos.division_complejos([7, 10], [12 , -5],  [0.20,0.91])
        self.assertEqual(libreriaComplejos.division_complejos([6, -2], [11 , -3], [0.55,-0.03])
        self.assertEqual(libreriaComplejos.division_complejos([5, -5], [10 , -4], [0.60,-0.25])
        self.assertEqual(libreriaComplejos.division_complejos([3, -1], [14 , -5], [0.21, 0.01])
        self.assertEqual(libreriaComplejos.division_complejos([1, -3], [15 , -2], [0.09,-0.18])

    def test_modulo(self):
        self.assertEqual(libreriaComplejos.modulo_complejos([-3, 4], [5.0])
        self.assertEqual(libreriaComplejos.modulo_complejos([-2, 4], [4.47])
        self.assertEqual(libreriaComplejos.modulo_complejos([3, 12], [12.36])
        self.assertEqual(libreriaComplejos.modulo_complejos([6, -4], [7.21])
        self.assertEqual(libreriaComplejos.modulo_complejos([4, -9], [9.84])
        self.assertEqual(libreriaComplejos.modulo_complejos([7, -5], [8.60])
        self.assertEqual(libreriaComplejos.modulo_complejos([9, 41], [41.97])
        self.assertEqual(libreriaComplejos.modulo_complejos([1, -4], [4.12])

    def test_angulo(self):
        self.assertEqual(libreriaComplejos.angulo_complejos([-6, 15], [1.951])
        self.assertEqual(libreriaComplejos.angulo_complejos([6, -15], [5.093])
        self.assertEqual(libreriaComplejos.angulo_complejos([6,  15], [1.19])
        self.assertEqual(libreriaComplejos.angulo_complejos([-6, -15], [4.332])
        self.assertEqual(libreriaComplejos.angulo_complejos([-7, -15], [4.276])
        self.assertEqual(libreriaComplejos.angulo_complejos([-7, 15], [2.007])
        self.assertEqual(libreriaComplejos.angulo_complejos([-6, -12], [4.249])
        self.assertEqual(libreriaComplejos.angulo_complejos([-6, -11], [4.213])
        self.assertEqual(libreriaComplejos.angulo_complejos([-6, -5], [3.836])

    def test_conjugado(self):
        self.assertEqual(libreriaComplejos.conjugado_complejos([-45, 3], [-45, -3])
        self.assertEqual(libreriaComplejos.conjugado_complejos([-23, 5], [-23, -5])
        self.assertEqual(libreriaComplejos.conjugado_complejos([-40, 6], [-40, -6])
        self.assertEqual(libreriaComplejos.conjugado_complejos([-15, 8], [-15, -8])
        self.assertEqual(libreriaComplejos.conjugado_complejos([-46, -2], [-46, 8])
        self.assertEqual(libreriaComplejos.conjugado_complejos([-25, -1], [-25, 1])
        self.assertEqual(libreriaComplejos.conjugado_complejos([-95, -8], [-95, 8])
        self.assertEqual(libreriaComplejos.conjugado_complejos([-42, -9], [-42, 9])

    def test_polarcart(self):
        self.assertEqual(libreriaComplejos.polares_cartesianas_complejos([2, 32], [ 1.66, 1.10])
        self.assertEqual(libreriaComplejos.polares_cartesianas_complejos([1, 34], [-0.84, 0.52])
        self.assertEqual(libreriaComplejos.polares_cartesianas_complejos([2, 22], [-1.99,-0.02])
        self.assertEqual(libreriaComplejos.polares_cartesianas_complejos([5, 67], [-2.58,-4.27])
        self.assertEqual(libreriaComplejos.polares_cartesianas_complejos([2, 0.22], [1.95,0.43])
        self.assertEqual(libreriaComplejos.polares_cartesianas_complejos([8, 0.55], [6.82,4.18])
        self.assertEqual(libreriaComplejos.polares_cartesianas_complejos([9, 0.44], [8.14,3.83])
        self.assertEqual(libreriaComplejos.polares_cartesianas_complejos([2, 0.33], [1.89,0.64])

    def test_cartepoalr(self):
        self.assertEqual(libreriaComplejos.polares_cartesianas_complejos([2, 22], [22.09,1.48])
        self.assertEqual(libreriaComplejos.polares_cartesianas_complejos([3, 12], [12.36,1.32])
        self.assertEqual(libreriaComplejos.polares_cartesianas_complejos([4, 3], [5.0, 0.64])
        self.assertEqual(libreriaComplejos.polares_cartesianas_complejos([2, 3], [3.60,0.98])
        self.assertEqual(libreriaComplejos.polares_cartesianas_complejos([6, 3], [6.70,0.46])
        self.assertEqual(libreriaComplejos.polares_cartesianas_complejos([1, 4], [4.12,1.32])
        self.assertEqual(libreriaComplejos.polares_cartesianas_complejos([3, 9], [9.48,1.24])
        self.assertEqual(libreriaComplejos.polares_cartesianas_complejos([2, 5], [5.38,1.19])

if __name__ == 'main':
    unittest.main()
# Author : Yesid Camilo Mora Barbosa