# Generated by Django 4.2.6 on 2024-08-23 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScriptedData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('scripted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
