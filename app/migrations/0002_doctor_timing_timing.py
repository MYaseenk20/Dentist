# Generated by Django 3.0.3 on 2020-07-24 13:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor_timing',
            name='timing',
            field=models.CharField(choices=[('10am to 1pm', '10am to 1pm'), ('1pm to 4pm', '1pm to 4pm'), ('4pm to 6pm', '4pm to 6pm')], default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
