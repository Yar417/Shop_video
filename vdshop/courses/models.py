from django.db import models
from django.urls import reverse


class Course(models.Model):
    slug = models.SlugField('Уникальное название курса ')
    title = models.CharField('Название курса', max_length=120)
    description = models.TextField('Описание курса')
    image = models.ImageField('Изображение', default='default.png', upload_to='course_images')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('course_detail', kwargs={'slug': self.slug})


class Lesson(models.Model):
    slug = models.SlugField('Уникальное название урока')
    title = models.CharField('Название урока', max_length=100)
    desc = models.TextField('Описание урока')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Какой курс')
    number = models.IntegerField('Номер урока')
    video = models.CharField('URL видео', max_length=100)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('lesson_detail', kwargs={'slug': self.course.slug, 'lesson_slug': self.slug})
