# Generated by Django 3.0.1 on 2019-12-18 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20191218_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='personal_portfolio//static//img'),
        ),
    ]
