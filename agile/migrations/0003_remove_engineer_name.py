# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agile', '0002_engineer_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='engineer',
            name='name',
        ),
    ]
