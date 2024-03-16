# Generated by Django 4.2.11 on 2024-03-16 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('industry', '0005_remove_category_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(max_length=64, unique=True, verbose_name='类别'),
        ),
        migrations.AlterField(
            model_name='category',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='启用'),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='机械名称')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='industry.category')),
            ],
        ),
    ]