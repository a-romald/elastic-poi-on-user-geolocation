# Generated by Django 2.1.4 on 2019-01-01 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='Title')),
                ('area', models.CharField(blank=True, max_length=255, null=True, verbose_name='Area')),
                ('poi_type', models.CharField(blank=True, max_length=255, verbose_name='Type of poi')),
                ('lat', models.DecimalField(decimal_places=6, max_digits=10, null=True, verbose_name='Latitide')),
                ('lng', models.DecimalField(decimal_places=6, max_digits=10, null=True, verbose_name='Longitude')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='Add datetime')),
            ],
            options={
                'verbose_name': 'Точка',
                'verbose_name_plural': 'Точки',
                'ordering': ['title'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='poi',
            unique_together={('lat', 'lng')},
        ),
    ]
