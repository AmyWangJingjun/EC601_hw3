# EC601_hw3
Exercise 1:

1/  Mat is basically a class with two data parts: the matrix header (containing information such as the size of the matrix,the method used for storing, at which address is the matrix stored, and so on) and a pointer to the matrix containing the pixel values (taking any dimensionality depending on the method chosen for storing). And need to notice that program access mat via address, but different instanse of mat may have same address.
2/  Basically, a pixel have three dimention, the first two elements stands for the position means rows and colums, which start counting from the upper left conner,the last dimention stores color information such as RGB HSV values, which can be acessed using index.

Exercise 2:

1/  the RGB stands for red green blue, while the color of the pixel has more red, then the red channel appears nearly white（take the baloon example, the red nose part is nearly white in red channel as well as the blue part appears white in the blue channel ）
2/  Ycrcb: Y stands for brightness of a picture, as in baloon case the Y channel appears the same intense of brightness as we see in the original image, but a grayscale one; Cr stands for red channel, somewhat like the R channel in RGB, which has bigest value on nose, which appears nearly white; Cb stands for blue channel, like B channel in RGB, appears white in blue region around nose.
3/  HSV:HUE essentially refers to a color having full saturation; VALUE refers to the lightness or darkness of a color, like Y in Ycrb. SATURATION defines the brilliance and intensity of a color.  
(the output image is in exercise 2 folder)
#the pixel value in hsv is[34 97 165]
#the pixel value in YCrBr is[155 129 98]
#the pixel value in BGR is[102 165 156]

Exercise 3:

1/  for the filter feature: the gaussian filter has better result for a gaussian noise image, and median filter is better for salt and pepper noise filter. 

2/  for the kernal feature: greater kernal value stands for how deep the image is processed by the filter, bigger kernal size will make the image more blurry. If the image is highly influenced by noise, then big kernal filter is suitable, otherwise, if there is litte noise on a image, then we do not need to use big kernal filter, it will decrease the resolution of the image. So we should chose the kernal size differently case by case. 

