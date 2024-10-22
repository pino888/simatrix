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
    show_info()
        Prints the size of the matrix
    display()
        Prints
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
        # TODO: review error handling and run tests
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
            print("Matrix objected created")
        self.dims = dims
        self.rows = rows
        self.cols = cols
        self.value = value

    def show_info(self):
        """
        Prints the size and index levels of a matrix.
        """
        # TODO: more info to be listed
        print(f"--------------\nDimensions: {self.dims} \nRows: {self.rows} \nColumns: {self.cols}\n--------------\n")

    # TODO: Develop a graphical environment
    def display(self):
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
        """Set all values to a given integer or float"""
        if type(value) is not int and type(value) is not float:
            raise TypeError(f"Value parameter type of {type(value)} is invalid, must be {int} or {float}")
        for dim in self:
            for row in dim:
                row[:] = [value] * len(row)
