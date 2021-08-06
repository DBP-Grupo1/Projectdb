package com.utec.jmujica.proyectofinal;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;

import android.view.View;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;
import android.widget.Button;
import android.content.Intent;

public class MainActivity extends AppCompatActivity {


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button login_button = findViewById(R.id.login_button_id);
        login_button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                redirectLogin();
            }
        });

        Button register_button = findViewById(R.id.register_button_id);
        register_button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                redirectRegister();
            }
        });
    }

    public void redirectLogin(){
        Intent intent = new Intent(this, Login.class);
        startActivity(intent);
    }

    public void redirectRegister(){
        Intent intent = new Intent(this, Register.class);
        startActivity(intent);
    }

}
