# Generated by Django 4.1.6 on 2023-02-07 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0004_rename_acctransactions_accounttransactions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ouruser',
            name='f_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='ouruser',
            name='l_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='ouruser',
            name='user_id',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]