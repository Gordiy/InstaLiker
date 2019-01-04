# Generated by Django 2.0 on 2018-12-31 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.TextField()),
                ('password', models.TextField()),
            ],
            options={
                'verbose_name': 'User data',
                'verbose_name_plural': "User's data",
            },
        ),
    ]
