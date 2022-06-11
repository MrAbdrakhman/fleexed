# Generated by Django 4.0.5 on 2022-06-11 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_yoga', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, db_index=True, default='No name', max_length=222, null=True)),
                ('description', models.TextField(blank=True)),
                ('price', models.IntegerField(blank=True, max_length=5)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
