# Generated by Django 3.1.7 on 2021-02-26 11:03

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
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('partners', models.ForeignKey(default='User_is_deleted', on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('price', models.FloatField()),
                ('hours', models.IntegerField()),
                ('company', models.ForeignKey(default='Company_is_deleted', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='bookingsCollection', to='intraApp.company')),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('company_ID', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='intraApp.company')),
            ],
        ),
    ]
