from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter() 

router.register('list', views.CourseViewset)
urlpatterns = [
    path('', include(router.urls)),
    path('Course/<int:pk>/', views.CourseDetail.as_view(), name='Course_Detail'),
]