# Generated by Django 4.0.5 on 2022-08-09 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Ticketing", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="ticket",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="Ticketing.ticket"
            ),
        ),
        migrations.AddConstraint(
            model_name="ticket",
            constraint=models.UniqueConstraint(
                fields=("title", "description", "user", "image", "time_created"),
                name="unique Ticketing",
            ),
        ),
    ]
