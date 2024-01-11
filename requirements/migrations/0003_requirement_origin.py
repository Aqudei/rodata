# Generated by Django 5.0.1 on 2024-01-11 09:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_department_is_external'),
        ('requirements', '0002_compliance_submission_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='requirement',
            name='origin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.department'),
        ),
    ]
