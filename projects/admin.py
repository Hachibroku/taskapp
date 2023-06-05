from django.contrib import admin
from projects.models import Project

# Register your models here.
admin.site.register(Project)


class ProjectCategory(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "owner",
    )
