"""
URL configuration for file_converter project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from converter.views import home, upload_pdf, upload_word, upload_pdf_to_ppt
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Show conversion selection
    path('convert/pdf/', upload_pdf, name='upload_pdf'),  # PDF to Word
    path('convert/word/', upload_word, name='upload_word'),  # Word to PDF
      path('convert/pdf-to-ppt/', upload_pdf_to_ppt, name='upload_pdf_to_ppt'),  # PDF to PowerPoint
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
