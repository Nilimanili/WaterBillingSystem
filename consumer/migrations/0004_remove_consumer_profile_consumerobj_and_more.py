# Generated by Django 4.1.7 on 2023-03-28 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0003_rename_consumer_consumer_profile_consumerobj'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consumer_profile',
            name='consumerobj',
        ),
        migrations.AddField(
            model_name='consumer_profile',
            name='consumer',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
