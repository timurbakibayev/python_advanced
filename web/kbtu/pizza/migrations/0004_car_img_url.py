# Generated by Django 3.1.2 on 2020-12-08 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0003_auto_20201103_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='img_url',
            field=models.CharField(default='https://www.extremetech.com/wp-content/uploads/2019/12/SONATA-hero-option1-764A5360-edit.jpg', max_length=1000),
        ),
    ]
