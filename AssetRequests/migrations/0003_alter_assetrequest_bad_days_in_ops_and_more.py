# Generated by Django 4.0.3 on 2022-12-12 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AssetRequests', '0002_userprofile_delete_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetrequest',
            name='bad_days_in_ops',
            field=models.CharField(max_length=10, verbose_name='Days/Weeks/Months in Operations'),
        ),
        migrations.AlterField(
            model_name='assetrequest',
            name='bad_equipment_name',
            field=models.CharField(max_length=50, verbose_name='Equipment Name'),
        ),
        migrations.AlterField(
            model_name='assetrequest',
            name='bad_equipment_rating',
            field=models.CharField(max_length=10, verbose_name='Equipment Rating'),
        ),
        migrations.AlterField(
            model_name='assetrequest',
            name='bad_installation_date',
            field=models.DateField(verbose_name='Installed Date'),
        ),
        migrations.AlterField(
            model_name='assetrequest',
            name='bad_last_service',
            field=models.DateField(verbose_name='Last Serviced Date'),
        ),
        migrations.AlterField(
            model_name='assetrequest',
            name='bad_model_number',
            field=models.CharField(max_length=20, verbose_name='Model Number'),
        ),
        migrations.AlterField(
            model_name='assetrequest',
            name='bad_serial_number',
            field=models.CharField(max_length=20, verbose_name='Serial Number'),
        ),
        migrations.AlterField(
            model_name='assetrequest',
            name='expected_date',
            field=models.DateField(verbose_name='Expected Delivery Date'),
        ),
        migrations.AlterField(
            model_name='assetrequest',
            name='hod_comment',
            field=models.CharField(max_length=500, verbose_name='HOD/CTO Comment'),
        ),
        migrations.AlterField(
            model_name='assetrequest',
            name='new_equipment_name',
            field=models.CharField(max_length=100, verbose_name='Equipment Name'),
        ),
        migrations.AlterField(
            model_name='assetrequest',
            name='new_equipment_rating',
            field=models.CharField(max_length=10, verbose_name='Rating'),
        ),
        migrations.AlterField(
            model_name='assetrequest',
            name='new_manufacturer',
            field=models.CharField(max_length=50, verbose_name='Manufacturer'),
        ),
        migrations.AlterField(
            model_name='assetrequest',
            name='sitemanager_comment',
            field=models.CharField(max_length=500, verbose_name='Site Manager Comment'),
        ),
    ]