# Generated by Django 2.2 on 2019-05-10 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sponsorship', '0004_auto_20190502_0351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsorship',
            name='relation',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='users.Relation'),
        ),
    ]