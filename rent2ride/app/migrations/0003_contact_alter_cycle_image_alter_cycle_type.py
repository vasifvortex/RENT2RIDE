# Generated by Django 4.2.13 on 2024-06-18 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_cycle_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=150)),
                ('email', models.CharField(default='', max_length=150)),
                ('phone_number', models.CharField(default='', max_length=15)),
                ('message', models.TextField(default='', max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='cycle',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='bike_images/'),
        ),
        migrations.AlterField(
            model_name='cycle',
            name='type',
            field=models.CharField(max_length=50),
        ),
    ]