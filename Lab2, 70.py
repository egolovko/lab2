"""
NAME
    Lab2, 70

DESCRIPTION
    This program calculates the sum of the power series, defined on the segment [A, B], with precision
"""

A = 0.
B = 1.


def s(x: float, positive_eps: float) -> float:
    """ Calculate the value of sum of the power series, defined on segment [0, 1], with precision eps

    :param x: the parameter of the sum of the power series
    :param eps: precision
    :return: return the calculated sum of the power series with precision eps
    """
    n = 0
    fraction =  x/2
    sigma = fraction

    x = -x
    negative_eps = -positive_eps
    while not (negative_eps < fraction < positive_eps):
        n += 1
        
        fraction *= x*n*n / (2*n + 1) / (2*n + 2)
        sigma += fraction

    return sigma


def _display_result(inp: float, eps: float, out: float):
    """ Display the result (out) of f(x) for inp

    :param inp: program input value
    :param eps: precision
    :param out: calculated value
    """

    print(f"for x = {inp:.5f}")
    print(f"for eps = {eps:.4e}")
    print(f"result = {out:.9f}")


def _display_error(error: BaseException):
    """ Display the error with custom description

    :param error: error with custom description
    """
    print("***** Error")
    print(error)



def _check_point(x:float) -> bool:
    """ Check the domain of function s(x, eps) for x

    :param x: the first parameter for S(x, eps) that must be checked
    :return: True if x is domain else False
    """
    return A <= x <= B


def _check_eps(eps:float) -> bool:
    """ Check the eps value to positive

    :param eps: the second parameter for S(x, eps) that must be checked
    :return: True if x is positive else False
    """
    return eps > 0


def input_float(prompt:str="") -> float:
    """ Send input request and return converted value if it possible

    :param prompt: custom description
    :return: converted value from terminal/command prompt
    :raises KeyboardInterrupt: if Ctrl+C was pressed when program wait the input
    :raises ValueError: if input value not possible to convert
    :raises Exception: If no input
    """
    try:
        input_data = input(prompt)
    except KeyboardInterrupt:
        raise KeyboardInterrupt("Input was aborted")
    except:
        raise Exception("There are no input to convert to float.")

    try:
        float_data = float(input_data)
    except ValueError:
        raise ValueError("Invalid data format. Input data must contain symbols for number translation. \n" + \
            "Check the example on the end of input request message and try again.")
    return float_data


def input_with_check(prompt:str="", check=lambda x: True) -> float:
    """ Get float value and check it by check function

    :param prompt: custom description
    :param check: function (f(x:float) -> bool) that can check value
    :return: correct input data
    :raises ValueError: if data not correct (function check(x) return False)
    """
    data = input_float(prompt)
    if not check(data):
        raise ValueError(f"Incorrect data. Point must be in  ({A} <= input number <= {B}) and eps must be positive")
    return data


def _main():
    """Program entry point"""

    print(f"This program calculates the sum of the power series, defined on the segment [{A}, {B}], with precision")
    print("This program is coded by Holovko Eugene, K-12.")

    try:
        point = input_with_check(f"Enter the point ({A} <= number <= {B})(Example: 0.22): ", _check_point)
        eps = input_with_check("Enter the precision (Example 1e-6): ", _check_eps)
    except Exception as e:
        _display_error(e)
    else:
        print("***** do calculations ...", end=" ")
        output_data = s(point, eps)
        print("done")

        _display_result(point, eps, output_data)


if __name__ == "__main__":
    try:
        _main()
    except KeyboardInterrupt:
        _display_error(KeyboardInterrupt("Program was aborted"))
