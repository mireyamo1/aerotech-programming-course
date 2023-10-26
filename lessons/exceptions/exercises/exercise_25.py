def weird_number(*args):
    for arg in args:
        try:
            if not isinstance(arg, (int, float, str)):
                raise TypeError(
                    "this function only accepts integers, floats and strings.")
            arg = float(arg)
        except TypeError:
            arg = 0
        else:
            arg = arg ** 3
        finally:
            int(arg) += 1
            return arg


print(weird_number("12a"))
