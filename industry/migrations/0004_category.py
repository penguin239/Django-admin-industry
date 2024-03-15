# Generated by Django 4.2.11 on 2024-03-15 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('industry', '0003_delete_sitesetting'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=64)),
                ('level', models.CharField(max_length=16)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
