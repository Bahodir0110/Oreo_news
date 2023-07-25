from django.db import models

class Articles(models.Model):
    title = models.CharField('Title', max_length=50)
    intro = models.CharField('Intro', max_length=250)
    full_text = models.TextField('Article')
    date = models.DateTimeField('Date')

    def __str__(self):
        return self.title
