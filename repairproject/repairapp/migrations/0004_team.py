# Generated by Django 3.2.13 on 2022-05-28 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repairapp', '0003_auto_20220527_1206'),
    ]

    operations = [
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('descr', models.TextField()),
                ('image', models.ImageField(upload_to='team')),
            ],
        ),
    ]
