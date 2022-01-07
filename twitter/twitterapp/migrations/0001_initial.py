# Generated by Django 4.0 on 2022-01-05 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('joined_date', models.DateTimeField(verbose_name='Acc creation date')),
            ],
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=140)),
                ('date', models.DateTimeField(verbose_name='Tweet date')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='twitterapp.user')),
            ],
        ),
    ]
