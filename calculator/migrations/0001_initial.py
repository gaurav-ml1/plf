# Generated by Django 5.0.6 on 2024-06-12 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReverseMortgageInput',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('margin', models.DecimalField(choices=[(3.5, 3.5), (4.5, 4.5), (2.3, 2.3)], decimal_places=2, max_digits=10)),
                ('age', models.IntegerField()),
                ('property_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('current_loan_balance', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
