# Generated by Django 2.1.4 on 2019-01-02 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190101_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='poi',
            name='address',
            field=models.CharField(blank=True, max_length=512, null=True, verbose_name='Address'),
        ),
    ]
