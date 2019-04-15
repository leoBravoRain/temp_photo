# api/urls.py

from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import Photo_View
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = {

    url(r'^photos/$', Photo_View.as_view(), name="create"),

  #   url(r'^update_danger/(?P<danger_id>[\w\ ]+)/(?P<new_danger_state>[\w\ ]+)/$', Dangers_Update_View.as_view(), name="update"),

  #   url(r'^danger_details/(?P<danger_id>[\w\ ]+)/$', Danger_Details_View.as_view(), name="danger_details"),

 	# url(r'area_of_company/$', Area_Of_Company_Create_View.as_view(), name="create_area_of_company"),

 	# url(r'suggestions_from_user/$', Suggestions_From_User_View.as_view(), name="create_suggestions_from_user"),
    
}

urlpatterns = format_suffix_patterns(urlpatterns)

# Add for media files
if settings.DEBUG:

    # La siguiente es para que Django sirva los archivos subidos por el usuario (Esto solo es para desarrollo)

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)