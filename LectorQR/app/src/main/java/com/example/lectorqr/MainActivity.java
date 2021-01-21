package com.example.lectorqr;

import android.content.Intent;
import android.net.Uri;
import android.webkit.WebView;
import android.os.Bundle;
import android.widget.TextView;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import com.google.zxing.integration.android.IntentIntegrator;
import com.google.zxing.integration.android.IntentResult;
import android.provider.Settings.Secure;



public class MainActivity  extends AppCompatActivity {



    TextView txt;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        txt = findViewById(R.id.txt);
        new IntentIntegrator(this).initiateScan();

    }

    public void irAweb(String url){
        /*Uri uri = Uri.parse(url);
        Intent intentNav = new Intent(Intent.ACTION_VIEW, uri);
        startActivity(intentNav);
    */
        WebView webview = new WebView(this);
        setContentView(webview);
        String postData = "";
        webview.postUrl(url, postData.getBytes());

    }


    @Override
    protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
        super.onActivityResult(requestCode, resultCode, data);

        IntentResult result = IntentIntegrator.parseActivityResult(requestCode,resultCode,data);

        String datos = result.getContents();
        String id = Secure.getString(this.getContentResolver(), Secure.ANDROID_ID);

        String url;
        url = datos +"&id_device="+ id + "&status=sano";
        irAweb(url);








    }
}
