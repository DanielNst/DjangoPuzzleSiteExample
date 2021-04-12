"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from app import views
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = [


    # создать новый элемент каталога
    path('createpuzzle/', views.createpuzzle, name="createpuzzle"),

    # редактирование элемента каталога
    path('editpuzzle/<int:puzzleNumber>/', views.editpuzzle, name="editpuzzle"),
        
    # удалить элемент каталога
    path('deletepuzzle_<int:puzzleNumber>/', views.deletepuzzle, name="deletepuzzle"),

     #главная страница
    path('', views.index, name="index"),
    path('index/', views.index, name="index1"),

    # каталог
    path('r^album/', views.album, name="album"),
    
    # администратирование каталога
    path('album_admin/', views.album_admin, name="album_admin"),

    # подробная информация об элементе каталога
    path('puzzleinfo_<int:puzzleNumber>/', views.puzzleinfo, name="puzzleinfo"),

    path('admin', admin.site.urls),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

