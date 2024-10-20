# Simatrix

##  A simple way to generate matrix.
Simatrix provides a simple way to generate a multidimensional matrix,
saving on writing the loops each time you need it.


## Quick Start
Install from pip or clone the GitHub repository
```
pip install simatrix

clone .....
```

Import the package
```
import simatrix.matrix as sim
```
Create your first matrix. Example below has 3 dimensions with 4 rows and 5 columns in each,
and the value of 1 filled in every cell.
```
my_matrix = sim.simple_matrix(3, 4, 5, 1)
```
The matrix can be navigated through using all three dimensions ```my_matrix[0][0][0]```, zero indexed
like standard python list.



## License
MIT License. Free to use it in any of your projects, either personal or commercial
use. Any credit to my git account would be great and please consider giving this project a star :)