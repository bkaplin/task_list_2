# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_subtask'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtask',
            name='description',
            field=models.CharField(max_length=70, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subtask',
            name='task',
            field=models.ForeignKey(verbose_name='\u0417\u0430\u0434\u0430\u0447\u0430', to='tasks.Task'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.CharField(max_length=70, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435'),
            preserve_default=True,
        ),
    ]
