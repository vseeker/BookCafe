from django.db import models

# Create your models here.


class Books(models.Model):
    name = models.CharField(verbose_name="name",
                            max_length=200)
    author = models.CharField(verbose_name="author",
                              max_length=200)
    publisher = models.CharField(verbose_name="publisher",
                                 max_length=200)
    uploader = models.CharField(verbose_name="uploader",
                                max_length=200)
    classification = models.CharField(verbose_name="classification",
                                      max_length=200)
    isbn = models.CharField(verbose_name="isbn",
                            max_length=200)
    novelty = models.FloatField(verbose_name="novelty",
                                max_length=200)
    description = models.CharField(verbose_name="description",
                                   max_length=200)
    image = models.ImageField(verbose_name="image",
                              max_length=200)
    title = models.CharField(verbose_name="title",
                             max_length=200)

    publication_date= models.DateTimeField('date published')



