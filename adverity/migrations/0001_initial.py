# Generated by Django 4.1.7 on 2023-02-16 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collections',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.CharField(max_length=255)),
                ('created', models.DateTimeField(verbose_name='date created')),
            ],
        ),
    ]
