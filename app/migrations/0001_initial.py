# Generated by Django 3.1.12 on 2023-03-10 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_idCliente', models.IntegerField()),
                ('_id', models.IntegerField()),
                ('total', models.FloatField()),
                ('date', models.DateTimeField()),
                ('user', models.CharField(max_length=100)),
                ('products', models.IntegerField()),
            ],
        ),
    ]