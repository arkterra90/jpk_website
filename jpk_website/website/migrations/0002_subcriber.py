# Generated by Django 5.1.3 on 2024-11-15 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subcriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameFirst', models.CharField(max_length=100)),
                ('nameLast', models.CharField(max_length=100)),
                ('subEmail', models.EmailField(max_length=254)),
                ('dateSub', models.DateField()),
            ],
        ),
    ]