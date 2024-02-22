# Generated by Django 5.0.1 on 2024-02-22 04:26

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('description', models.CharField(max_length=2000)),
                ('link', models.ImageField(upload_to='Views/media/images')),
                ('review', models.IntegerField(default=0)),
                ('ingredient', models.CharField(blank=True, default=' ', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('quantity', models.IntegerField(default=0)),
                ('paid', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Views.product')),
            ],
        ),
    ]
