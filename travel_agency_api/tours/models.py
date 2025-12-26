from django.db import models
from django.contrib.auth.models import User

class Tour(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название тура")
    description = models.TextField(verbose_name="Описание")
    country = models.CharField(max_length=100, verbose_name="Страна")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Тур"
        verbose_name_plural = "Туры"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, verbose_name="Тур")
    booking_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата бронирования")
    number_of_people = models.PositiveIntegerField(default=1, verbose_name="Количество человек")

    def __str__(self):
        return f"{self.user.username} → {self.tour.title}"

    class Meta:
        verbose_name = "Бронирование"
        verbose_name_plural = "Бронирования"

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, verbose_name="Тур")
    rating = models.PositiveSmallIntegerField(verbose_name="Оценка (1-5)")
    comment = models.TextField(blank=True, verbose_name="Комментарий")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} — {self.rating}★"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"