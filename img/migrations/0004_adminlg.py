# Generated by Django 4.1.6 on 2024-01-06 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('img', '0003_alter_pr_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='adminlg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='Unknown', max_length=100)),
                ('password', models.CharField(default='Unknown', max_length=100)),
            ],
        ),
    ]