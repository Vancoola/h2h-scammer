from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.urls import reverse
from io import BytesIO
from PIL import Image
from django.core.files.base import ContentFile
import os


# Create your models here.

class CountryModel(models.Model):
    name = models.CharField('Название', max_length=255)
    code = models.CharField('Код', max_length=255, null=True, blank=True)
    flag = models.URLField('Флаг', null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Страну'
        verbose_name_plural = 'Страны'


class NewsModel(models.Model):
    title = models.CharField('Название', max_length=255)
    slug = models.SlugField('Слаг', unique=True, db_index=True)
    text = CKEditor5Field('Текст')
    logo = models.ImageField('Логотип', null=True)
    local = models.ForeignKey(CountryModel, on_delete=models.CASCADE, verbose_name='Страна', related_name='country')

    def save(self, *args, **kwargs):
        img_io = BytesIO()
        im = Image.open(self.logo).convert('RGB')
        im.save(img_io, format='WEBP')
        name = os.path.splitext(self.logo.name)[0] + '.webp'
        self.logo = ContentFile(img_io.getvalue(), name)
        super(NewsModel, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('news-page', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class QuestionModel(models.Model):
    name = models.CharField('Имя', max_length=255)
    telenumber = models.CharField('Номер телефона', max_length=255)
    email = models.EmailField('Почта')
    msg = models.TextField('Сообщение')
    date_of_application = models.DateTimeField('Дата обращения', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class SeasonModel(models.Model):
    league = models.ForeignKey("LeagueModel", verbose_name='Лига', on_delete=models.CASCADE,
                               related_name='season_league')
    year = models.IntegerField('Год')
    start = models.DateTimeField('Начало')
    end = models.DateTimeField('Конец', null=True, blank=True)
    current = models.BooleanField('Текущий')
    events = models.BooleanField('События')
    lineups = models.BooleanField()
    statistics_fixtures = models.BooleanField()
    statistics_players = models.BooleanField()
    standings = models.BooleanField()
    players = models.BooleanField()
    top_scorers = models.BooleanField()
    top_assists = models.BooleanField()
    top_cards = models.BooleanField()
    injuries = models.BooleanField()
    predictions = models.BooleanField()
    odds = models.BooleanField()


    def __str__(self):
        return self.league.name

    class Meta:
        verbose_name = 'Сезон'
        verbose_name_plural = 'Сезоны'


class TeamModel(models.Model):
    team_id = models.IntegerField('Id по api', primary_key=True, unique=True, db_index=True, editable=True)
    name = models.CharField('Имя', max_length=255)
    code = models.CharField('Код', max_length=255, blank=True, null=True)
    # country = models.ForeignKey('CountryModel', verbose_name='Страна', on_delete=models.CASCADE)
    founded = models.IntegerField(null=True, blank=True)
    national = models.BooleanField(default=False)
    logo = models.URLField(null=True, blank=True)
    league = models.ManyToManyField("LeagueModel", through="TopListModel")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'


class GameModel(models.Model):
    game_id = models.IntegerField('Id', primary_key=True, unique=True, db_index=True)
    long = models.CharField(max_length=255, blank=True, null=True)
    short = models.CharField(max_length=255, blank=True, null=True)
    elapsed = models.IntegerField(null=True, blank=True)
    seconds = models.CharField(max_length=10, null=True, blank=True)
    league = models.ForeignKey("LeagueModel", verbose_name="Лига", on_delete=models.CASCADE, related_name='games')
    home = models.ForeignKey(TeamModel, verbose_name="Дома", on_delete=models.CASCADE, related_name='home_team')
    away = models.ForeignKey(TeamModel, verbose_name="Гости", on_delete=models.CASCADE, related_name='away_team')
    home_goals = models.IntegerField('Гол (Дома)', default=0, blank=True)
    away_goals = models.IntegerField('Гол (Гости)', default=0, blank=True)
    # stopped = models.BooleanField()
    # blocked = models.BooleanField()
    # finished = models.BooleanField()
    update = models.DateTimeField(auto_now=True, editable=False)
    date = models.DateField(null=True, blank=True)
    winner = models.ForeignKey(TeamModel, verbose_name='Победители', on_delete=models.CASCADE,
                               related_name='winner_team', null=True, blank=True)
    referee = models.CharField(max_length=255, null=True, blank=True)
    round = models.CharField(max_length=255, null=True, blank=True)

    # slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.league.name


class TopListModel(models.Model):
    league = models.ForeignKey("LeagueModel", on_delete=models.CASCADE, related_name='league_top')
    team = models.ForeignKey("TeamModel", on_delete=models.CASCADE, related_name='team')
    place = models.IntegerField('Место', null=True, blank=True, default=1)
    win = models.IntegerField('Победы', default=0)
    draw = models.IntegerField('Ничья', default=0)
    lose = models.IntegerField('Поражение', default=0)
    matches_played = models.IntegerField('Матчей сыграно', default=0)
    point = models.IntegerField('Очков', default=0)
    goalsDiff = models.IntegerField('GD', default=0)
    is_home = models.BooleanField(default=False)
    is_away = models.BooleanField(default=False)

    def __str__(self):
        return self.team.name + self.league.name

    class Meta:
        unique_together = ('league', 'team')
        ordering = ('-point',)


class LeagueModel(models.Model):
    league_id = models.IntegerField(verbose_name='Id по api', unique=True, db_index=True,
                                    primary_key=True)
    name = models.CharField('Название', max_length=255)
    type = models.CharField('Тип', max_length=255)
    logo = models.URLField('Лого')
    country = models.ForeignKey('CountryModel', on_delete=models.CASCADE, verbose_name='Страна')
    slug = models.SlugField('Слаг', unique=True, null=True, blank=True, max_length=255)

    def __str__(self):
        return self.name

    def year_getter(self):
        print(self.season_league.first().year)
        return self.season_league.first().year

    def get_absolute_url(self):
        return reverse('game', kwargs={'game_slug': self.slug})

    class Meta:
        verbose_name = 'Лига'
        verbose_name_plural = 'Лиги'
        ordering = ('-games__date',)


class MainColumnModel(models.Model):
    name = models.CharField('Имя', max_length=255)
    url = models.CharField('Ссылка', max_length=255, null=True, blank=True)
    country = models.ForeignKey('CountryModel', on_delete=models.CASCADE, verbose_name='country', null=True, blank=True)

    def __str__(self):
        return self.name

    def clean(self):
        if self.url is not None:
            if self.url[-1] != '/':
                self.url = self.url + '/'


class ColumnModel(models.Model):
    name = models.CharField('Имя', max_length=255)
    url = models.CharField('Ссылка', max_length=255, null=True, blank=True)
    main_column = models.ForeignKey('MainColumnModel', on_delete=models.CASCADE, related_name='column')

    def clean(self):
        if self.url is not None:
            if self.url[-1] != '/':
                self.url = self.url + '/'

    def __str__(self):
        return self.name


class InfoModel(models.Model):
    country = models.ForeignKey('CountryModel', on_delete=models.CASCADE)
    name = models.CharField('Имя SEO', max_length=225, null=True, blank=True)
    text = CKEditor5Field(verbose_name='SEO Текст', null=True, blank=True)
    full_text = CKEditor5Field(verbose_name='Полный SEO Текст', null=True, blank=True)
    telenumber = models.CharField(verbose_name='Номер телефона', max_length=255)
    telegram = models.CharField(verbose_name='Телеграм', max_length=255)
    whatsup = models.CharField(verbose_name='WhatsUp', max_length=255)
    facebook = models.CharField(verbose_name='Facebook', max_length=255)
    instagram = models.CharField(verbose_name='Instagram', max_length=255)
    x = models.CharField(verbose_name='X', max_length=255)
    youtube = models.CharField(verbose_name='YouTube', max_length=255)

    class Meta:
        verbose_name = 'Инфо'
        verbose_name_plural = 'Инфо'


    def __str__(self):
        return self.country.name
