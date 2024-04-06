from django.urls import path
from blog.api.about import detail_about,list_about
from blog.api.archaeology import ArchaeologyListAPIView,detail_archaeology
from blog.api.electronic import ElectronicListAPIView,ElectronicRetrieveAPIView
from blog.api.items import ItemsListAPIView,ItemsRetrieveAPIView
from blog.api.news import NewsListAPIView,NewsRetrieveAPIView
from blog.api.scientists import ScientistsListAPIView,ScientistsRetrieveAPIView
from blog.api.video import VideoListAPIView,VideoRetrieveAPIView
from blog.api.picture import PictureListAPIView,PictureRetrieveAPIView
from blog.api.contact import ContactListCreateView

from blog.api.down import FileDownAsarView

urlpatterns = [

    path('about/',list_about),
    path('about/<int:pk>/',detail_about),

    path('arxiv/',ArchaeologyListAPIView.as_view()),
    path('arxiv/<int:pk>/',detail_archaeology),

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

    path('contact/', ContactListCreateView.as_view()),

    path('items/downland/<int:pk>/', FileDownAsarView.as_view()),

]

