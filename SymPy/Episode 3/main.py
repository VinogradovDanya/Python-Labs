from scipy.integrate import solve_ivp
import sympy as sy
import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(0, 10, 1000)

x = sy.symbols('x')
y = sy.symbols('y', cls=sy.Function)
sym_sol = sy.dsolve(sy.Eq(y(x).diff(x), - 2 * y(x)), y(x), ics={y(0): np.sqrt(2)})
sym_res = sy.lambdify(x, sym_sol.rhs, 'numpy')


def fun(x_, y_):
    return -2 * y_


sci_res = solve_ivp(fun, [0, 10], [np.sqrt(2)], t_eval=X)

fig, (sci, sym, diff) = plt.subplots(ncols=3)
fig.set_figheight(7)
fig.set_figwidth(14)

sci.grid()
sci.set_title('SciPy')
sci.plot(sci_res.t, sci_res.y[0])

sym.grid()
sym.set_title('SymPy')
sym.plot(X, sym_res(X))

diff.grid()
diff.set_title('Difference')
diff.plot(sci_res.t, sci_res.y[0] - sym_res(sci_res.t))

plt.savefig('res.png')
plt.show()
