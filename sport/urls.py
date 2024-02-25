from django.urls import path, include
from sport.views import IndexTV, SearchTV, NewsPage, News, PersonalVS, LeagueViewSet, CountryViewSet, SeasonViewSet, GameViewSet, TeamViewSet, TopListViewSet
from django.conf import settings
from django.conf.urls.static import static
from sport.views import handler404, page
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(60)(IndexTV.as_view()), name='index'),
    # path('register/', Register.as_view(), name='register'),
    path('search/<str:search>/', SearchTV, name='search'),
    path('news/<slug:slug>/', NewsPage, name='news-page'),
    path('news/', News, name='news'),
    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),
    path('<slug:game_slug>', cache_page(60)(PersonalVS.as_view()), name='game'),
    path('api/leagues/', LeagueViewSet.as_view({'get': 'list', 'post': 'create'}), name='api_league'),
    path('api/country/', CountryViewSet.as_view({'post': 'create'}), name='api_country'),
    path('api/seasons/', SeasonViewSet.as_view({'post': 'create'}), name='api_seasons'),
    path('api/games/', GameViewSet.as_view({'post': 'create', 'get': 'list', 'put': 'update'}), name='api_games'),
    path('api/teams/', TeamViewSet.as_view({'post': 'create'}), name='api_teams'),
    path('api/toplist/', TopListViewSet.as_view({'post': 'create', 'put': 'update'}), name='api_top'),
    path('page/<int:page_pk>/', page, name='page')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

