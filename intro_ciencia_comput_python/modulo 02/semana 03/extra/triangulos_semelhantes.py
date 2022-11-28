class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        return self.a + self.b + self.c

    def tipo_lado(self):
        if self.a == self.b and self.a == self.c:
            return 'equilátero'
        elif self.a != self.b and self.a != self.c and self.b != self.c:
            return 'escaleno'
        else:
            return 'isósceles'

    def retangulo(self):
        import math
        lista = sorted([self.a, self.b, self.c])
        if lista[-1] ** 2 == (lista[0] ** 2) + (lista[1] ** 2):
            return True
        else:
            return False

    def semelhantes(self, triangulo):
        listaSelf = sorted([self.a, self.b, self.c])
        listaTriangulo = sorted([triangulo.a, triangulo.b, triangulo.c])

        if listaSelf[0] / listaTriangulo[0] == listaSelf[1] / listaTriangulo[1] and listaSelf[0] / listaTriangulo[0] == listaSelf[2] / listaTriangulo[2]:
            return True
        else:
            return False
        
