# Simatrix
- - -

##  A simple way to generate matrix in Python.
This module provides a simple way to generate a matrix (multidimensional list).
Its shape is similar in design to a cube or numpy ndarray model, with the values
of either integers or floats. The module is based on python's built-in list
and therefore all the list methods are applicable, as well as a few
custom ones, designed for the module.

Some of the common uses are:
- 3D positioning
- Serialised data collection
- An inventory
- - -

## Quick Start
Install the package from pip
```
pip install simatrix
```

Import the matrix module
```
import simatrix.matrix as sim
```
Create your first matrix. Example below has 3 dimensions with 4 rows and 5 columns in each,
and the value of 1 filled in every cell.
```
my_matrix = sim.Matrix(3, 4, 5, 1)
```
The matrix can be navigated through using all three dimensions -  `my_matrix[0][0][0]`,
and is zero indexed like a standard python list.
- - -

## Methods
- `my_matrix.inspect()` - Prints the size of the matrix
- `my_matrix.display()` - Prints each dimension and its content
- `my_matrix.zero()` - Replaces all the values with zeros
- `my_matrix.set_values()` - Replaces all the values with a given integer or float

- - -
## Example
Code:
``` python
# Daily temperature log

import simatrix.matrix as sim
from datetime import datetime as dt


# Get current date information and turn into an index
today = dt.today()
month_id = today.month-1
day_id = today.day-1
hour_id = today.hour-1

# Create matrix with a dimension for each month of the year, row for every day of the month and column for each hour
temperatures = sim.Matrix(12, 31, 24)

# Inspect the size
temperatures.inspect()

# Get current temperature reading in Celsius (hardoced value for the example purposes)
current_temp = 28

# Set the temperature value into. In real life you'd have an hourly reading mechanism instead 
temperatures[month_id][day_id][hour_id] = current_temp

# Display current month's data
temperatures.display(month_id)
```
Output:
```
Matrix objected has been created
--------------
Dimensions: 12 
Rows: 31 
Columns: 24
Total number of cells: 8928
--------------

[0, 0, 0, 0, 0, ... 0, 0, 0, 0, 0]
...
[0, 0, 0, 0, 0, ... 0, 0, 0, 28, 0]
...
[0, 0, 0, 0, 0, ... 0, 0, 0, 0, 0]

```

- - -
## License
MIT License. Free to use in all projects. Any credit to my git account would be great and please consider giving this project a star :)