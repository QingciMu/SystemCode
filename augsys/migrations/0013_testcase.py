# Generated by Django 4.1.2 on 2022-12-13 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('augsys', '0012_alter_predicttask_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('taskName', models.CharField(max_length=255)),
                ('testCase', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'testCase',
            },
        ),
    ]
