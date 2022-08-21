# Generated by Django 4.1 on 2022-08-21 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Namespace',
            fields=[
                ('name', models.SlugField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('namespace_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.namespace')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('base.namespace', models.Model),
        ),
    ]
