# Generated by Django 2.2.4 on 2019-08-27 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20190827_1359'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Makaleye Fotoğraf Ekleyin'),
        ),
    ]
