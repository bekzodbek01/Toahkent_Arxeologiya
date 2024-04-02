from django.urls import path
from blog.api.about import AboutListAPIView,AboutRetrieveAPIView
from blog.api.archaeology import ArchaeologyRetrieveAPIView, ArchaeologyListViews
from blog.api.electronic import ElectronicListAPIView,ElectronicRetrieveAPIView
from blog.api.items import ItemsListAPIView,ItemsRetrieveAPIView
from blog.api.news import NewsListAPIView,NewsRetrieveAPIView
from blog.api.scientists import ScientistsListAPIView,ScientistsRetrieveAPIView
from blog.api.video import VideoListAPIView,VideoRetrieveAPIView
from blog.api.picture import PictureListAPIView,PictureRetrieveAPIView
urlpatterns = [

    path('about/',AboutListAPIView.as_view()),
    path('about/<int:pk>/',AboutRetrieveAPIView.as_view()),

    path('arxiv/',ArchaeologyListViews.as_view()),
    path('arxiv/<int:pk>/',ArchaeologyRetrieveAPIView.as_view()),

    path('electronic/',  ElectronicListAPIView.as_view()),
    path('electronic/<int:pk>/', ElectronicRetrieveAPIView.as_view()),

    path('items/', ItemsListAPIView.as_view()),
    path('items/<int:pk>/', ItemsRetrieveAPIView.as_view()),

    path('news/', NewsListAPIView.as_view()),
    path('news/<int:pk>/', NewsRetrieveAPIView.as_view()),

    path('olimlar/', ScientistsListAPIView.as_view()),
    path('olimlar/<int:pk>/', ScientistsRetrieveAPIView.as_view()),

    path('video/',VideoListAPIView.as_view()),
    path('video/<int:pk>/', VideoRetrieveAPIView.as_view()),

    path('picture/', PictureListAPIView.as_view()),
    path('picture/<int:pk>/', PictureRetrieveAPIView.as_view()),

]
