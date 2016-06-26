#include <opencv2/opencv.hpp>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <assert.h>

#include <cppconn/driver.h>
#include <cppconn/exception.h>
#include <cppconn/resultset.h>
#include <cppconn/statement.h>
#include <mysql_connection.h>

using namespace std;
using namespace cv;
/* Doit etre fourni en second paramètre le nombre de caméra*/
int main(int argc, char** argv)
{

    assert(argc==2);
    int Nombre_Camera=atoi(argv[1]);
    int Nmbr_Voiture[Nombre_Camera]={};
    for(int l=0; l<Nombre_Camera;l++)
    {
        char Nom_fichier[20+Nombre_Camera/10]="Camera";
        sprintf(Nom_fichier,"Camera%d.avi",l+1);
        printf("%s\n",Nom_fichier);
        //Transformation Video to Jpg
        CvCapture* capture=0;
        IplImage* frame=0;

        capture = cvCaptureFromAVI(Nom_fichier); // Lit AVI video
        if( !capture )
            throw "Error when reading steam_avi";

        /*On ne recupere qu'une frame*/
        frame = cvQueryFrame( capture );

        Mat Image_Solo = cvarrToMat(frame);
        /*On cherche a remplace .avi par .jpg*/

        Nom_fichier[strlen(Nom_fichier)-1]='g';
        Nom_fichier[strlen(Nom_fichier)-2]='p';
        Nom_fichier[strlen(Nom_fichier)-3]='j';

        /*On ecrit l'image*/
        imwrite( Nom_fichier,Image_Solo);
        //Nom_fichier.jpg existe alors

        /* Executionn du script python afin de modifier photo*/
        /*if(fork()==0)
    {//On est fils
        int retour=execlp("python","python","main_superposition_calque.py",Nom_fichier,NULL);//Disparition du fils avec le execlp
        printf("Execlp echoue\n");
        exit(-1);
    }
    //On est père
    wait(Null);//attente fin du fils*/


        //Traitement du nombre de Voiture
        Mat Image_Source, gray_img, eq_img, result_img;
        //on vient stocker la matrice sour la forme d'une matrice
        Image_Source = imread(Nom_fichier, CV_LOAD_IMAGE_COLOR);
        if (Image_Source.data == NULL) {
            printf("imread() failed...\n");
            return -1;
        }
        //On converti l'image en niveau de Gris vvv
        cvtColor(Image_Source, gray_img, CV_RGB2GRAY);
        equalizeHist(gray_img, eq_img);//lissage , Utilité a verifier
        result_img = Image_Source.clone();

        CascadeClassifier cascade;
        if (cascade.load("cas1.xml") == false) {//Fichier .xml comprenant nos voitures cataloguées
            printf("cascade.load() failed...\n");
            return -1;
        }

        vector<Rect> faces;
        cascade.detectMultiScale(//la formule magique pour detecter nos voitures
                                 eq_img,//image lissée en niveau de gris
                                 faces,//vecteur
                                 1.1,          // Facteur d'echelle
                                 4,            // minimum neighbors
                                 0,            // flags
                                 Size(100, 100) // Taille minimum d'un carré pour la detection
                                 );

        vector<Rect>::const_iterator i;
        int Nbr_Vehicules=0;
        for (i = faces.begin(); i != faces.end(); ++i)
        {

            rectangle(
                        result_img,
                        Point(i->x, i->y),
                        Point(i->x + i->width, i->y + i->height),
                        CV_RGB(255, 0, 0),
                        2);
            Nbr_Vehicules++;

        }
        Nmbr_Voiture[l]=Nbr_Vehicules;
        //Nbr_Vehicules représentent le nombres de vehicules présent sur la photo
// imshow("result_img", result_img);
        //TODO: Comm base de données
    }
/*
    sql::Driver *driver;
     sql::Connection *con;
     sql::Statement *stmt;
     sql::ResultSet *res;

     /* Create a connection */
  /*   driver = get_driver_instance();
     con = driver->connect("tcp://127.0.0.1:3306", "root", "root");
     /* Connect to the MySQL test database */
  /*   con->setSchema("test");
*/

}
