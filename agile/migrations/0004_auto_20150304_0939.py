# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agile', '0003_remove_engineer_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.ForeignKey(default=1, to='agile.Category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='task_type',
            field=models.CharField(max_length=15, choices=[(b'1', b'Interface design'), (b'2', b'Database'), (b'3', b'Development')]),
            preserve_default=True,
        ),
    ]
