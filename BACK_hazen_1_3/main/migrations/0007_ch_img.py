# Generated by Django 4.2 on 2023-04-24 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_likediscomm_is_dis_alter_likediscomm_is_like_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ch',
            name='img',
            field=models.TextField(blank=True, null=True),
        ),
    ]
