# Generated by Django 3.2 on 2021-04-16 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Regi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=70)),
                ('Last_name', models.CharField(max_length=70)),
                ('Email_Id', models.EmailField(max_length=70)),
                ('Phone_Number', models.IntegerField()),
                ('username', models.CharField(max_length=70)),
                ('password', models.CharField(max_length=70)),
            ],
            options={
                'db_table': 'Regi',
            },
        ),
        migrations.DeleteModel(
            name='Reg',
        ),
    ]
