# Generated by Django 2.2 on 2019-05-10 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0004_expense_school'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='school.School'),
        ),
    ]
