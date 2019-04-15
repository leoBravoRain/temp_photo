# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics
from .serializers import Photo_Serializer
from .models import Photo

import django

from datetime import timedelta

def remove_expired_elements():

    photos = Photo.objects.all()

    current_date = django.utils.timezone.now()

    for photo in photos:

        print('Analizing file ' + str(photo.id) + '\n')

        delta_time_file = ((current_date - photo.date).seconds)

        delta_time_file = timedelta(seconds = delta_time_file)

        print("delta time: ")

        print((delta_time_file))

        user_delta_time = (photo.delta_time)

        user_delta_time = timedelta(seconds = 60*user_delta_time)

        print("User: ")

        print((user_delta_time))

        if delta_time_file > user_delta_time:

            print("Remove file " + str(photo.id))

            photo.delete()

        else:

            print('Dont remove file')

        print('\n')

    return True 

# Manage comments of danger
class Photo_View(generics.ListCreateAPIView):

    print('\n NEW REQUEST \n')

    # queryset = Videos_Location.objects.all()
    serializer_class = Photo_Serializer

    # remove_expired_elements()

    def perform_create(self, serializer):

        remove_expired_elements()

        """Save the post data when creating a new bucketlist."""
        serializer.save()

    # Filtering query set
    def get_queryset(self):

        remove_expired_elements()

        # get location_id
        # danger_id = self.kwargs['danger_id']

        # Filter by location id
        photos = Photo.objects.all()

        # Return queryset
        return photos