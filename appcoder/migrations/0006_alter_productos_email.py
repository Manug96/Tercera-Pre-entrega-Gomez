# Generated by Django 5.0.6 on 2024-08-04 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcoder', '0005_alter_productos_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
