from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from apps.views import set_language
from root import settings

urlpatterns = [
    path('i18n/set_language/', set_language, name='set_language'),
    path('rosetta/', include('rosetta.urls')),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('ckeditor5/', include('django_ckeditor_5.urls'), name='ck_editor_5_upload_file'),  # Add CKEditor uploader URL
    path('', include('apps.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


