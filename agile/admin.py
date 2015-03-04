from django.contrib import admin
from agile.models import *

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_priority', 'task_title', 'due_date', 'task_type', 'project', 'team')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'started_at', 'due_date')

#@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('team_name', 'project')

admin.site.register(Team)
admin.site.register(Category)
@admin.register(Engineer)
class EngineerAdmin(admin.ModelAdmin):
    list_display = ('user', 'team', 'started_work')

admin.site.register(Skill)
