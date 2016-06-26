package smartcity.smartcity;

import android.Manifest;
import android.app.AlertDialog;
import android.content.Context;
import android.content.DialogInterface;
import android.content.pm.PackageManager;
import android.location.Location;
import android.location.LocationManager;
import android.os.Build;
import android.support.v4.app.ActivityCompat;
import android.support.v4.content.ContextCompat;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.widget.Toolbar;
import android.util.Printer;
import android.view.View;


import android.location.LocationListener;
import android.widget.TabHost;

import com.google.android.gms.maps.CameraUpdate;
import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.MapView;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.model.BitmapDescriptorFactory;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.MarkerOptions;


public class Main extends AppCompatActivity implements LocationListener {

    private LocationManager locationManager;
    private static final long MIN_TIME = 400;
    private static final float MIN_DISTANCE = 1000;

    private  GoogleMap map;

    private int LOCATION_PERMISSION = 2;

    public void setupTab() {
        TabHost host = (TabHost)findViewById(R.id.tabHost);
        host.setup();

        //Tab 1
        TabHost.TabSpec spec = host.newTabSpec("Favoris");
        spec.setContent(R.id.tab1);
        spec.setIndicator("Accueil");
        host.addTab(spec);

        //Tab 2
        spec = host.newTabSpec("Favoris");
        spec.setContent(R.id.tab2);
        spec.setIndicator("Favoris");
        host.addTab(spec);

        //Tab 3
        spec = host.newTabSpec("FAQ");
        spec.setContent(R.id.tab3);
        spec.setIndicator("FAQ");
        host.addTab(spec);
    }

    @Override
    public void onLocationChanged(Location location) {
        LatLng latLng = new LatLng(location.getLatitude(), location.getLongitude());
        CameraUpdate cameraUpdate = CameraUpdateFactory.newLatLngZoom(latLng, 10);
        if (map != null)
            map.animateCamera(cameraUpdate);
        else {
            // ERRORRORROROR
        }
        locationManager.removeUpdates(this);
    }

    @Override
    public void onStatusChanged(String provider, int status, Bundle extras) { }

    @Override
    public void onProviderEnabled(String provider) { }

    @Override
    public void onProviderDisabled(String provider) { }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        setupTab();
        locationManager = (LocationManager) getSystemService(Context.LOCATION_SERVICE);


        int mapID = getResources().getIdentifier("mapView", "id", getPackageName());
        MapView mapView = (MapView)findViewById(mapID);


        mapView.getMapAsync(new OnMapReadyCallback() {

            @Override
            public void onMapReady(GoogleMap googleMap) {
                map = googleMap;

                LatLng Solutec = new LatLng(45.746149, 4.834771);
                map.addMarker(new MarkerOptions().position(Solutec).alpha(0.0f)); //transpa du marqueur
                map.moveCamera(CameraUpdateFactory.newLatLng(Solutec)); //Centre la camera sur la tour du web
                map.animateCamera(CameraUpdateFactory.newLatLngZoom(Solutec, 13.0f)); //zoom sur lyon


                //Ini des cam

                int Nombre_Camera;
                Nombre_Camera = 3;

                int Tab_Num_Camera[] = new int[Nombre_Camera];
                Tab_Num_Camera[0]=1;
                Tab_Num_Camera[1]=2;
                Tab_Num_Camera[2]=3;

                int Tab_Voiture_Camera[]= new int[Nombre_Camera];
                Tab_Voiture_Camera[0]=0;
                Tab_Voiture_Camera[1]=2;
                Tab_Voiture_Camera[2]=4;

                double Tab_Coord_Lat_Camera[] = new double[Nombre_Camera];
                Tab_Coord_Lat_Camera[0]=45.747;
                Tab_Coord_Lat_Camera[1]=45.749;
                Tab_Coord_Lat_Camera[2]=45.751;


                double Tab_Coord_Lng_Camera[]= new double[Nombre_Camera];
                Tab_Coord_Lng_Camera[0]=4.834;
                Tab_Coord_Lng_Camera[1]=4.836;
                Tab_Coord_Lng_Camera[2]=4.838;

                LatLng Coord_Cam[]= new LatLng[Nombre_Camera];

                int i;
                i=Nombre_Camera;
                float Couleur_place_libre;
                String Aff_Marqueur_Nbr_place;
                String Aff_Marqueur_Num_Camera;

                //Crée les marqueurs de X cameras
                for(i=0;i<Nombre_Camera;i++) {
                    Coord_Cam[i] = new LatLng(Tab_Coord_Lat_Camera[i], Tab_Coord_Lng_Camera[i]);
                    Couleur_place_libre = BitmapDescriptorFactory.HUE_RED;
                    if (Tab_Voiture_Camera[i] > 0)
                        Couleur_place_libre = BitmapDescriptorFactory.HUE_ORANGE;
                    if (Tab_Voiture_Camera[i] > 3)
                        Couleur_place_libre = BitmapDescriptorFactory.HUE_GREEN;
                    Aff_Marqueur_Nbr_place = String.format("%d place(s) libre(s)", Tab_Voiture_Camera[i]);
                    Aff_Marqueur_Num_Camera = String.format("Camera %d", Tab_Num_Camera[i]);
                    map.addMarker(new MarkerOptions().title(Aff_Marqueur_Nbr_place)
                            .snippet(Aff_Marqueur_Num_Camera).position(Coord_Cam[i]).icon(BitmapDescriptorFactory.defaultMarker(Couleur_place_libre)));

                }

            }


        });



    }




    public void onSearchButtonClick(View v) {
        if (ContextCompat.checkSelfPermission(this, Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED) {
            requestLocationPermission();
        }
        locationManager.requestLocationUpdates(LocationManager.GPS_PROVIDER, MIN_TIME, MIN_DISTANCE, this);
    }



    public void requestLocationPermission() {
        if (ActivityCompat.shouldShowRequestPermissionRationale(this, Manifest.permission.ACCESS_FINE_LOCATION) == false) {
            ActivityCompat.requestPermissions(this, new String[]{Manifest.permission.ACCESS_FINE_LOCATION}, LOCATION_PERMISSION);
        }
    }

    @Override
    public void onRequestPermissionsResult(int requestCode, String[] permissions, int[] result){
        super.onRequestPermissionsResult(requestCode, permissions, result);

        if(requestCode == LOCATION_PERMISSION && result[0] == PackageManager.PERMISSION_GRANTED){

            locationManager.requestLocationUpdates(LocationManager.GPS_PROVIDER, MIN_TIME, MIN_DISTANCE, this); //You can also use LocationManager.GPS_PROVIDER and LocationManager.PASSIVE_PROVIDER
        }
        else {

            // GERER QUAND L'USER REFUSE LA LOCALIS
        }
    }

}
