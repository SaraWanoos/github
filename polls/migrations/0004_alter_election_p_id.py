# Generated by Django 4.0.2 on 2022-06-03 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_candidates_prog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='election',
            name='P_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.people', unique=True),
        ),
    ]
