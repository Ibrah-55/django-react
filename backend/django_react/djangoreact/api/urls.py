from django.urls import path
from .views import ArticlesListView, ArticlesDetailView

urlpatterns = [
    path('', ArticlesListView.as_view()),
    path('<pk>', ArticlesDetailView.as_view())
]
