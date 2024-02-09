# Generated by Django 5.0.1 on 2024-02-09 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_alter_user_firstname_alter_user_lastname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, default='12345 main', max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='address2',
            field=models.CharField(blank=True, default=' ', max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, default='Dallas', max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='state',
            field=models.CharField(blank=True, default='TX', max_length=128),
            preserve_default=False,
        ),
    ]
