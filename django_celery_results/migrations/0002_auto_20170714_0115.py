# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celery_results', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskresult',
            name='task_args',
            field=models.TextField(null=True, editable=False),
        ),
        migrations.AddField(
            model_name='taskresult',
            name='task_name',
            field=models.CharField(max_length=256, null=True, editable=False, db_index=True),
        ),
    ]