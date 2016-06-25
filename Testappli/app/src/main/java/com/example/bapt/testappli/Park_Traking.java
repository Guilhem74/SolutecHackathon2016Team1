package com.example.bapt.testappli;

import android.os.Bundle;
import android.support.v4.app.FragmentActivity;
import android.support.v7.app.ActionBar;

import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.model.BitmapDescriptorFactory;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.MarkerOptions;


public class Park_Traking extends FragmentActivity implements OnMapReadyCallback {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_park__traking);
        SupportMapFragment mapFragment = (SupportMapFragment) getSupportFragmentManager()
                .findFragmentById(R.id.map);
        mapFragment.getMapAsync(this);
    }

    @Override
    public void onMapReady(GoogleMap map) {
        LatLng Solutec = new LatLng(45.746149, 4.834771);
        map.addMarker(new MarkerOptions().position(Solutec).alpha(0.0f));
        map.moveCamera(CameraUpdateFactory.newLatLng(Solutec));


        //Ini des cam
        int Nombre_Camera;
        Nombre_Camera = 3;

        int Tab_Voiture_Camera[]= new int[Nombre_Camera];
        Tab_Voiture_Camera[0]=5;
        Tab_Voiture_Camera[1]=3;
        Tab_Voiture_Camera[2]=5;

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
        Couleur_place_libre = BitmapDescriptorFactory.HUE_RED;
        for(i=0;i<Nombre_Camera;i++)
        {
            Coord_Cam[i]=new LatLng(Tab_Coord_Lat_Camera[i],Tab_Coord_Lng_Camera[i]);

            if(Tab_Voiture_Camera[i]>0)
                Couleur_place_libre = BitmapDescriptorFactory.HUE_ORANGE;
            if(Tab_Voiture_Camera[i]>3)
                Couleur_place_libre = BitmapDescriptorFactory.HUE_GREEN;

            map.addMarker(new MarkerOptions().position(Coord_Cam[i]).icon(BitmapDescriptorFactory.defaultMarker(Couleur_place_libre)));
        }


    }

}