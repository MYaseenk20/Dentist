# Generated by Django 3.0.3 on 2020-07-24 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_appointment_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]