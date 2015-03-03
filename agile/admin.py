from django.contrib import admin
from agile.models import *


admin.site.register(Project)
admin.site.register(Team)
admin.site.register(Engineer)
admin.site.register(Skill)
admin.site.register(Task)