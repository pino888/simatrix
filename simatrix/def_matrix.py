# This is the main matrix generator module with a few helper functions
from matrix import Matrix

popo = Matrix(3, 2, 3, 9)

popo.show_info()


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


# Display matrix content
# TODO: Develop a graphical environment
def display_matrix(matrix: list):
    if type(matrix) is not list:
        raise TypeError(f"Provided matrix type of {type(matrix)} is invalid, must be {list}")
    for index, value in enumerate(matrix):
        print(f"Dimension index {index}")
        for row in value:
            print(row)
        print("\n")


def show_info(matrix: list):
    """
    Prints size of a matrix.
    :param matrix:
    :return: Info about each parameter of given matrix
    """
    # TODO: review error handling and run tests
    if type(matrix) is not list:
        raise TypeError(f"Provided matrix type of {type(matrix)} is invalid, must be {list}")
    try:
        print(f"--------------\n"
              f"Dimensions: {len(matrix)} \nRows: {len(matrix[0])} \nColumns: {len(matrix[0][0])}"
              f"\n--------------\n")

    except TypeError:
        raise TypeError(f"Provided matrix does not meet the criteria, make sure it has 3 levels")


a = simple_matrix(1, 5, 4, 8)
b = [[2.1], [0.2]]
#display_matrix(a)


# Reset matrix values function
def reset_values(matrix: list):
    matrix[:] = [[[0 for _ in range(len(matrix[0][0]))] for _ in range(len(matrix[0]))] for _ in range(len(matrix))]


reset_values(a)
#display_matrix(a)

if __name__ == "__main__":
    print("Running at base level")
