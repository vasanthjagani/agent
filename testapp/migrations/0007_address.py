# Generated by Django 2.1.3 on 2018-11-24 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0006_auto_20181124_1251'),
    ]

    operations = [
        migrations.CreateModel(
            name='address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addressid', models.CharField(max_length=100)),
                ('agentid', models.CharField(max_length=100)),
                ('addressline1', models.CharField(max_length=100)),
                ('addressline2', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('pincode', models.IntegerField(default=False)),
                ('landmark', models.CharField(max_length=100)),
                ('agentaddress', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.agent')),
            ],
        ),
    ]
