# Generated by Django 4.0.4 on 2022-06-09 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_user_shopname'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='shopname',
            field=models.CharField(max_length=254, null=True),
        ),
    ]