# Generated by Django 3.0.3 on 2020-07-25 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_appointment_doctor_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='reviews',
            new_name='message',
        ),
    ]
