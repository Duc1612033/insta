# Generated by Django 3.1 on 2024-11-13 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0004_alter_group_id_alter_membership_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
