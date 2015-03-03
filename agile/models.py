from django.db import models


class Project(models.Model):
    project_name = models.CharField(max_length=200)
    started_at = models.DateField()
    due_date = models.DateField()

    def __str__(self):
        return self.project_name


class Team(models.Model):
    team_name = models.CharField(max_length=200)
    projects = models.ManyToManyField(Project, null=True, blank=True)

    def __str__(self):
        return self.team_name


class Task(models.Model):
    task_title = models.CharField(max_length=200)
    project = models.ForeignKey(Project)
    team = models.ForeignKey(Team)

    def __str__(self):
        return self.task_title



class Engineer(models.Model):
    team = models.ForeignKey(Team)
    name = models.CharField(max_length=200)
    started_work = models.DateField()

    def __str__(self):
        return self.name


class Skill(models.Model):
    engineer = models.ManyToManyField(Engineer)
    skill = models.CharField(max_length=200)

    def __str__(self):
        return self.skill

