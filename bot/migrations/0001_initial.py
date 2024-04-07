# Generated by Django 4.2.11 on 2024-04-07 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=200)),
                ('resolution', models.IntegerField()),
                ('scale', models.FloatField()),
                ('voxel_size', models.FloatField()),
            ],
        ),
    ]