# Generated by Django 3.0 on 2019-12-09 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='household',
            name='external_customer_identifier',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='household',
            name='external_subscription_identifier',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
