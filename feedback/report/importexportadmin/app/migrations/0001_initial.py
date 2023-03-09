# Generated by Django 4.1.7 on 2023-03-08 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('cost', models.IntegerField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]