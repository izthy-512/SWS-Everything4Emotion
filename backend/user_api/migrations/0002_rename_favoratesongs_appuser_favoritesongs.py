# Generated by Django 4.2.3 on 2023-07-17 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user_api", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="appuser",
            old_name="FavorateSongs",
            new_name="FavoriteSongs",
        ),
    ]
