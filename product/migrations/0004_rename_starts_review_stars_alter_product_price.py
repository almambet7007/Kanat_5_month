# Generated by Django 4.2.5 on 2023-10-09 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_review_starts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='starts',
            new_name='stars',
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(),
        ),
    ]
