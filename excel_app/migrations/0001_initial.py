# Generated by Django 5.0.1 on 2024-01-07 13:45

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
                ('group', models.CharField(blank=True, max_length=12, null=True)),
                ('cust_code', models.CharField(blank=True, max_length=25, null=True)),
                ('product_name', models.CharField(blank=True, max_length=50, null=True)),
                ('product_feature', models.CharField(blank=True, choices=[('NA', 'NA'), ('NONE', 'NONE'), ('FULL', 'FULL'), ('HALF', 'HALF'), ('OPEN', 'OPEN'), ('CLOSE', 'CLOSE')], max_length=50, null=True)),
                ('rate_basis', models.CharField(blank=True, max_length=12, null=True)),
                ('multiplying_factor', models.CharField(blank=True, max_length=6, null=True)),
                ('rate', models.CharField(blank=True, max_length=50, null=True)),
                ('len_from', models.FloatField(blank=True, null=True)),
                ('len_upto', models.FloatField(blank=True, null=True)),
                ('w_from', models.FloatField(blank=True, null=True)),
                ('w_upto', models.FloatField(blank=True, null=True)),
                ('th_from', models.FloatField(blank=True, null=True)),
                ('th_upto', models.FloatField(blank=True, null=True)),
                ('valid_from', models.DateField(blank=True, null=True)),
                ('valid_upto', models.DateField(blank=True, null=True)),
                ('valid_yn', models.BooleanField(default=True)),
            ],
        ),
    ]