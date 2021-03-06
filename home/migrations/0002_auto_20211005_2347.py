# Generated by Django 3.2.7 on 2021-10-05 18:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='zip',
        ),
        migrations.AddField(
            model_name='contact',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='desc',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.CharField(default=django.utils.timezone.now, max_length=122),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=122),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.CharField(default=django.utils.timezone.now, max_length=12),
            preserve_default=False,
        ),
    ]
