# Generated by Django 4.0.2 on 2022-06-03 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_alter_election_p_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='election',
            name='P_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='polls.people'),
        ),
    ]
