# Generated by Django 4.0.4 on 2022-11-22 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0050_remove_stock_itemcreation_company_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pancin',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.companies'),
        ),
    ]
