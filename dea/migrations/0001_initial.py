# Generated by Django 3.1.4 on 2020-12-31 12:57

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='AccountType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AccountType', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='EntityType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ledger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('AccountType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dea.accounttype')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='dea.ledger')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TransactionType_DE',
            fields=[
                ('XactTypeCode', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='TransactionType_Ext',
            fields=[
                ('XactTypeCode_ext', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='LedgerTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, unique=True)),
                ('ledgerno_dr', models.CharField(max_length=50)),
                ('amount', models.DecimalField(decimal_places=3, max_digits=10)),
                ('ledger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dea.ledger')),
            ],
        ),
        migrations.CreateModel(
            name='LedgerStatement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(unique=True)),
                ('ClosingBalance', models.DecimalField(decimal_places=3, max_digits=10)),
                ('ledger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dea.ledger')),
            ],
        ),
        migrations.CreateModel(
            name='AccountType_Ext',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('XactTypeCode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dea.transactiontype_de')),
            ],
        ),
        migrations.CreateModel(
            name='AccountTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, unique=True)),
                ('Amount', models.DecimalField(decimal_places=3, max_digits=10)),
                ('Account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dea.account')),
                ('XactTypeCode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dea.transactiontype_de')),
                ('XactTypeCode_ext', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dea.transactiontype_ext')),
                ('ledger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dea.ledger')),
            ],
        ),
        migrations.CreateModel(
            name='AccountStatement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(unique=True)),
                ('ClosingBalance', models.DecimalField(decimal_places=3, max_digits=10)),
                ('TotalCredit', models.DecimalField(decimal_places=3, max_digits=10)),
                ('TotalDebit', models.DecimalField(decimal_places=3, max_digits=10)),
                ('AccountNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dea.account')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='AccountType_Ext',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dea.accounttype_ext'),
        ),
    ]