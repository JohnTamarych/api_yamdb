from django.db import models
from titles.models import Title
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import User


class Review(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE, related_name='reviews', verbose_name='Произведение')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews', verbose_name='Автор')
    text = models.TextField('Комментарий оценки')
    score = models.PositiveSmallIntegerField(
        'Оценка',
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ]
    )
    pub_date = models.DateTimeField('Дата и время', auto_now_add=True)

    def __str__(self):
        return self.pk

    class Meta:
        ordering = ['-pub_date']


class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments', verbose_name='Оценка')
    author = author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name='Автор')
    text = models.TextField('Комментарий к оценке')
    pub_date = models.DateTimeField('Дата и время', auto_now_add=True)

    class Meta:
        ordering = ['-pub_date']