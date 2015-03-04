# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Engineer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('started_work', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project_name', models.CharField(max_length=200)),
                ('started_at', models.DateField()),
                ('due_date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('skill', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('task_title', models.CharField(max_length=200)),
                ('task_type', models.CharField(max_length=15, choices=[(b'1', b'Interface design'), (b'2', b'Database')])),
                ('task_priority', models.IntegerField(default=0)),
                ('due_date', models.DateField()),
                ('project', models.ForeignKey(to='agile.Project')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('team_name', models.CharField(max_length=200)),
                ('project', models.ForeignKey(blank=True, to='agile.Project', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='task',
            name='team',
            field=models.ForeignKey(to='agile.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='engineer',
            name='skill',
            field=models.ManyToManyField(to='agile.Skill'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='engineer',
            name='team',
            field=models.ForeignKey(to='agile.Team'),
            preserve_default=True,
        ),
    ]
