# Generated by Django 4.1.5 on 2023-01-29 06:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('training_room', '0003_trainingblock_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingblock',
            name='user',
            field=models.ForeignKey(default='auth.User', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
