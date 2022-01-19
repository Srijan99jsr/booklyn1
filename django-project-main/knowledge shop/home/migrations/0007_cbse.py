# Generated by Django 3.2.7 on 2021-10-20 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_defence_engg_icse_jee_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cbse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('cat', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('quant', models.IntegerField()),
                ('image_url', models.CharField(max_length=2083)),
            ],
        ),
    ]
