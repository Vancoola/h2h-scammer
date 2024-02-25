from rest_framework import serializers
from sport.models import LeagueModel, SeasonModel, CountryModel, GameModel, TeamModel, TopListModel


class LeagueSerializer(serializers.HyperlinkedModelSerializer):
    season = serializers.CharField(source='season_league.first.year', read_only=True)

    class Meta:
        model = LeagueModel
        fields = ('league_id', 'name', 'season')


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeasonModel
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryModel
        fields = '__all__'


class GameSerializer(serializers.ModelSerializer):
    season = serializers.IntegerField(source='league.season_league.first.year', read_only=True)

    class Meta:
        model = GameModel
        fields = ('game_id', 'long', 'short', 'season', 'update', 'referee', 'round', 'date', 'home_odds',
                  'away_odds', 'draw_odds', 'league', 'winner', 'home', 'away')
        # fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamModel
        fields = '__all__'


class TopListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopListModel
        fields = ('id', 'league', 'team', 'place', 'win', 'draw', 'lose', 'matches_played', 'point', 'goalsDiff',
                  'is_home', 'is_away', 'goals', 'form')
