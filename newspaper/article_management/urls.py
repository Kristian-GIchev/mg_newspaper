from django.urls import path

from newspaper.article_management.views import create_article, view_my_articles, edit_article, delete_article, view_article

urlpatterns = [
    path('create-article/', create_article, name='create_article'),
    path('view-my-articles/', view_my_articles, name='view_my_articles'),
    path('edit-article/<int:pk>', edit_article, name='edit_article'),
    path('delete-article/<int:pk>', delete_article, name='delete_article'),
    path('view-article/<int:pk>', view_article, name='view_article'),
]