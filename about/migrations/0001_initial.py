# Generated by Django 4.1.7 on 2023-06-11 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vision', models.TextField()),
                ('mission', models.TextField()),
                ('image', models.ImageField(upload_to='about/')),
            ],
        ),
    ]
