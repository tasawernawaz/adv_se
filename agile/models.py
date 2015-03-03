from django.db import models


class Project(models.Model):
    project_name = models.CharField(max_length=200)
    started_at = models.DateTimeField()
    due_date = models.DateTimeField()


class Team(models.Model):
    projects = models.ManyToManyField(Project)
    team_name = models.CharField(max_length=200)


class Task(models.Model):
    project = models.ForeignKey(Project)
    team = models.ForeignKey(Team)


class Engineer(models.Model):
    team = models.ForeignKey(Team)
    name = models.CharField(max_length=200)
    started_work = models.DateTimeField()


class Skill(models.Model):
    engineer = models.ManyToManyField(Engineer)
    skill = models.CharField(max_length=200)



