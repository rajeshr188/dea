# Generated by Django 3.1.4 on 2021-01-09 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dea', '0007_auto_20210109_1511'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ledgerstatement',
            name='closingBalance',
        ),
        migrations.AddField(
            model_name='ledgerstatement',
            name='ClosingBalance',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=13),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='accountstatement',
            name='ClosingBalance',
            field=models.DecimalField(decimal_places=3, max_digits=13),
        ),
        migrations.AlterField(
            model_name='accountstatement',
            name='TotalCredit',
            field=models.DecimalField(decimal_places=3, max_digits=13),
        ),
        migrations.AlterField(
            model_name='accountstatement',
            name='TotalDebit',
            field=models.DecimalField(decimal_places=3, max_digits=13),
        ),
        migrations.AlterField(
            model_name='accounttransaction',
            name='Amount',
            field=models.DecimalField(decimal_places=3, max_digits=13),
        ),
        migrations.AlterField(
            model_name='ledgertransaction',
            name='amount',
            field=models.DecimalField(decimal_places=3, max_digits=13),
        ),
    ]
