# Generated by Django 5.1.3 on 2024-11-24 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0002_alter_customuser_is_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='firstName',
            new_name='fullNames',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='lastName',
        ),
    ]
