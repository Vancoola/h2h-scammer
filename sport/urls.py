from django.urls import path
from sport.views import IndexTV, SearchTV, NewsPage, News, PersonalVS
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', IndexTV.as_view(), name='index'),
    # path('register/', Register.as_view(), name='register'),
    path('search/<str:search>/', SearchTV, name='search'),
    path('news/<slug:slug>/', NewsPage, name='news-page'),
    path('news/', News, name='news'),

    path('<slug:game_slug>', PersonalVS.as_view(), name='game'),

    # path('api/', LLMVS.as_view({'post': 'create'}))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)