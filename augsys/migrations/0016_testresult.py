# Generated by Django 4.1.2 on 2023-03-06 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('augsys', '0015_threshold'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('taskName', models.CharField(max_length=255)),
                ('dataset', models.CharField(max_length=255)),
                ('IOU', models.CharField(max_length=255, null=True)),
                ('OSE', models.CharField(max_length=255, null=True)),
                ('USE', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'testResult',
            },
        ),
    ]
