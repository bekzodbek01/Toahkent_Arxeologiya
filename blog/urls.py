from django.urls import path
from blog.api.about import AboutListAPIView,AboutRetrieveAPIView
from blog.api.archaeology import ArchaeologyRetrieveAPIView, ArchaeologyListViews
from blog.api.electronic import list_electronic, electronic_detail
from blog.api.items import items_detail, list_items
from blog.api.news import list_news, news_detail
from blog.api.picture import list_picture, picture_detail
from blog.api.scientists import list_scientists, scientists_detail
from blog.api.video import list_video, video_detail
from blog.api.contact import ContactListCreateView
from blog.api.down import FileDownAsarView

urlpatterns = [
    path('about/', AboutListAPIView.as_view()),
    path('about/<int:pk>/', AboutRetrieveAPIView.as_view()),

    path('arxiv/', ArchaeologyListViews.as_view()),
    path('arxiv/<int:pk>/', ArchaeologyRetrieveAPIView.as_view()),

    path('electronic/', list_electronic, name='electronic-list'),
    path('electronic/<int:pk>/', electronic_detail, name='electronic-detail'),

    path('items/', list_items, name='news-list'),
    path('items/<int:pk>/', items_detail, name='news-detail'),

    path('news/', list_news, name='list_news'),
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

