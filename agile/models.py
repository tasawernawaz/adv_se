from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Project(models.Model):
    project_name = models.CharField(max_length=200)
    started_at = models.DateField()
    due_date = models.DateField()
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.project_name


class Team(models.Model):
    team_name = models.CharField(max_length=200)
    project = models.ForeignKey(Project, null=True, blank=True)

    def __str__(self):
        return self.team_name


class Task(models.Model):
    task_title = models.CharField(max_length=200)
    task_type = models.CharField(max_length=15, choices=(("1", "Interface design" ), ("2", "Database"), ("3", "Development")))
    task_priority = models.IntegerField(default=0)
    due_date = models.DateField()
    project = models.ForeignKey(Project)
    team = models.ForeignKey(Team)

    def __str__(self):
        return self.task_title


class Skill(models.Model):
    skill = models.CharField(max_length=200)

    def __str__(self):
        return self.skill


class Engineer(models.Model):
    user = models.ForeignKey(User)
    team = models.ForeignKey(Team)
    #name = models.CharField(max_length=200)
    started_work = models.DateField()
    skill = models.ManyToManyField(Skill)
    #
    #def __str__(self):
    #    return self.fir

