#include <stdio.h>

#include <stdlib.h>

#include <opencv/highgui.h>


int main (int argc, char* argv[])

{

  IplImage* img = NULL;

  const char* window_title = "Hello, OpenCV!";


  if (argc < 2)

  {

    fprintf (stderr, "usage: %s IMAGE\n", argv[0]);

    return EXIT_FAILURE;

  }

  img = cvLoadImage(argv[1], CV_LOAD_IMAGE_UNCHANGED);


  if (img == NULL)

  {

    fprintf (stderr, "couldn't open image file: %s\n", argv[1]);

    return EXIT_FAILURE;

  }

  cvNamedWindow (window_title, CV_WINDOW_AUTOSIZE);

  cvShowImage (window_title, img);

  cvWaitKey(0);

  cvDestroyAllWindows();

  cvReleaseImage(&img);


  return EXIT_SUCCESS;

}
