# Generated by Django 3.1.2 on 2020-11-02 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RecurringEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('price', models.PositiveIntegerField()),
                ('comment', models.TextField(blank=True)),
                ('start', models.DateField()),
                ('end', models.DateField(null=True)),
                ('recurrence', models.DurationField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SingleEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('price', models.PositiveIntegerField()),
                ('comment', models.TextField(blank=True)),
                ('date', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]