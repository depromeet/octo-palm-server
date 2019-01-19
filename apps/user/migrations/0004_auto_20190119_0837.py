# Generated by Django 2.1.4 on 2019-01-19 08:37

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20190108_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialuser',
            name='extra_data',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict, verbose_name='기타 정보'),
        ),
        migrations.AddField(
            model_name='socialuser',
            name='provider',
            field=models.CharField(choices=[('google', '구글')], default='google', max_length=20, verbose_name='소셜 플랫폼'),
        ),
        migrations.AddField(
            model_name='socialuser',
            name='uid',
            field=models.CharField(default='', max_length=150, verbose_name='UID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='활성화 여부'),
        ),
    ]
