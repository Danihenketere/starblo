# Generated by Django 5.0.1 on 2024-02-04 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0015_post_img1b_post_post_img1s_post_post_img2b_post_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='advert',
            field=models.TextField(default='This is just a placw holder'),
            preserve_default=False,
        ),
    ]
