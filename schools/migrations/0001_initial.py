# Generated by Django 2.0.6 on 2019-05-31 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254)),
                ('number_of_students', models.PositiveIntegerField(default=0)),
                ('number_of_staff', models.PositiveIntegerField(default=0)),
                ('address', models.TextField(blank=True, null=True)),
                ('date_school_was_created', models.DateTimeField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': "School's Profile",
                'ordering': ('name',),
            },
        ),
    ]
