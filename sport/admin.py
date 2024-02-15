from django.contrib import admin
from .models import QuestionModel, NewsModel, CountryModel, LeagueModel, SeasonModel, GameModel, TeamModel, TopListModel


@admin.register(QuestionModel)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_of_application', 'telenumber')
    readonly_fields = ('name', 'telenumber', 'email', 'msg')

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(NewsModel)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'slug')
    list_filter = ('local',)


admin.site.register(CountryModel)

admin.site.register(LeagueModel)
admin.site.register(SeasonModel)

admin.site.register(TeamModel)
admin.site.register(GameModel)
admin.site.register(TopListModel)
