from django.contrib import admin

from educational_modules.models import EducationalModule, Topic, Lesson


@admin.register(EducationalModule)
class EducationalModuleAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "topic", "owner", "video_link")
    search_fields = ("name",)
    ordering = ("name",)