# Generated by Django 3.2.8 on 2021-11-03 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0007_auto_20211103_1019'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('author', models.ManyToManyField(to='Product.Author')),
            ],
        ),
    ]