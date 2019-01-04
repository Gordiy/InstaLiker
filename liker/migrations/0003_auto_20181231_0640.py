# Generated by Django 2.0 on 2018-12-31 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liker', '0002_auto_20181231_0622'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialNetworks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=36, null=True)),
                ('link', models.CharField(blank=True, default=None, max_length=58, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Social Network',
                'verbose_name_plural': 'Social Networks',
            },
        ),
        migrations.AlterModelOptions(
            name='userdata',
            options={'verbose_name': 'Social Network', 'verbose_name_plural': 'Social Networks'},
        ),
    ]
