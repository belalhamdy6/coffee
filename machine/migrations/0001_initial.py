# Generated by Django 3.0.5 on 2020-09-17 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoffeFlaver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coffe_flaver_name_en', models.CharField(max_length=200)),
                ('coffe_flaver_name_ar', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PackSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pack_size_value', models.IntegerField()),
                ('pack_size_name_en', models.CharField(max_length=200)),
                ('pack_size_name_ar', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_type_name_en', models.CharField(max_length=200)),
                ('product_type_name_ar', models.CharField(max_length=200)),
                ('product_type_enum', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CoffePods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coffe_pods_name_en', models.CharField(max_length=200)),
                ('coffe_pods_name_ar', models.CharField(max_length=200)),
                ('coffe_flaver_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='machine.CoffeFlaver')),
                ('pack_size_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='machine.PackSize')),
                ('product_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='machine.ProductType')),
            ],
        ),
        migrations.CreateModel(
            name='CoffeMachine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('water_line', models.BooleanField()),
                ('coffe_machine_name_en', models.CharField(max_length=200)),
                ('coffe_machine_name_ar', models.CharField(max_length=200)),
                ('product_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='machine.ProductType')),
            ],
        ),
    ]
