# Generated by Django 4.1.6 on 2023-02-26 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('user_password', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
    ]
