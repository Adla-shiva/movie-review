# Generated by Django 4.1.6 on 2024-01-05 19:50

from django.db import migrations, models
import img.models


class Migration(migrations.Migration):

    dependencies = [
        ('img', '0002_remove_pr_img_remove_pr_name_pr_date_pr_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pr',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=img.models.filepath),
        ),
    ]
