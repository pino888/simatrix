

def simple_matrix(dims: int, rows: int, cols: int, value: int | float = 0) -> list:
    """
    Create a multidimensional matrix of any given number of dimensions and its size and value.

    Args:
        dims (int): Number of dimension to be created. Must be greater than 0.
        rows (int): Number of rows in each dimension. Must be greater than 0.
        cols (int): Number of columns each row. Must be greater than 0.
        value (int|float): Integer or float value to populate each cell. Default 0.

    Returns:
        list: Matrix (multidimensional list) generated from the user input.
    """

    try:
        # Check the input and raise an error if invalid, otherwise create the matrix
        for dimension in [dims, rows, cols]:
            if type(dimension) is not int:
                raise TypeError(f"Dimensional parameter type of {type(dimension)} is invalid, must be {int}")
        if type(value) is not int and type(value) is not float:
            raise TypeError(f"Value parameter type of {type(value)} is invalid, must be {int} or {float}")
        if dims <= 0 or rows <= 0 or cols <= 0:
            raise ValueError(f"Invalid dimensional parameter value, must be greater than zero")
        matrix = [[[value for _ in range(cols)] for _ in range(rows)] for _ in range(dims)]

    except NotImplementedError as e:
        print(e)

    else:
        return matrix


# FURTHER DEVELOPMENT
# Display matrix content - to be developed
def display_matrix(matrix: list):
    if type(matrix) is not list:
        raise TypeError(f"Provided matrix type of {type(matrix)} is invalid, must be {list}")
    for index, value in enumerate(matrix):
        print(f"Dimension index {index}")
        for row in value:
            print(row)
        print("\n")


# Display shape/info function

# Clear matrix values function
