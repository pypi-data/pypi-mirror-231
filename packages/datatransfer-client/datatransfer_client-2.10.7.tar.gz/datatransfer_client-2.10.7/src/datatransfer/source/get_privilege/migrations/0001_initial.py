# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-29 15:46
from __future__ import unicode_literals

from __future__ import absolute_import
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='GetPrivilegeData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('risid', models.PositiveIntegerField(verbose_name='ID \u0432 \u0420\u0418\u0421')),
                ('person_type', models.SmallIntegerField(
                    verbose_name='1 - \u0448\u043a\u043e\u043b\u044c\u043d\u0438\u043a, 2 - \u0437\u0430\u044f\u0432\u043b\u0435\u043d\u0438\u0435')),
                ('exemption', models.PositiveIntegerField(verbose_name='ID \u043b\u044c\u0433\u043e\u0442\u044b')),
                ('start_date', models.DateField(
                    verbose_name='\u0414\u0430\u0442\u0430 \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u044f \u043b\u044c\u0433\u043e\u0442\u044b',
                    null=True, blank=True)),
                ('expiration_date', models.DateField(
                    verbose_name='\u0414\u0430\u0442\u0430 \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u044f \u043b\u044c\u0433\u043e\u0442\u044b',
                    null=True, blank=True)),
            ],
            options={
                'verbose_name': '\u0414\u0430\u043d\u043d\u044b\u0435 \u043e \u043f\u0440\u0438\u0432\u0435\u043b\u0435\u0433\u0438\u044f\u0445 \u0438\u0437 \u041a\u043e\u043d\u0442\u0438\u043d\u0433\u0435\u043d\u0442\u0430',
                'verbose_name_plural': '\u0414\u0430\u043d\u043d\u044b\u0435 \u043e \u043f\u0440\u0438\u0432\u0435\u043b\u0435\u0433\u0438\u044f\u0445 \u0438\u0437 \u041a\u043e\u043d\u0442\u0438\u043d\u0433\u0435\u043d\u0442\u0430',
            },
        ),
        migrations.CreateModel(
            name='GetPrivilegeSession',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now,
                                                   verbose_name='\u0414\u0430\u0442\u0430/\u0432\u0440\u0435\u043c\u044f \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
                ('session',
                 models.CharField(unique=True, max_length=256, verbose_name='\u0421\u0435\u0441\u0441\u0438\u044f')),
                ('processed', models.BooleanField(default=False,
                                                  verbose_name='\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u0430\u043d\u043e',
                                                  choices=[
                                                      (True, '\u0417\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u043e'),
                                                      (False,
                                                       '\u041d\u0435 \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u043e')])),
                ('message',
                 models.TextField(verbose_name='\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='GetPrivilegeStatistic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.PositiveIntegerField(
                    verbose_name='\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e')),
                ('model',
                 models.ForeignKey(verbose_name='\u041c\u043e\u0434\u0435\u043b\u044c', to='contenttypes.ContentType', on_delete=django.db.models.deletion.CASCADE,)),
                ('session', models.ForeignKey(
                    verbose_name='\u0421\u0435\u0441\u0441\u0438\u044f \u043e\u0431\u043c\u0435\u043d\u0430 \u0434\u0430\u043d\u043d\u044b\u043c\u0438',
                    to='get_privilege.GetPrivilegeSession', on_delete=django.db.models.deletion.CASCADE,)),
            ],
        ),
    ]
