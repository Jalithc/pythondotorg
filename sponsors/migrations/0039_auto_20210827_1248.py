# Generated by Django 2.0.13 on 2021-08-27 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0038_auto_20210827_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsorship',
            name='level_name',
            field=models.CharField(blank=True, default='', help_text='DEPRECATED: will be removed after manual data sanity check.', max_length=64),
        ),
    ]