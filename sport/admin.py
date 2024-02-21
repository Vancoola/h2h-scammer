from django.contrib import admin
from .models import QuestionModel, NewsModel, CountryModel, LeagueModel, SeasonModel, GameModel, TeamModel, TopListModel, MainColumnModel, ColumnModel
from .models import InfoModel

@admin.register(QuestionModel)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_of_application', 'telenumber')
    readonly_fields = ('name', 'telenumber', 'email', 'msg')

    def has_add_permission(self, request, obj=None):
        return False


class ColumnAdmin(admin.TabularInline):
    model = ColumnModel
    fk = 'main_column'


@admin.register(MainColumnModel)
class MainColumnAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [ColumnAdmin]


@admin.register(NewsModel)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'slug')
    list_filter = ('local',)


admin.site.register(InfoModel)

@admin.register(CountryModel)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    search_fields = ('name',)


@admin.register(LeagueModel)
class LeagueModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'league_id')
    search_fields = ('name',)

# admin.site.register(SeasonModel)
@admin.register(SeasonModel)
class SeasonModelAdmin(admin.ModelAdmin):
    list_display = ('year', '__str__')
    search_fields = ( 'year', 'league__name')

@admin.register(TeamModel)
class TeamModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'team_id')
    search_fields = ('name', 'team_id')


# admin.site.register(GameModel)

@admin.register(GameModel)
class GameAdmin(admin.ModelAdmin):
    list_display = ('league',)
    search_fields = ('game_id',)

# admin.site.register(TopListModel)

@admin.register(TopListModel)
class TopListModelAdmin(admin.ModelAdmin):
    search_fields = ('team__name',)
