# Generated by Django 2.2.12 on 2021-10-10 18:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Infra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('director', models.CharField(max_length=300)),
                ('cast', models.CharField(max_length=800)),
                ('description', models.TextField(max_length=5000)),
                ('release_date', models.DateField()),
                ('averageRating', models.FloatField(default=0)),
                ('image', models.URLField(default=None, null=True)),
                ('electricity', models.FloatField()),
                ('railways', models.TextField(max_length=1000)),
                ('bridges', models.FloatField()),
                ('tunnels', models.FloatField()),
                ('water_supply', models.CharField(max_length=1)),
                ('sewers', models.FloatField()),
                ('telecommunication', models.TextField(max_length=5000)),
                ('market', models.FloatField()),
                ('transportation', models.TextField(max_length=5000)),
                ('distributors', models.TextField(max_length=5000)),
                ('suppliers', models.TextField(max_length=5000)),
                ('mining_area', models.FloatField()),
                ('forest_area', models.FloatField()),
                ('ready_to_use_land', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=5000)),
                ('rating', models.FloatField(default=0)),
                ('Infra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Infra')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
