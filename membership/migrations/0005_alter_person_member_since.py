# Generated by Django 3.2.2 on 2021-06-17 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0004_remove_person_keyfob_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='member_since',
            field=models.DateField(blank=True, null=True, verbose_name='Date Joined'),
        ),
    ]