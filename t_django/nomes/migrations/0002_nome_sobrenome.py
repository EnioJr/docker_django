# Generated by Django 2.2.14 on 2020-07-30 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nomes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nome',
            name='sobrenome',
            field=models.CharField(default='ninguem', max_length=100),
            preserve_default=False,
        ),
    ]