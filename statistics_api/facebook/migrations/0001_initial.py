# Generated by Django 3.2.7 on 2021-09-10 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('user_id', models.CharField(max_length=255)),
                ('post_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('likes', models.IntegerField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PostHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(db_index=True, max_length=255)),
                ('post_id', models.CharField(max_length=255)),
                ('likes', models.IntegerField()),
                ('created_at', models.DateField()),
            ],
        ),
    ]