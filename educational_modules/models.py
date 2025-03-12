from django.db import models

from users.models import User


class EducationalModule(models.Model):
    name = models.CharField(max_length=150, verbose_name="Образовательный модуль", help_text="Введите название модуля")
    description = models.TextField(verbose_name="Описание образовательного модуля", help_text="Введите описание модуля")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Владелец",
                              help_text="Выберите владельца модуля", related_name="modules", null=True, blank=True)

    class Meta:
        verbose_name = "Образовательный модуль"
        verbose_name_plural = "Образовательные модули"

    def __str__(self):
        return self.name
