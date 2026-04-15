from django.urls import path, include
# from rest_framework.routers import DefaultRouter

from watchlist_app.api import views

# router = DefaultRouter()
# router.register('stream', StreamPlatformVS, basename='streamplatform')


urlpatterns = [

    path('list/', views.WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', views.WatchDetailAV.as_view(), name='movie-detail'),
    path('list2/', views.WatchListGV.as_view(), name='watch-list'),

    # path('', include(router.urls)),

    path('stream/', views.StreamPlatformAV.as_view(), name='stream-list'),
    path('stream/<int:pk>/', views.StreamPlatformDetailAV.as_view(), name='stream-detail'),


    path('<int:pk>/review-create/', views.ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/reviews/', views.ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>/', views.ReviewDetail.as_view(), name='review-detail'),


    path('reviews/', views.UserReview.as_view(), name='user-review-detail'),
    # path('reviews/<str:username>/', views.UserReview.as_view(), name='review-user'),

]
