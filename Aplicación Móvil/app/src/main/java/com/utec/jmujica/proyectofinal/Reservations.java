package com.utec.jmujica.proyectofinal;

import androidx.appcompat.app.AppCompatActivity;

import java.util.Calendar;
import java.util.Date;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.DatePicker;
import android.widget.TimePicker;
import android.widget.EditText;
import android.widget.NumberPicker;
import android.widget.Toast;

public class Reservations extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_reservations);

        NumberPicker numberPicker = findViewById(R.id.number_picker_guests);

        numberPicker.setMinValue(1);
        numberPicker.setMaxValue(8);
        numberPicker.setValue(1);
    }

    public void submitReservation(View view) {


        DatePicker picked_date = findViewById(R.id.date_picker_id);

        int day = picked_date.getDayOfMonth();
        int month = picked_date.getMonth();
        int year =  picked_date.getYear();

        Calendar picked_calendar = Calendar.getInstance();
        picked_calendar.set(year, month, day);

        Date picked_time = picked_calendar.getTime();
        Date current_time = Calendar.getInstance().getTime();



        TimePicker clock = findViewById(R.id.time_picker_id);
        int hour = clock.getHour();



        EditText name_edit = findViewById(R.id.name_id);
        EditText phone_edit = findViewById(R.id.phone_id);
        //EditText mail_edit = findViewById(R.id.email_id);

        String name = name_edit.getText().toString();
        String phone = phone_edit.getText().toString();
        //String mail = mail_edit.getText().toString();

        Intent mail_intent = new Intent(Intent.ACTION_SENDTO);
        mail_intent.setData(Uri.parse("mailto:"));
        //mail_intent.putExtra(mail_intent.EXTRA_EMAIL, mail);
        mail_intent.putExtra(Intent.EXTRA_SUBJECT, getString(R.string.mail_subject) + name);
        mail_intent.putExtra(Intent.EXTRA_TEXT, getString(R.string.main_body_txt));


        if (name.length() == 0 ||
            phone.length() == 0) {
                Toast.makeText(this, getString(R.string.empty_fields), Toast.LENGTH_LONG).show();
        }else if(!android.util.Patterns.PHONE.matcher(phone).matches()) {
            Toast.makeText(this, getString(R.string.toast_phone), Toast.LENGTH_LONG).show();
        } else if(hour < 10 || hour > 20 ) {
            Toast.makeText(this, getString(R.string.is_closed_txt), Toast.LENGTH_LONG).show();
        } else if(current_time.after(picked_time)) {
            Toast.makeText(this, getString(R.string.past_date_txt), Toast.LENGTH_LONG).show();
        } else {
            Toast.makeText(this, getString(R.string.reservation_succes), Toast.LENGTH_LONG).show();

            /*
            if(mail_intent.resolveActivity(getPackageManager()) != null) {
                startActivity(mail_intent);
            }
            */
        }
    }

}
