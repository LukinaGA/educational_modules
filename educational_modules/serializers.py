from rest_framework import serializers

from educational_modules.models import Lesson, Topic, EducationalModule
from educational_modules.validators import validate_video_link


class LessonSerializer(serializers.ModelSerializer):

    video_link = serializers.CharField(validators=[validate_video_link])

    class Meta:
        model = Lesson
        fields = ["id", "name", "description", "topic", "video_link"]


class TopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topic
        fields = ["id", "name", "description", "educational_module"]


class EducationalModuleSerializer(serializers.ModelSerializer):

    class Meta:
        model = EducationalModule
        fields = ["id", "name", "description"]
