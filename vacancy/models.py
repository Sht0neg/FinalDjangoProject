from django.db import models
from django.contrib.auth.models import User
from user.models import Profile

class Vacancy(models.Model):
    title = models.CharField(verbose_name="Название вакансии", max_length=100)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_query_name="vacancies", related_name="vacancies")
    description = models.TextField(verbose_name="Описание")
    price = models.FloatField(verbose_name="Заработная плата")
    publication_date = models.DateField(verbose_name="Дата публикации")

    profile = models.ManyToManyField(Profile, related_query_name="submit_vacancies", blank=True, related_name="submit_vacancies")

    date_create = models.DateTimeField(verbose_name="Дата добавления", auto_now_add=True)
    date_edit = models.DateTimeField(verbose_name="Дата изменения", auto_now=True)

    def parse_object(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author.parse_object(),
            "description": self.description,
            "price": self.price,
            "publication_date": self.publication_date.month,
        }

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"
        ordering = ("-date_create", )

