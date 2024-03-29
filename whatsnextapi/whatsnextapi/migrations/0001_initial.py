# Generated by Django 2.2.7 on 2019-11-19 02:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Production',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_whatsnextapi.production_set+', to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('production_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='whatsnextapi.Production')),
                ('tmdb_url', models.CharField(max_length=100)),
                ('watched', models.BooleanField()),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('whatsnextapi.production',),
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('production_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='whatsnextapi.Production')),
                ('tvdb_url', models.CharField(max_length=100)),
                ('watched', models.SmallIntegerField()),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('whatsnextapi.production',),
        ),
        migrations.CreateModel(
            name='WatchList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('productions', models.ManyToManyField(to='whatsnextapi.Production')),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.SmallIntegerField()),
                ('episodes', models.SmallIntegerField()),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='whatsnextapi.Show')),
            ],
        ),
    ]
