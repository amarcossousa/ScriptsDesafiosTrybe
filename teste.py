from unittest import TestCase, main
from scripts import tripleTheChances, calculadoraAdicaoSubtracao, vezesLetraAparece

class Teste(TestCase):

    def teste_tripleTheChances(self):
        self.assertEqual(tripleTheChances(4), (4, [0, 3, 6, 9]))
    
    def teste_calculadoraAdicaoSubtracao(self):
        self.assertEqual(calculadoraAdicaoSubtracao(2, 3, '+'), 5)
    
    def teste_vezesLetraAparece(self):
        self.assertEqual(vezesLetraAparece('Isso é um teste!', 'e'),2)

if __name__ == '__main__':
    main()

