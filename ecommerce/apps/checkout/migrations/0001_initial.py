# Generated by Django 3.1.7 on 2023-06-17 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryOptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_name', models.CharField(help_text='Required', max_length=255, verbose_name='Delivery Name')),
                ('delivery_price', models.DecimalField(decimal_places=2, error_messages={'name': {'max_length': 'The name is too long.'}}, help_text='Max 999.99', max_digits=5, verbose_name='Delivery Price')),
                ('delivery_method', models.CharField(choices=[('IS', 'In-Store'), ('HD', 'Home Delivery'), ('DD', 'Digital Delivery')], help_text='Required', max_length=255, verbose_name='Delivery Method')),
                ('delivery_timeframe', models.CharField(help_text='Required', max_length=255, verbose_name='Delivery Timeframe')),
                ('delivery_window', models.CharField(help_text='Required', max_length=255, verbose_name='Delivery Window')),
                ('order', models.IntegerField(default=0, help_text='Required', verbose_name='List Order')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Delivery Option',
                'verbose_name_plural': 'Delivery Options',
            },
        ),
        migrations.CreateModel(
            name='PaymentSelections',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Required', max_length=255, verbose_name='Payment Name')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Payment Selection',
                'verbose_name_plural': 'Payment Selections',
            },
        ),
    ]