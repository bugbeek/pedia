# Generated by Django 3.0.5 on 2021-02-28 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_person_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=56, null=True),
        ),
    ]