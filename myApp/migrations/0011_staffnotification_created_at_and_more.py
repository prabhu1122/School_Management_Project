# Generated by Django 4.1.5 on 2023-02-20 15:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0010_staffnotification'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffnotification',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='staffnotification',
            name='messages',
            field=models.TextField(),
        ),
    ]