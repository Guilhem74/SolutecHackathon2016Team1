#include <opencv2/opencv.hpp>
#include <iostream>
#include <stdio.h>

using namespace std;


int main(int argc, char** argv)
{

    cv::Mat src_img, gray_img, eq_img, result_img;

            src_img = cv::imread("Photos/Photo0.jpg", CV_LOAD_IMAGE_COLOR);
            if (src_img.data == NULL) {
                    printf("cv::imread() failed...\n");
                    return -1;
            }

            cv::cvtColor(src_img, gray_img, CV_RGB2GRAY);
            cv::equalizeHist(gray_img, eq_img);
            result_img = src_img.clone();

            cv::CascadeClassifier cascade;
            if (cascade.load("cas1.xml") == false) {
                    printf("cascade.load() failed...\n");
                    return -1;
            }

            std::vector<cv::Rect> faces;
            cascade.detectMultiScale(
                    eq_img,
                    faces,
                    1.1,          // scale factor
                    3,            // minimum neighbors
                    0,            // flags
                    cv::Size(100, 100) // minimum size
                    );

            std::vector<cv::Rect>::const_iterator i;
            int k=0;
            int x_min[100]={};
            int y_min[100]={};
            bool valide[100]={true};

            for (i = faces.begin(); i != faces.end(); ++i) {

                    x_min[k]=i->x;//i->x + i->width max
                    y_min[k]=i->y;
                k++;
            }
            int k_max=k;
            printf("%d\n",k_max);
            int j;
            i = faces.begin();
            for(k=0;k<k_max && i != faces.end();k++)
            {
                for(j=0;j<k_max&&valide[k]==true;j++)
                {
                    if( (x_min[k]>x_min[j]) && ((x_min[k]+ i->width)<(x_min[j]+ i->width)))//X contenu dans celui d'une autre case
                    {
                            valide[k]=false;

                    }

                }
                i++;
            }
            k=0;
            for (i = faces.begin(); i != faces.end(); ++i) {
                if(valide[k]==1||1)
                {
                cv::rectangle(
                        result_img,
                        cv::Point(i->x, i->y),
                        cv::Point(i->x + i->width, i->y + i->height),
                        CV_RGB(255, 0, 0),
                        2);
                }
                else
                {
                    printf("Imbriquation\n");
                }
                k++;
            }


            while(true) {
                    cv::imshow("result_img", result_img);
                    int c = cv::waitKey(0);
                    if (c == 27) break;
            }

}
