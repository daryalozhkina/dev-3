from django.db import models


class CollegeGroup(models.Model):
    name = models.CharField(max_length=128)
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    category = models.ForeignKey(CollegeGroup,
                                 on_delete=models.CASCADE)
    name = models.IntegerField('Количество студентов', default=0)

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
