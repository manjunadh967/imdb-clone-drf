from django.http import HttpResponse

def home(request):
    return HttpResponse("IMDB API is running 🚀" \
                        "Please Use any below paths for data:" \
                        "watch/"
                        "account/")


from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('dashboard/', admin.site.urls),
    path('watch/', include('watchlist_app.api.urls')),
    # path('api-auth/', include('rest_framework.urls')),
    path('account/', include('user_app.api.urls')),
    path('', home),

]
