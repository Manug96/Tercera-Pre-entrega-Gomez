# Generated by Django 5.0.6 on 2024-08-04 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcoder', '0003_rename_estudiante_historia_rename_curso_productos_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]