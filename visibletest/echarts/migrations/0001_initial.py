# Generated by Django 2.0.5 on 2018-05-28 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('price', models.FloatField()),
                ('sales', models.IntegerField()),
                ('address', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'goods',
            },
        ),
    ]