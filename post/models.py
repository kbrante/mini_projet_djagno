# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from autoslug import AutoSlugField

# Create your models here.
class Post(models.Model):
    title = models.CharField(verbose_name='Mon super titre', max_length=100)
    slug = AutoSlugField(populate_from='title')
    body = models.TextField(verbose_name='Contenu')
    creation_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'Article'
