# Generated by Django 3.1.4 on 2021-01-03 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userclassname', models.CharField(max_length=50, verbose_name='UserClassName')),
            ],
            options={
                'verbose_name': 'UserClass',
                'verbose_name_plural': 'UserClasses',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('password', models.CharField(max_length=50, verbose_name='Password')),
                ('userclass', models.ManyToManyField(related_name='UserClass', to='authentication.UserClass')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
    ]