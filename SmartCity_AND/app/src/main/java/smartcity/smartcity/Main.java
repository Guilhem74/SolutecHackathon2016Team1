package smartcity.smartcity;

import android.Manifest;
import android.content.Context;
import android.content.pm.PackageManager;
import android.graphics.drawable.Drawable;
import android.location.Location;
import android.location.LocationManager;
import android.support.v4.app.ActivityCompat;
import android.support.v4.content.ContextCompat;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
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
    private int INTERNET_PERMISSION = 3;


    @Override
    public void onLocationChanged(Location location) {
        LatLng latLng = new LatLng(location.getLatitude(), location.getLongitude());
        CameraUpdate cameraUpdate = CameraUpdateFactory.newLatLngZoom(latLng, 10);
        if (map != null)
            map.animateCamera(cameraUpdate);
        else {
            // ERRORRORROROR
        }
        try {
            locationManager.removeUpdates(this);
        }
        catch (SecurityException e) {
            // ERRORROROROR
        };
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


        if (ContextCompat.checkSelfPermission(this, Manifest.permission.INTERNET) != PackageManager.PERMISSION_GRANTED) {
            requestInternetPermission();
        }



        locationManager = (LocationManager) getSystemService(Context.LOCATION_SERVICE);


        int mapID = getResources().getIdentifier("mapView", "id", getPackageName());
        MapView mapView = (MapView)findViewById(mapID);


        mapView.getMapAsync(new OnMapReadyCallback() {

            @Override
            public void onMapReady(GoogleMap googleMap) {
                map = googleMap;

                LatLng lyon_coord = new LatLng(45.746149, 4.834771);
                map.addMarker(new MarkerOptions().position(lyon_coord).alpha(0.0f)); //transpa du marqueur
                map.moveCamera(CameraUpdateFactory.newLatLng(lyon_coord)); //Centre la camera sur la tour du web
                map.animateCamera(CameraUpdateFactory.newLatLngZoom(lyon_coord, 13.0f)); //zoom sur lyon

                updateCamInfo();
            }
        });

    }

    void updateCamInfo() {
        CamData data = new CamData();
        CamInfo cam[] = data.getInfos();
        int i=0;
        while (cam[i] != null) {
            float color = BitmapDescriptorFactory.HUE_RED;
            if (cam[i].Nbr_places_DISPO > 0)
                color = BitmapDescriptorFactory.HUE_ORANGE;
            if (cam[i].Nbr_places_DISPO > 3)
                color = BitmapDescriptorFactory.HUE_GREEN;
            addMarker(cam[i].Latitude, cam[i].Longitude, cam[i].id, cam[i].Nbr_places_DISPO, color);
            i++;
        }

    }

    public void addMarker(double lat, double lng, int cam_nbr, int pl_libres, float color) {
        if (map == null) {
            // ERREUR A GERRER
            return;
        }
        String pl_str = String.format("%d place(s) libre(s)", pl_libres);
        String nb_cam = String.format("Caméra %d", cam_nbr);
        LatLng pos = new LatLng(lat, lng);
        map.addMarker(new MarkerOptions().title(pl_str).snippet(nb_cam).position(pos).icon(BitmapDescriptorFactory.defaultMarker(color)));

    }


    public void onSearchButtonClick(View v) {
        if (ContextCompat.checkSelfPermission(this, Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED) {
            requestLocationPermission();
        }
        locationManager.requestLocationUpdates(LocationManager.GPS_PROVIDER, MIN_TIME, MIN_DISTANCE, this);
    }



    public void setupTab() {
        TabHost host = (TabHost)findViewById(R.id.tabHost);
        host.setup();


        TabHost.TabSpec spec = host.newTabSpec("Favoris");
        spec.setContent(R.id.tab1);
        spec.setIndicator("",getResources().getDrawable(R.drawable.a));
        host.addTab(spec);


        spec = host.newTabSpec("Favoris");
        spec.setContent(R.id.tab2);
        spec.setIndicator("",getResources().getDrawable(R.drawable.b));
        host.addTab(spec);


        spec = host.newTabSpec("FAQ");
        spec.setContent(R.id.tab3);
        spec.setIndicator("",getResources().getDrawable(R.drawable.c));
        host.addTab(spec);
    }


    public void requestInternetPermission() {
        if (ActivityCompat.shouldShowRequestPermissionRationale(this, Manifest.permission.INTERNET) == false) {
            ActivityCompat.requestPermissions(this, new String[]{Manifest.permission.INTERNET}, INTERNET_PERMISSION);
        }
    }

    public void requestLocationPermission() {
        if (ActivityCompat.shouldShowRequestPermissionRationale(this, Manifest.permission.ACCESS_FINE_LOCATION) == false) {
            ActivityCompat.requestPermissions(this, new String[]{Manifest.permission.ACCESS_FINE_LOCATION}, LOCATION_PERMISSION);
        }
    }

    @Override
    public void onRequestPermissionsResult(int requestCode, String[] permissions, int[] result){
        super.onRequestPermissionsResult(requestCode, permissions, result);

        if(requestCode == LOCATION_PERMISSION && result[0] == PackageManager.PERMISSION_GRANTED) {

            try {
                locationManager.requestLocationUpdates(LocationManager.GPS_PROVIDER, MIN_TIME, MIN_DISTANCE, this); //You can also use LocationManager.GPS_PROVIDER and LocationManager.PASSIVE_PROVIDER
            } catch (SecurityException e) {
                // ERRRORROROR
            }
        }
        else if (requestCode == INTERNET_PERMISSION && result[0] == PackageManager.PERMISSION_GRANTED) {

            // GERER QUAND L'USER REFUSE LA LOCALIS
        }
    }

}
