from django.urls import path
from blog import views


urlpatterns=[

    path("users/",views.UserCreateView.as_view()),
    path("blogs/",views.PostListCreateView.as_view()),
    path("blogs/<int:pk>/",views.PostRetrieveUpdateDestroyView.as_view()),
    path("blogs/<int:pk>/comments/",views.CommentCreateView.as_view()),
]