# Generated by Django 4.0.2 on 2022-05-09 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_alter_candidates_fname_alter_candidates_lname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidates',
            name='Prog',
            field=models.TextField(default='Election program'),
        ),
    ]
