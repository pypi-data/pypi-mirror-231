# Generated by Django 3.2.10 on 2022-01-11 16:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pretalx_public_voting", "0003_migrate_settings"),
    ]

    operations = [
        migrations.AddField(
            model_name="publicvotingsettings",
            name="allowed_emails",
            field=models.TextField(null=True),
        ),
    ]
