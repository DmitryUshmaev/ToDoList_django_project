# Generated by Django 4.1.3 on 2023-01-26 07:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bot', '0003_rename_chat_id_tguser_tg_chat_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tguser',
            name='tg_chat_id',
        ),
        migrations.RemoveField(
            model_name='tguser',
            name='tg_user_ud',
        ),
        migrations.AddField(
            model_name='tguser',
            name='chat_id',
            field=models.BigIntegerField(default=None, unique=True, verbose_name='Chat ID'),
        ),
        migrations.AlterField(
            model_name='tguser',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tguser',
            name='username',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Username'),
        ),
        migrations.AlterField(
            model_name='tguser',
            name='verification_code',
            field=models.CharField(blank=True, default=None, max_length=32, null=True),
        ),
    ]
