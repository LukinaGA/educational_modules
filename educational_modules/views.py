from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from educational_modules.models import EducationalModule, Topic, Lesson
from educational_modules.paginators import LessonPagination
from educational_modules.serializers import EducationalModuleSerializer, TopicSerializer, LessonSerializer
from users.permissions import IsAdmin, IsModerator, IsTeacher, IsOwner


class EducationalModuleViewSet(viewsets.ModelViewSet):
    serializer_class = EducationalModuleSerializer
    queryset = EducationalModule.objects.all()

    def get_permissions(self):
        if self.action in ["create", "update", "destroy"]:
            self.permission_classes = (IsAuthenticated, IsAdmin)
        else:
            self.permission_classes = (AllowAny,)

        return super().get_permissions()


class TopicViewSet(viewsets.ModelViewSet):
    serializer_class = TopicSerializer
    queryset = Topic.objects.all()

    def get_permissions(self):
        if self.action in ["create", "update", "destroy"]:
            self.permission_classes = (IsAuthenticated, IsAdmin)
        else:
            self.permission_classes = (AllowAny,)

        return super().get_permissions()

class LessonCreateView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, IsTeacher | IsAdmin)

    def perform_create(self, serializer):
        lesson = serializer.save(owner=self.request.user)
        lesson.save()


class LessonListView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    pagination_class = LessonPagination


class LessonDetailView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonUpdateView(generics.UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, IsOwner)


class LessonDeleteView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, IsAdmin | IsOwner | IsModerator)
