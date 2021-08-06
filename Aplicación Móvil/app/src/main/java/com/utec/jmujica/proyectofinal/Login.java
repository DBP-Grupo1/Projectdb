package com.utec.jmujica.proyectofinal;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

public class Login extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);
    }

    public void submitLogin(View view) {
        EditText user_name = findViewById(R.id.name_edit_id);
        EditText password = findViewById(R.id.password_edit_id);

        if (user_name.getText().toString().length() == 0 ||
            password.getText().toString().length() == 0) {
                Toast.makeText(this, getString(R.string.empty_fields), Toast.LENGTH_LONG).show();
        } else {
            redirectReservations();
        }
    }

    public void redirectReservations(){
        Intent intent = new Intent(this, Reservations.class);
        startActivity(intent);
    }
}
