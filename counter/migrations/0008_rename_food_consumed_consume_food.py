# Generated by Django 4.2.6 on 2023-12-03 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0007_alter_consume_food_consumed_alter_consume_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consume',
            old_name='food_consumed',
            new_name='food',
        ),
    ]