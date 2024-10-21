# This is the main matrix generator module with a few helper functions

class Matrix(list):
    """
    Creates a multidimensional matrix of any given number of dimensions and its size and value. Always displayed
    and accessed by triple index [n][n][n].

    Args:
        dims (int): Number of dimension to be created. Must be greater than 0.
        rows (int): Number of rows in each dimension. Must be greater than 0.
        cols (int): Number of columns each row. Must be greater than 0.
        value (int|float): Integer or float value to populate each cell. Default 0.

    Returns:
        list: Matrix (multidimensional list) generated from the user input.
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
        super().__init__([[[value for _ in range(cols)] for _ in range(rows)] for _ in range(dims)])
        self.dims = dims
        self.rows = rows
        self.cols = cols
        self.value = value

    def show_info(self):
        """
        Prints size of a matrix.
        :param self:
        :return: Info about each parameter of given matrix
        """
        # maybe more info
        print(f"--------------\nDimensions: {self.dims} \nRows: {self.rows} \nColumns: {self.cols}\n--------------\n")

    def display(self):
        pass

    def reset(self):
        """Set all values to 0"""
        for dim in self:
            for row in dim:
                row[:] = [0] * len(row)
