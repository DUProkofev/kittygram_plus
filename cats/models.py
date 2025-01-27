from django.db import models


class Achievement(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Owner(models.Model):
    first_name = models.CharField('Имя', max_length=128)
    last_name = models.CharField('Фамилия', max_length=128)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Cat(models.Model):
    name = models.CharField('Кличка', max_length=16)
    color = models.CharField('Окрас', max_length=16)
    birth_year = models.IntegerField('Год рождения')
    owner = models.ForeignKey(
        Owner,
        on_delete=models.CASCADE,
        related_name='cats',
        verbose_name='Хозяин',
    )
    achievements = models.ManyToManyField(
        Achievement,
        through='AchievementCat'
    ),

    def __str__(self):
        return self.name


class AchievementCat(models.Model):
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.achievement} {self.cat}'
