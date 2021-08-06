package com.utec.jmujica.proyectofinal;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.EditText;

import android.os.Bundle;
import android.view.View;
import android.widget.Toast;
import android.widget.Button;

public class Register extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_register);
    }

    public void submitRegister(View view){

        EditText user_name = findViewById(R.id.name_edit_id);
        EditText password_match = findViewById(R.id.password_edit_id);
        EditText password_rematch = findViewById(R.id.password_match_id);
        EditText email_text = findViewById(R.id.email_id);

        if(user_name.getText().toString().length() ==  0 ||
            password_match.getText().toString().length() ==  0 ||
            password_rematch.getText().toString().length() ==  0 ||
            email_text.getText().toString().length() ==  0) {

            Toast.makeText(this, getString(R.string.empty_fields), Toast.LENGTH_LONG).show();

        } else {
            passwordValidation(password_match, password_rematch);
            emailVerification(email_text);
        }

    }

    public void emailVerification(EditText email_text){

        if(!android.util.Patterns.EMAIL_ADDRESS.matcher(email_text.getText().toString()).matches()) {
            Toast.makeText(this, getString(R.string.toast_email), Toast.LENGTH_LONG).show();
        }
    }

    public void passwordValidation(EditText password_match, EditText password_rematch){

        if(!password_match.getText().toString().equals(password_rematch.getText().toString())) {
            Toast.makeText(this, getString(R.string.toast_password), Toast.LENGTH_LONG).show();
        }
    }
}
