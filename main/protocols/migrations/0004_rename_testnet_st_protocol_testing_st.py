# Generated by Django 4.0.5 on 2022-06-26 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('protocols', '0003_alter_protocol_active_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='protocol',
            old_name='testnet_st',
            new_name='testing_st',
        ),
    ]