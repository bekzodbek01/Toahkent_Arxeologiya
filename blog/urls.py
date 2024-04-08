from django.urls import path
from blog.api.archaeology import ArchaeologyListAPIView,detail_archaeology
from blog.api.about import detail_about,list_about
from blog.api.electronic import list_electronic, electronic_detail
from blog.api.items import items_detail,ItemsListAPIView
from blog.api.news import NewsListAPIView, news_detail
from blog.api.picture import list_picture, picture_detail
from blog.api.scientists import list_scientists, scientists_detail
from blog.api.video import list_video, video_detail
from blog.api.contact import ContactListCreateView
from blog.api.down import FileDownAsarView

urlpatterns = [


    path('about/',list_about),
    path('about/<int:pk>/',detail_about),

    path('arxiv/',ArchaeologyListAPIView.as_view()),
    path('arxiv/<int:pk>/',detail_archaeology),

    path('electronic/', list_electronic, name='electronic-list'),
    path('electronic/<int:pk>/', electronic_detail, name='electronic-detail'),

    path('items/', ItemsListAPIView.as_view()),
    path('items/<int:pk>/', items_detail, name='news-detail'),

    path('news/', NewsListAPIView.as_view()),
    path('news/<int:pk>/', news_detail, name='news_detail'),

    path('scientists/', list_scientists, name='list_scientists'),
    path('scientists/<int:pk>/', scientists_detail, name='scientists_detail'),

    path('videos/', list_video, name='list_video'),
    path('videos/<int:pk>/', video_detail, name='video_detail'),

    path('pictures/', list_picture, name='list_picture'),
    path('pictures/<int:pk>/', picture_detail, name='picture_detail'),

    path('contact/', ContactListCreateView.as_view()),

    path('items/downland/<int:pk>/', FileDownAsarView.as_view()),

]

