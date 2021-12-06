import sympy as sym

ro, lyambda, mu = sym.symbols('ro, l, m')
matrix = sym.Matrix.zeros(9, 9)

matrix[0, 3] = -1 / ro
matrix[1, 4] = -1 / ro
matrix[2, 5] = -1 / ro
matrix[3, 0] = -(lyambda + 2 * mu)
matrix[6, 0] = -lyambda
matrix[8, 0] = -lyambda
matrix[4, 1] = -mu
matrix[5, 2] = -mu

print(*matrix.eigenvals().items(), sep='\n')
