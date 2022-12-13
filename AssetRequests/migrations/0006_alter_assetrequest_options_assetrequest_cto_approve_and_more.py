# Generated by Django 4.0.3 on 2022-12-12 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AssetRequests', '0005_assetrequest'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='assetrequest',
            options={'ordering': ['-requestdate'], 'verbose_name_plural': 'Asset Requests'},
        ),
        migrations.AddField(
            model_name='assetrequest',
            name='cto_approve',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='assetrequest',
            name='cto_status',
            field=models.CharField(choices=[('approved', 'approved'), ('rejected', 'rejected'), ('pending', 'pending'), ('confirmed', 'confirmed')], default='pending', max_length=10),
        ),
        migrations.AddField(
            model_name='assetrequest',
            name='mgr_approve',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='assetrequest',
            name='mgr_status',
            field=models.CharField(choices=[('approved', 'approved'), ('rejected', 'rejected'), ('pending', 'pending'), ('confirmed', 'confirmed')], default='pending', max_length=10),
        ),
    ]
