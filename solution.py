import OZvMO.parser as parser
import OZvMO.LocalExtrema as LocalExtrema
import OZvMO.plot as plot


def solve_task1():
    variab, func, restr = parser.parser_task1()
    output_str, dots = LocalExtrema.local_extrema(variab, func, restr)
    fig = plot.plot(variab, func, restr, dots)
    print(output_str)
    fig.show()


def solve_task2():
    variables, func, restr, restr_func = parser.parser_task2()
    output_str, sol = LocalExtrema.lagrange()
    fig = plot.plot(variab, func, restr, dots)
    print(output_str)
    fig.show()
