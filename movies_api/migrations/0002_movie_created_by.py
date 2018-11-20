# Generated by Django 2.1.3 on 2018-11-19 17:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='created_by',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='movies', to=settings.AUTH_USER_MODEL),
        ),
    ]