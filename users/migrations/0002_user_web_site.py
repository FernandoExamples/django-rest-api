# Generated by Django 4.0.5 on 2022-06-02 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='web_site',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
