# Generated by Django 2.2 on 2019-05-10 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0008_auto_20190510_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='school',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='school.School'),
        ),
    ]
