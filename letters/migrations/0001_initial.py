# Generated by Django 3.1.7 on 2021-05-28 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Letter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('letter_title', models.CharField(blank=True, max_length=200, null=True)),
                ('letter_type', models.CharField(blank=True, max_length=200, null=True)),
                ('school_association', models.CharField(blank=True, max_length=200, null=True)),
                ('author_prefix', models.CharField(blank=True, max_length=200, null=True)),
                ('author_first_name', models.CharField(blank=True, max_length=200, null=True)),
                ('author_last_name', models.CharField(blank=True, max_length=200, null=True)),
                ('author_title', models.CharField(blank=True, max_length=200, null=True)),
                ('organization_name', models.CharField(blank=True, max_length=200, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('country', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
