#include "opencv2/core/core.hpp"
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include "iostream"

 // Author Rishab Shah

using namespace cv;
using namespace std;
 
int main(int argc, char** argv )
{
    Mat src;
    src = imread(argv[1], CV_LOAD_IMAGE_COLOR);
    namedWindow( "Original image", CV_WINDOW_AUTOSIZE );
    imshow( "Original image", src);

	vector<Mat> input_planes0(3);
	split(src,input_planes0);
	Mat channel1_display, channel2_display, channel3_display;
        imshow("Red",   input_planes0[2]);
        cout<<int(input_planes0[2].at<uchar>(20,25))<<endl;
        imshow("Green",   input_planes0[1]);
        cout<<int(input_planes0[1].at<uchar>(20,25))<<endl;
        imshow("Blue",   input_planes0[0]);
        cout<<int(input_planes0[0].at<uchar>(20,25))<<endl;


	Mat ycrcb_image;
	vector<Mat> input_planes(3);
	cvtColor(src, ycrcb_image, CV_BGR2YCrCb);
	split(ycrcb_image,input_planes);
        imshow("Y",   input_planes[0]);
        cout<<int(input_planes[2].at<uchar>(20,25))<<endl;
        imshow("Cb",   input_planes[1]);
        cout<<int(input_planes[2].at<uchar>(20,25))<<endl;
        imshow("Cr",   input_planes[2]);
        cout<<int(input_planes[2].at<uchar>(20,25))<<endl;


	Mat hsv_image;
	cvtColor(src, hsv_image, CV_BGR2HSV);
	vector<Mat> hsv_planes(3);
	split(hsv_image,hsv_planes);
        imshow("Hue",   hsv_planes[0]);
        cout<<int(hsv_planes[0].at<uchar>(20,25))<<endl;
        imshow("Saturation",   hsv_planes[1]);
        cout<<int(hsv_planes[1].at<uchar>(20,25))<<endl;
        imshow("Value",   hsv_planes[2]);
        cout<<int(hsv_planes[2].at<uchar>(20,25))<<endl;


	
    waitKey(0);                                       
    return 0;
} 
// 235
// 138
// 106
// 96
// 96
// 96
// 7
// 140
// 235