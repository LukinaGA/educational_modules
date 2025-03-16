from rest_framework import serializers


def validate_video_link(value):
    if not value.startswith("https://www.youtube.com/") or not value.startswith("https://rutube.ru/"):

        raise serializers.ValidationError("Неверная ссылка на видео. Добавьте ссылку на видео с Youtube или Rutube")
