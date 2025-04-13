from django.urls import path
from .views import AuthorDataView

urlpatterns = [
    path("api/authors/", AuthorDataView.as_view(), name='author-data'),
]
