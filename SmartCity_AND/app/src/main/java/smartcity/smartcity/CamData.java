package smartcity.smartcity;

/**
 * Created by nicolas on 26/06/16.
 */

import android.util.Log;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.InputStream;


public class CamData {
    // JDBC driver name and database URL
    static final String DB_URL = "http://192.168.101.25/bdd.php";

    InputStream is;


    public CamInfo[] getInfos() {

        CamInfo[] cam = new CamInfo[100];

        String result = null;
// L'année à envoyer

        CamDataRequest dr = new CamDataRequest();
        dr.execute(DB_URL);
        try {
            while (result == null)
                result = dr.get();
        } catch (Exception e) {
        }

// Parsing des données JSON
        try {
            JSONArray jArray = new JSONArray(result);
            for (int i = 0; i < jArray.length(); i++) {
                cam[i] = new CamInfo();
                JSONObject json_data = jArray.getJSONObject(i);


                int id = json_data.getInt("Numero");
                float Latitude = (float) json_data.getDouble("Latitude");
                float Longitude = (float) json_data.getDouble("Longitude");
                int Nbr_places_MAX = json_data.getInt("Nbr_places_MAX");
                int Nbr_places_DISPO = json_data.getInt("Nbr_places_DISPO");
                int Utilisable = json_data.getInt("Utilisable");


                cam[i].id = id;
                cam[i].Latitude = Latitude;
                cam[i].Longitude = Longitude;
                cam[i].Nbr_places_MAX = Nbr_places_MAX;
                cam[i].Nbr_places_DISPO = Nbr_places_DISPO;
                cam[i].Utilisable = Utilisable == 1 ? true : false;

            }
        } catch (JSONException e) {
            Log.e("log_tag", "Error parsing data " + e.toString());
        }


        return cam;
    }
}
