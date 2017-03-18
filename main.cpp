#include <cv.h>
#include <highgui.h>
#include <opencv2/opencv.hpp>
#include <iostream>

using namespace cv;

int main(){

    int state=0;   

    VideoCapture cap(0); // open the default camera
    namedWindow("org",1);
    while(cap.isOpened()){
	Mat bgr;
	cap >> img;
	imshow("org",img);
	if(waitKey(30) >= 0) break;
	
	//draw lines and put text according to the state of the execution
	drawlines(img ,  state);

	
    }
    return 0;
}

void(
