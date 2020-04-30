from django.contrib import admin
from .models import *


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'status','project','assigned_to')
    list_filter = ('title', 'project')
    ordering = ('start_date',)
    search_fields = ('title', 'project')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title', 'members')
    ordering = ('title',)
    search_fields = ('title',)


admin.site.register(Project,ProjectAdmin)
admin.site.register(Task,TaskAdmin)
