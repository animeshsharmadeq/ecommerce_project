# Generated by Django 4.0.4 on 2022-06-13 13:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_user_rejection_reason'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('shop', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('product_name', models.CharField(blank=True, max_length=254, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('brand', models.CharField(blank=True, max_length=254, null=True)),
                ('material', models.CharField(blank=True, max_length=254, null=True)),
                ('category', models.CharField(blank=True, max_length=254, null=True)),
                ('is_published', models.BooleanField(default=False)),
            ],
        ),
    ]
