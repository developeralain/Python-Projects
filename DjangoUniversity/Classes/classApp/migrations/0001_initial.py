# Generated by Django 4.0.1 on 2022-01-12 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='djangoClasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Course_Number', models.IntegerField()),
                ('Instructor_Name', models.CharField(max_length=255)),
                ('Duration', models.FloatField()),
            ],
        ),
    ]