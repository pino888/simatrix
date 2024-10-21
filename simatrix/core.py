# This is the main matrix generator module with a few helper functions

class Matrix(list):
    def __init__(self, dims: int, rows: int, cols: int, value: int | float = 0):
        super().__init__([[[value for _ in range(cols)] for _ in range(rows)] for _ in range(dims)])
        self.dims = dims
        self.rows = rows
        self.cols = cols
        self.value = value

    def get_list(self):
        return self

    def show_info(self):
        # maybe more info
        print(f"--------------\nDimensions: {self.dims} \nRows: {self.rows} \nColumns: {self.cols}\n--------------\n")

    def display(self):
        pass

    def reset(self):
        pass
