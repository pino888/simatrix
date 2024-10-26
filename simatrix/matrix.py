# This module extends a built-in list class and acts as a matrix generator with a few helper methods

class Matrix(list):
    """
    Create a multidimensional matrix of any given number of dimensions and its size and value.

    The returned object is a multidimensional list (similar to numpy ndarray). Always constructed from triple
    index and accessed in such way: matrix[dimension][row][column].

    Parameters
    ----------
    dims: int
        Number of dimension to be created. Must be greater than 0
    rows: int
        Number of rows in each dimension. Must be greater than 0
    cols: int
        Number of columns each row. Must be greater than 0
    value: int | float
        Integer or float value to populate each cell (default 0)


    Methods
    -------
    inspect()
        Prints the size of the matrix
    display()
        Prints each dimension and its content
    zero()
        Replaces all the values with zeros
    set_values()
        Replaces all the values with a given integer or float


    Returns
    -------
    list
        Matrix (multidimensional list) generated from the user input.
    """

    def __init__(self, dims: int, rows: int, cols: int, value: int | float = 0):
        # Validate the input and raise an error if incorrect
        for dimension in [dims, rows, cols]:
            if type(dimension) is not int:
                raise TypeError(f"Dimensional parameter type of {type(dimension)} is invalid, must be {int}")
        if type(value) is not int and type(value) is not float:
            raise TypeError(f"Value parameter type of {type(value)} is invalid, must be {int} or {float}")
        if dims <= 0 or rows <= 0 or cols <= 0:
            raise ValueError(f"Invalid dimensional parameter value, must be greater than zero")

        try:
            super().__init__([[[value for _ in range(cols)] for _ in range(rows)] for _ in range(dims)])
        except TypeError as err:
            print(err)
        except ValueError as err:
            print(err)
        else:
            print("Matrix objected has been created")
            self._dims = dims
            self._rows = rows
            self._cols = cols
            self._value = value

    def inspect(self):
        """
        Prints the size and index levels of a matrix.
        """

        # TODO: more info to be listed
        print(f"--------------\nDimensions: {self._dims} \n"
              f"Rows: {self._rows} \n"
              f"Columns: {self._cols}\n"
              f"Total number of cells: {self._dims*self._rows*self._cols}\n"
              f"--------------\n")

    # TODO: Develop a graphical environment
    def display(self, dim: int = None):
        """Display dimension of a given index. If no index is specified, all dimensions are displayed"""

        if dim:
            print(f"Dimension index {dim}")
            for index, value in enumerate(self[dim]):

                print(value)

        else:
            for index, value in enumerate(self):
                print(f"Dimension index {index}")
                for row in value:
                    print(row)
                print("\n")

    def zero(self):
        """Set all values to 0"""

        for dim in self:
            for row in dim:
                row[:] = [0] * len(row)

    def set_values(self, value: int | float):
        """Set all values to a given integer or a float"""

        if type(value) is not int and type(value) is not float:
            raise TypeError(f"Value parameter type of {type(value)} is invalid, must be {int} or {float}")
        for dim in self:
            for row in dim:
                row[:] = [value] * len(row)
