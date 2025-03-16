from django.urls import path
from rest_framework.routers import DefaultRouter

from educational_modules.apps import EducationalModulesConfig
from educational_modules.views import EducationalModuleViewSet, TopicViewSet, LessonCreateView, LessonListView, \
    LessonDetailView, LessonUpdateView, LessonDeleteView


app_name = EducationalModulesConfig.name

router = DefaultRouter()
router.register(r'educational_modules', EducationalModuleViewSet)
router.register(r'topics', TopicViewSet)
urlpatterns = [
    path("lessons/create/", LessonCreateView.as_view(), name="create_lesson"),
    path("lessons/", LessonListView.as_view(), name="lessons"),
    path("lessons/<int:pk>/", LessonDetailView.as_view(), name="lesson"),
    path("lessons/<int:pk>/update/", LessonUpdateView.as_view(), name="update_lesson"),
    path("lessons/<int:pk>/delete/", LessonDeleteView.as_view(), name="delete_lesson"),
] + router.urls
