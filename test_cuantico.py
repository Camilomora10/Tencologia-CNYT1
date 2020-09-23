import unittest
from sistema_clasico_cuantico import canicas_clicks, probabilistico_clicks, cuantico_clicks, grafico

class sistema_clasico_cualtico(unittest.TestCase):

    def testcanicas_clicks(self):
        matriz_booleana = [[True, True, False, False, True, False], [True, True, False, True, False, False],
                           [False, True, False, False, False, True], [False, False, True, False, False, False],
                           [True, False, False, True, True, False], [False, False, False, False, False, False]]

        vector_booleano = [True, True, False, True, False, False]

        self.assertEqual(canicas_clicks(matriz_booleana, vector_booleano, 1), [True, True, True, False, True, False])
        self.assertEqual(canicas_clicks(matriz_booleana, vector_booleano, 5), [True, True, True, True, True, False])
        self.assertEqual(canicas_clicks(matriz_booleana, vector_booleano, 10), [True, True, True, True, True, False])
        self.assertEqual(canicas_clicks(matriz_booleana, vector_booleano, 2020), [True, True, True, True, True, False])

    def testprobabilistico_clicks(self):
        matriz = [[[0, 1], [1 / 6, 0], [5 / 6, 0]], [[1 / 3, 0], [1 / 2, 0], [1 / 6, 0]],
                  [[2 / 3, 0], [1 / 3, 0], [0, 0]]]
        vector = [[[1 / 5, 0]], [[7 / 10, 0]], [[1 / 10, 0]]]
        self.assertEqual(probabilistico_clicks(matriz, vector, 1),[[[0.2, 0.2]], [[0.4333333333333333, 0.0]], [[0.36666666666666664, 0.0]]])

        self.assertEqual(probabilistico_clicks(matriz, vector, 5),[[[-0.07777777777777783, 0.17253086419753086]], [[0.10925925925925925, 0.2132716049382716]],
                                                                  [[0.02962962962962963, 0.22160493827160493]]])

        self.assertEqual(probabilistico_clicks(matriz, vector, 10),[[[-0.08682270233196157, -0.05798718278463648]], [[-0.10747385116598078, 0.04696966449474162]],
                                                                    [[-0.11239283264746223, 0.015690014860539513]]])

        self.assertEqual(probabilistico_clicks(matriz, vector, 2020),[[[-1.5668413920173896e-127, -5.106715877825539e-127]], [[-5.8182349710386965e-127,
                                                                    -1.907947620799566e-127]], [[-4.7755941426900886e-127, -3.288025414703672e-127]]])

    def testcuantico_clisks(self):
        matriz = [[[1/(2**0.5),0], [0, 1/(2**0.5)]],[[1/(2**0.5), 0], [0, -1/(2**0.5)]]]
        vector = [[[1, 0]], [[0, 0]]]

        self.assertEqual(cuantico_clicks(matriz, vector, 1), [0.5041, 0.5041])
        self.assertEqual(cuantico_clicks(matriz, vector, 3), [1.0, 0.0])

        c1 = [-1 / (6 * 0.5), 1 / (6 ** 0.5)]
        c2 = [-1 / (6 ** 0.5), -1 / (6 ** 0.5)]
        c3 = [1 / (6 ** 0.5), -1 / (6 ** 0.5)]

        matriz = [[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                 [[1/2, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                 [[1/2, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                 [[0, 0], c1, [0, 0], [1, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                 [[0, 0], c2, [0, 0], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0]],
                 [[0, 0], c3, c1, [0, 0], [0, 0], [1, 0], [0, 0], [0, 0]],
                 [[0, 0], [0, 0], c2, [0, 0], [0, 0], [0, 0], [1, 0], [0, 0]],
                 [[0, 0], [0, 0], c3, [0, 0], [0, 0], [0, 0], [0, 0], [1, 0]]]
        vector = [[[1, 0]], [[0, 0]], [[0, 0]], [[0, 0]], [[0, 0]], [[0, 0]], [[0, 0]], [[0, 0]]]

        self.assertEqual(cuantico_clicks(matriz, vector, 1), [0.0, 0.25, 0.25, 0.0, 0.0, 0.0, 0.0, 0.0])
        self.assertEqual(cuantico_clicks(matriz, vector, 5), [0.0, 0.0, 0.0, 0.06760000000000001, 0.0841, 0.0016, 0.0841, 0.0841])
        self.assertEqual(cuantico_clicks(matriz, vector, 10), [0.0, 0.0, 0.0, 0.06760000000000001, 0.0841, 0.0016, 0.0841, 0.0841])

if __name__ == '__main__':
    unittest.main()

# Author Yesid Camilo Mora Barbosa
