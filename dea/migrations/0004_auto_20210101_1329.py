# Generated by Django 3.1.4 on 2021-01-01 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dea', '0003_auto_20210101_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ledgertransaction',
            name='ledger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='credit_txns', to='dea.ledger'),
        ),
        migrations.AlterField(
            model_name='ledgertransaction',
            name='ledgerno_dr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='debit_txns', to='dea.ledger'),
        ),
    ]
