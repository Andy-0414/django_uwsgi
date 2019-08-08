from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PostView,PeopleView
post_list = PostView.as_view({
    'get': 'list'
})
post_detail = PostView.as_view({
    'get': 'retrieve',
})
people_list = PeopleView.as_view({
    'get': 'list'
})
people_detail = PeopleView.as_view({
    'get': 'retrieve',
})
urlpatterns = format_suffix_patterns([
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('posts/', post_list, name='post_list'),
    path('posts/<int:pk>/', post_detail, name='post_detail'),
    path('people/', people_list, name='people_list'),
    path('people/<int:pk>/', people_detail, name='people_detail'),
])
