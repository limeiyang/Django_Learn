# Generated by Django 2.1.7 on 2019-03-22 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190321_2019'),
    ]

    operations = [
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('pic', models.ImageField(blank=True, upload_to='pic', verbose_name='图片')),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='pic',
        ),
    ]
