# Generated by Django 3.2.4 on 2021-06-05 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0002_scores'),
    ]

    operations = [
        migrations.AddField(
            model_name='pictures',
            name='uploaded_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
