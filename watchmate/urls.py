from django.http import HttpResponse


from django.contrib import admin
from django.urls import path, include
from watchlist_app.api.views import home


urlpatterns = [
    path('', home, name='home'),
    path('dashboard/', admin.site.urls),
    path('watch/', include('watchlist_app.api.urls')),
    # path('api-auth/', include('rest_framework.urls')),
    path('account/', include('user_app.api.urls')),

]
