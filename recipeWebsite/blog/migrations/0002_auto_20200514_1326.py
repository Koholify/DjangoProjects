# Generated by Django 3.0.6 on 2020-05-14 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='topic',
        ),
        migrations.AlterField(
            model_name='instruction',
            name='instruction_step',
            field=models.CharField(max_length=1000),
        ),
    ]
