
import unittest
from bubble_sort import bubble_sort


class TestBubbleSort(unittest.TestCase):
    """Suite de pruebas (Test Suite) para el método bubble_sort.

    Se define un caso de prueba por cada camino de ejecución independiente
    identificado a partir de la complejidad ciclomática V(G) = 4.
    """

    def setUp(self):
        """Arrange global: se ejecuta ANTES de cada caso de prueba."""
        self.resultado = None

    def tearDown(self):
        """Limpieza: se ejecuta DESPUÉS de cada caso de prueba."""
        self.resultado = None

    def test_cp1_lista_un_elemento(self):
        """CP1: la decisión del bucle externo es FALSA (no se entra al bucle)."""
        # Arrange
        lista = [42]
        esperado = [42]

        # Act
        self.resultado = bubble_sort(lista)

        # Assert
        self.assertEqual(self.resultado, esperado)

    def test_cp2_lista_ya_ordenada(self):
        """CP2: se entra a ambos bucles pero el if nunca es verdadero (sin swaps)."""
        # Arrange
        lista = [10, 20, 30]
        esperado = [10, 20, 30]

        # Act
        self.resultado = bubble_sort(lista)

        # Assert
        self.assertEqual(self.resultado, esperado)

    def test_cp3_un_solo_intercambio(self):
        """CP3: el if es VERDADERO y se ejecuta el intercambio (swap)."""
        # Arrange
        lista = [20, 10]
        esperado = [10, 20]

        # Act
        self.resultado = bubble_sort(lista)

        # Assert
        self.assertEqual(self.resultado, esperado)

    def test_cp4_lista_desordenada(self):
        """CP4: múltiples pasadas con varios intercambios (caso general)."""
        # Arrange
        lista = [5, 1, 4, 2, 8]
        esperado = [1, 2, 4, 5, 8]

        # Act
        self.resultado = bubble_sort(lista)

        # Assert
        self.assertEqual(self.resultado, esperado)


if __name__ == "__main__":
    unittest.main()
