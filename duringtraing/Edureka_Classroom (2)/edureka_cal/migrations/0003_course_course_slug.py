# Generated by Django 3.1.2 on 2020-10-11 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edureka_cal', '0002_course_end_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
