# Generated by Django 4.0.4 on 2022-06-09 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='shopname',
            field=models.CharField(default=None, max_length=254),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
    ]