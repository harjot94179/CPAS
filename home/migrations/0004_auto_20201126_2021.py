# Generated by Django 3.0.8 on 2020-11-26 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20201126_1147'),
    ]

    operations = [
        migrations.AddField(
            model_name='udata',
            name='email',
            field=models.CharField(default='Mail not provided', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='udata',
            name='name',
            field=models.CharField(default='Anonymous User', max_length=255),
            preserve_default=False,
        ),
    ]
