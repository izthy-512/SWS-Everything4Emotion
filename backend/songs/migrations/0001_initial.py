# Generated by Django 4.2.3 on 2023-07-12 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Queries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.DateField(blank=True)),
                ('singer', models.CharField(max_length=100)),
                ('mood', models.CharField(choices=[('happy', 'happy'), ('confused', 'confused'), ('proud', 'proud'), ('relaxed', 'relaxed'), ('unamused', 'unameused')], default='happy', max_length=20)),
                ('text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('period', models.DateField(blank=True)),
                ('singer', models.CharField(max_length=100)),
                ('style', models.CharField(choices=[('None', 'None'), ('pop', 'pop'), ('rock', 'rock'), ('hiphop', 'hip hop'), ('jazz', 'jazz'), ('country', 'country'), ('electronic', 'electronic'), ('classical', 'classical')], default='None', max_length=20)),
                ('mood', models.CharField(choices=[('happy', 'happy'), ('confused', 'confused'), ('proud', 'proud'), ('relaxed', 'relaxed'), ('unamused', 'unameused')], default='happy', max_length=20)),
            ],
        ),
    ]
