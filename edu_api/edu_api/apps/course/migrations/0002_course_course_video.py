# Generated by Django 2.2.2 on 2020-09-30 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_video',
            field=models.FileField(blank=True, null=True, upload_to='video', verbose_name='视频'),
        ),
    ]
