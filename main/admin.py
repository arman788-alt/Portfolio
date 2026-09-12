from django.contrib import admin
from .models import ContactMessage,Education,Skill,Project

# Register your models here.
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "email",
        "subject",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "subject",
        "message",
    )

    readonly_fields = ("created_at",)

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = (
        "degree",
        "vname",
        
    )
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display=(
        "no",
        "shortname",
    )

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display=(
        "fullname",
    )

    