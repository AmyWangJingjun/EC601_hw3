# EC601_hw3
Exersice1:
Mat is basically a class with two data parts: the matrix header (containing information such as the size of the matrix,
the method used for storing, at which address is the matrix stored, and so on) and a pointer to the matrix containing 
the pixel values (taking any dimensionality depending on the method chosen for storing). And need to notice that program
access mat via address, but different instanse of mat may have same address.
Basically, a pixel have three dimention, the first two elements stands for the position means rows and colums, which start counting
from the upper left conner,the last dimention stores color information such as RGB HSV values, which can be acessed using index.

