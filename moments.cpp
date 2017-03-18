#include "opencv2/imgcodecs.hpp"
#include "opencv2/highgui.hpp"
#include "opencv2/imgproc.hpp"
#include <iostream>
using namespace cv;
using namespace std;

RNG rng(12345);

void moments(Mat& src )
{
    Mat temp1,temp2;
    GaussianBlur(src, temp1, Size(5,5),0,0);
    GaussianBlur(src, temp1, Size(5,5),0,0);
    GaussianBlur(src, temp1, Size(5,5),0,0);
    threshold(temp1,temp2 ,0,255,3 );
   
    GaussianBlur(src, temp2, Size(5,5),0,0);
    GaussianBlur(src, temp2, Size(5,5),0,0);
    GaussianBlur(src, temp2, Size(5,5),0,0);
    threshold(temp2,temp1 ,0,255,3 );
 
    GaussianBlur(src, temp1, Size(5,5),0,0);
    GaussianBlur(src, temp1, Size(5,5),0,0);
    GaussianBlur(src, temp1, Size(5,5),0,0);
    threshold(temp1,temp2 ,0,255,3 );
    
    imshow("temp",temp2);
 
    
  vector<vector<Point> > contours;
  vector<Vec4i> hierarchy;
  findContours(temp2 , contours, hierarchy, RETR_TREE, CHAIN_APPROX_SIMPLE, Point(0, 0) );
  vector<Moments> mu(contours.size() );
    Moments m;
    double area=0.0;
  for( size_t i = 0; i < contours.size(); i++ )
     { mu[i] = moments( contours[i], false );
	if(contourArea(contours[i])>area){
	    area=contourArea(contours[i]);
	    m=mu[i];
	}
     }
  vector<Point2f> mc( contours.size() );
    Point2f max_area_cnt;
    max_area_cnt=Point2f(static_cast<float>(m.m10/m.m00,static_cast<float>(m.m01/m.m00)));
  for( size_t i = 0; i < contours.size(); i++ )
     { mc[i] = Point2f( static_cast<float>(mu[i].m10/mu[i].m00) , static_cast<float>(mu[i].m01/mu[i].m00) ); }
  Mat drawing = Mat::zeros( src.size(), CV_8UC3 );
  
    for( size_t i = 0; i< contours.size(); i++ )
     {
       Scalar color = Scalar( rng.uniform(0, 255), rng.uniform(0,255), rng.uniform(0,255) );
       //drawContours( drawing, contours, (int)i, color, 2, 8, hierarchy, 0, Point() );
       //circle( drawing, mc[0], 4, color, -1, 8, 0 );
     }
  namedWindow( "Contours", WINDOW_AUTOSIZE );
  imshow( "Contours", drawing );
  printf("\t Info: Area and Contour Length \n");
  for( size_t i = 0; i< contours.size(); i++ )
     {
       printf(" * Contour[%d] - Area (M_00) = %.2f - Area OpenCV: %.2f - Length: %.2f \n", (int)i, mu[i].m00, contourArea(contours[i]), arcLength( contours[i], true ) );
       Scalar color = Scalar( rng.uniform(0, 255), rng.uniform(0,255), rng.uniform(0,255) );
       //drawContours( drawing, contours, (int)i, color, 2, 8, hierarchy, 0, Point() );
       //circle( drawing, mc[i], 4, color, -1, 8, 0 );
     }
       Scalar color = Scalar( rng.uniform(0, 255), rng.uniform(0,255), rng.uniform(0,255) );
    circle (drawing,max_area_cnt,4,color,-1,8,0);
    cout<<max_area_cnt<<endl;
}
