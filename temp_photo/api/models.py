# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import django

from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

# Location
class Photo(models.Model):

    # Add photo field

    date = models.DateTimeField(default=django.utils.timezone.now)

    photo = models.ImageField(upload_to= 'imagenes/photo')

    delta_time = models.IntegerField()

    name  = models.CharField(max_length=300)

    # # Metodo para obtener nombre de objeto
    def __unicode__(self):
      return self.name

@receiver(pre_delete, sender=Photo)
def mymodel_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.photo.delete(False)