# Generated by Django 3.1 on 2020-08-21 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='solution_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
