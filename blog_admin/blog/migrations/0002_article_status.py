# Generated by Django 3.1.2 on 2020-10-18 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('1', 'Active'), ('0', 'Inactive')], default='0', max_length=1),
        ),
    ]
