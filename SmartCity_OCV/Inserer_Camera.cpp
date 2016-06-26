




#include <opencv2/opencv.hpp>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <assert.h>
//sudo apt-get install libmysqlcppconn-dev
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

    sql::Driver *driver;
     sql::Connection *con;
     sql::Statement *stmt;
     sql::ResultSet *res;

     /* Create a connection */
     driver = get_driver_instance();
     con = driver->connect("localhost", "root", "azzaro");
     /* Connect to the MySQL test database */
     con->setSchema("Carte_Cam");

     stmt = con->createStatement();
    int latitude=0;
    printf("Entrer une latitude\n:");
    scanf("%d",&latitude);
    int longitude=0;
    printf("Entrer une longitude\n:");
    scanf("%d",&longitude);

     char Envoie_requete[1000]={};

    sprintf(Envoie_requete,"INSERT INTO Camera(Numero,Latitude,Longitude,Nbr_places_MAX,Nbr_places_DISPO,Utilisable) VALUES(NULL,%d,%d,0,0,1)",latitude,longitude);

    stmt->execute(Envoie_requete);

      delete stmt;
      delete con;


}
