# Generated by Django 5.1.3 on 2024-12-08 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu_app', '0002_alter_kelas_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vocabulary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=100)),
                ('meaning', models.CharField(max_length=100)),
            ],
        ),
    ]
