# Generated by Django 2.0 on 2019-06-14 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=20)),
                ('price', models.FloatField(default=0)),
            ],
            options={
                'db_table': 'books',
            },
        ),
    ]
