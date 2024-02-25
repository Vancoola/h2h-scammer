from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.views.generic import TemplateView, DetailView
from sport.forms import QuestionForms
from sport.models import NewsModel, GameModel, TopListModel, LeagueModel, MainColumnModel, InfoModel
from django.utils.safestring import mark_safe
from django.http import HttpResponseNotFound
from django.db.models import Q
from rest_framework import viewsets, generics
from .serializer import *
from rest_framework.response import Response
import json
from django.utils import translation
from datetime import date
from django.core.paginator import Paginator


class TopListViewSet(viewsets.ViewSet):
    def create(self, request, *args, **kwargs):
        print(request.data)
        serializers = TopListSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data['id'])
        else:
            return Response(serializers.errors)

    def update(self, request):
        if 'team' in request.data and 'league' in request.data:
            mdl = TopListModel.objects.filter(team_id=1989, league=request.data['league']).first()
            print(mdl)
            print(request.data)
            serializer = TopListSerializer(instance=mdl, data=request.data, )
            if serializer.is_valid():
                # serializer.save()
                return Response({"OK"})
            return Response(serializer.errors)
        else:
            return Response({'not id'})


class GameViewSet(viewsets.ViewSet):
    def list(self, *args, **kwargs):
        obj = GameModel.objects.filter(date__gte=str(date.today()))
        serializer = GameSerializer(instance=obj, many=True)
        return Response(serializer.data)

    def create(self, request):
        print(request.data)
        serializer = GameSerializer(data=json.loads(request.data))
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Game'})
        else:
            return Response(serializer.errors)

    def update(self, request):
        if 'game_id' in request.data:
            mdl = GameModel.objects.filter(game_id=request.data['game_id']).first()
            print(mdl)
            print(request.data)
            serializer = GameSerializer(instance=mdl, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"OK"})
            return Response(serializer.errors)
        else:
            return Response({'not id'})


class LeagueViewSet(viewsets.ViewSet):
    def list(self, *args, **kwargs):
        print('000000000000000')
        serializer = LeagueSerializer(instance=LeagueModel.objects.all(), many=True)
        # print(serializer.data)
        # print(serializer.data)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = LeagueSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Country'})
        else:
            return Response(serializer.errors)


class SeasonViewSet(viewsets.ViewSet):
    def create(self, request, *args, **kwargs):
        print(json.loads(request.data))
        serializer = SeasonSerializer(data=json.loads(request.data))
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Season'})
        else:
            return Response(serializer.errors)


class TeamViewSet(viewsets.ViewSet):
    def create(self, request, *args, **kwargs):
        print(json.loads(request.data))
        serializer = TeamSerializer(data=json.loads(request.data))
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Team'})
        else:
            return Response(serializer.errors)


class CountryViewSet(viewsets.ViewSet):

    def create(self, request, *args, **kwargs):
        print(request.data['name'])
        serializers = CountrySerializer(CountryModel.objects.filter(name__contains=str(request.data['name'])).first())
        print(serializers.data)
        return Response(serializers.data)

    def update(self, request):
        serializer = CountrySerializer(data=request.data, many=True)
        print(request.data)
        if serializer.is_valid():
            print(serializer.data)
            serializer.save()
            return Response({'message': 'Country'})
        else:
            return Response(serializer.errors)


# class CountryViewSet(viewsets.ModelViewSet):
#     queryset = CountryModel.objects.all()
#     serializer_class = CountrySerializer


class PersonalVS(DetailView):
    model = LeagueModel
    template_name = 'main/in-person-meeting-template.html'
    slug_url_kwarg = 'game_slug'

    def post(self, req, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data()
        if 'switch' in self.request.POST and self.request.session['LANGUAGE_SESSION_KEY'] != 'en':
            self.request.session['LANGUAGE_SESSION_KEY'] = "en"
            translation.activate("en")
        else:
            self.request.session['LANGUAGE_SESSION_KEY'] = str(self.request.LANGUAGE_CODE)
            translation.activate(str(self.request.LANGUAGE_CODE))
        if 'search' in self.request.POST and self.request.POST['search'] != '':
            return redirect('search', self.request.POST['search'])
        if context["form"].is_valid():
            context["form"].save()
        return super(PersonalVS, self).render_to_response(context)

    def get_context_data(self, **kwargs):
        if 'LANGUAGE_SESSION_KEY' not in self.request.session:
            self.request.session['LANGUAGE_SESSION_KEY'] = "en"
        translation.activate(self.request.session['LANGUAGE_SESSION_KEY'])
        context = super().get_context_data(**kwargs)
        context['country_code'] = context['object'].country.name
        context['form'] = QuestionForms(self.request.POST)
        context['league_name'] = context['object'].name
        context['games'] = context['object'].games.all
        context['lang_code'] = str(self.request.session['LANGUAGE_SESSION_KEY']).upper()
        # print(context['object'].games.first)
        context['columns'] = MainColumnModel.objects.filter(
            Q(country__code=str(self.request.session['LANGUAGE_SESSION_KEY']).upper()) |
            Q(country__code='WL'))
        context['info'] = InfoModel.objects.filter(
            Q(country__code=str(self.request.session['LANGUAGE_SESSION_KEY']).upper()) |
            Q(country__code='WL')).first()
        context['seo_text'] = mark_safe(
            InfoModel.objects.filter(Q(country__code=str(self.request.session['LANGUAGE_SESSION_KEY']).upper()) |
                                     Q(country__code='WL')).first().text)
        return context


class IndexTV(TemplateView):
    template_name = 'main/index.html'

    def post(self, req, *args, **kwargs):
        context = self.get_context_data()
        if 'switch' in self.request.POST and self.request.session['LANGUAGE_SESSION_KEY'] != 'en':
            self.request.session['LANGUAGE_SESSION_KEY'] = "en"
            translation.activate("en")
        elif self.request.session['LANGUAGE_SESSION_KEY'] == 'en':
            self.request.session['LANGUAGE_SESSION_KEY'] = str(self.request.LANGUAGE_CODE)
            translation.activate(str(self.request.LANGUAGE_CODE))
        if 'search' in self.request.POST and self.request.POST['search'] != '':
            return redirect('search', self.request.POST['search'])
        if context["form"].is_valid():
            context["form"].save()
        return super(TemplateView, self).render_to_response(context)

    def get_context_data(self, **kwargs):
        if 'LANGUAGE_SESSION_KEY' not in self.request.session:
            self.request.session['LANGUAGE_SESSION_KEY'] = "en"
            translation.activate(self.request.LANGUAGE_CODE)
        leagues = Paginator(LeagueModel.objects.filter(games__isnull=False, games__date__gte=str(date.today())), 10)
        self.request.session['active_page'] = 1
        context = super().get_context_data(**kwargs)
        context['form'] = QuestionForms(self.request.POST)
        context['lang_code'] = str(self.request.session['LANGUAGE_SESSION_KEY']).upper()
        context['leagues'] = leagues.page(1).object_list
        context['num_pages'] = leagues.num_pages
        context['num_pages_range'] = leagues.page_range
        context['columns'] = MainColumnModel.objects.filter(
            Q(country__code=str(self.request.session['LANGUAGE_SESSION_KEY']).upper()) |
            Q(country__code='WL'))
        context['info'] = InfoModel.objects.filter(
            Q(country__code=str(self.request.session['LANGUAGE_SESSION_KEY']).upper()) |
            Q(country__code='WL')).first()
        context['seo_text'] = mark_safe(
            InfoModel.objects.filter(Q(country__code=str(self.request.session['LANGUAGE_SESSION_KEY']).upper()) |
                                     Q(country__code='WL')).first().text)

        # context['pages'] = leagues.page_range

        return context


def SearchTV(request, search):
    # global obj
    if 'LANGUAGE_SESSION_KEY' not in request.session:
        request.session['LANGUAGE_SESSION_KEY'] = "en"
    translation.activate(request.session['LANGUAGE_SESSION_KEY'])
    if request.method == 'POST':
        if 'switch' in request.POST and request.session['LANGUAGE_SESSION_KEY'] != 'en':
            request.session['LANGUAGE_SESSION_KEY'] = "en"
            translation.activate("en")
        else:
            request.session['LANGUAGE_SESSION_KEY'] = str(request.LANGUAGE_CODE)
            translation.activate(str(request.LANGUAGE_CODE))
        if 'search' in request.POST and request.POST['search'] != '':
            return redirect('search', request.POST['search'])
        form = QuestionForms(request.POST)
        if form.is_valid():
            form.save()
    obj = get_list_or_404(LeagueModel, name__contains=search, games__isnull=False)
    form = QuestionForms()

    return render(request, 'main/search-page.html',
                  {'lang_code': str(request.session['LANGUAGE_SESSION_KEY']).upper(), 'form': form, 'search': search,
                   'leagues': obj,
                   'columns': MainColumnModel.objects.filter(
                       Q(country__code=str(request.session['LANGUAGE_SESSION_KEY']).upper()) |
                       Q(country__code='WL')), 'info': InfoModel.objects.filter(
                      Q(country__code=str(request.session['LANGUAGE_SESSION_KEY']).upper()) |
                      Q(country__code='WL')).first(), 'seo_text': mark_safe(
                      InfoModel.objects.filter(Q(country__code=str(request.session['LANGUAGE_SESSION_KEY']).upper()) |
                                               Q(country__code='WL')).first().text)})


def News(request):
    if 'LANGUAGE_SESSION_KEY' not in request.session:
        request.session['LANGUAGE_SESSION_KEY'] = "en"
    translation.activate(request.session['LANGUAGE_SESSION_KEY'])
    if request.method == 'POST':
        if 'switch' in request.POST and request.session['LANGUAGE_SESSION_KEY'] != 'en':
            request.session['LANGUAGE_SESSION_KEY'] = "en"
            translation.activate("en")
        else:
            request.session['LANGUAGE_SESSION_KEY'] = str(request.LANGUAGE_CODE)
            translation.activate(str(request.LANGUAGE_CODE))
        if 'search' in request.POST and request.POST['search'] != '':
            return redirect('search', request.POST['search'])
        form = QuestionForms(request.POST)
        if form.is_valid():
            form.save()

    form = QuestionForms()
    return render(request, 'main/news.html', {'news':
        NewsModel.objects.filter(
            Q(local__code=str(request.LANGUAGE_CODE).upper()) | Q(local__code='wl')),
        'lang_code': str(request.session['LANGUAGE_SESSION_KEY']).upper(), 'form': form,
        'columns': MainColumnModel.objects.filter(
            Q(country__code=str(request.session['LANGUAGE_SESSION_KEY']).upper()) |
            Q(country__code='WL')),
        'info': InfoModel.objects.filter(Q(country__code=str(request.session['LANGUAGE_SESSION_KEY']).upper()) |
                                         Q(country__code='WL')).first(), 'seo_text': mark_safe(
            InfoModel.objects.filter(Q(country__code=str(request.session['LANGUAGE_SESSION_KEY']).upper()) |
                                     Q(country__code='WL')).first().text)})


def NewsPage(request, slug):
    if 'LANGUAGE_SESSION_KEY' not in request.session:
        request.session['LANGUAGE_SESSION_KEY'] = "en"
    translation.activate(request.session['LANGUAGE_SESSION_KEY'])
    if request.method == 'POST':
        if 'switch' in request.POST and request.session['LANGUAGE_SESSION_KEY'] != 'en':
            request.session['LANGUAGE_SESSION_KEY'] = "en"
            translation.activate("en")
        else:
            request.session['LANGUAGE_SESSION_KEY'] = str(request.LANGUAGE_CODE)
            translation.activate(str(request.LANGUAGE_CODE))
        if 'search' in request.POST and request.POST['search'] != '':
            return redirect('search', request.POST['search'])
        form = QuestionForms(request.POST)
        if form.is_valid():
            form.save()

    form = QuestionForms()
    obj = get_object_or_404(NewsModel, slug=slug)
    return render(request, 'main/news-page.html', {'logo': obj.logo, 'text': mark_safe(obj.text),
                                                   'title': obj.title,
                                                   'lang_code': str(request.session['LANGUAGE_SESSION_KEY']).upper(),
                                                   'form': form, 'columns': MainColumnModel.objects.filter(
            Q(country__code=str(request.session['LANGUAGE_SESSION_KEY']).upper()) |
            Q(country__code='WL')), 'info': InfoModel.objects.filter(
            Q(country__code=str(request.session['LANGUAGE_SESSION_KEY']).upper()) |
            Q(country__code='WL')).first(), 'seo_text': mark_safe(
            InfoModel.objects.filter(Q(country__code=str(request.session['LANGUAGE_SESSION_KEY']).upper()) |
                                     Q(country__code='WL')).first().text)})


def handler404(request, *args, **kwargs):
    if 'LANGUAGE_SESSION_KEY' not in request.session:
        request.session['LANGUAGE_SESSION_KEY'] = "en"
    translation.activate(request.session['LANGUAGE_SESSION_KEY'])
    if request.method == 'POST':
        if 'switch' in request.POST and request.session['LANGUAGE_SESSION_KEY'] != 'en':
            request.session['LANGUAGE_SESSION_KEY'] = "en"
            translation.activate("en")
        else:
            request.session['LANGUAGE_SESSION_KEY'] = str(request.LANGUAGE_CODE)
            translation.activate(str(request.LANGUAGE_CODE))
        if 'search' in request.POST and request.POST['search'] != '':
            return redirect('search', request.POST['search'])
        form = QuestionForms(request.POST)
        if form.is_valid():
            form.save()
    form = QuestionForms()
    return render(request, 'main/404.html', {'lang_code': str(request.session['LANGUAGE_SESSION_KEY']).upper(),
                                                   'form': form, 'columns': MainColumnModel.objects.filter(
            Q(country__code=str(request.session['LANGUAGE_SESSION_KEY']).upper()) |
            Q(country__code='WL')), 'info': InfoModel.objects.filter(
            Q(country__code=str(request.session['LANGUAGE_SESSION_KEY']).upper()) |
            Q(country__code='WL')).first(), 'seo_text': mark_safe(
            InfoModel.objects.filter(Q(country__code=str(request.session['LANGUAGE_SESSION_KEY']).upper()) |
                                     Q(country__code='WL')).first().text)})


def page(request, page_pk):
    if 'LANGUAGE_SESSION_KEY' not in request.session:
        request.session['LANGUAGE_SESSION_KEY'] = "en"
    translation.activate(request.session['LANGUAGE_SESSION_KEY'])
    if request.method == 'POST':
        if 'switch' in request.POST and request.session['LANGUAGE_SESSION_KEY'] != 'en':
            request.session['LANGUAGE_SESSION_KEY'] = "en"
            translation.activate("en")
        else:
            request.session['LANGUAGE_SESSION_KEY'] = str(request.LANGUAGE_CODE)
            translation.activate(str(request.LANGUAGE_CODE))
        if 'search' in request.POST and request.POST['search'] != '':
            return redirect('search', request.POST['search'])
        form = QuestionForms(request.POST)
        if form.is_valid():
            form.save()
    form = QuestionForms()
    pagin = Paginator(LeagueModel.objects.filter(games__isnull=False, games__date__gte=str(date.today())), 10)
    request.session['active_page'] = page_pk
    return render(request, 'main/page.html', {'leagues': pagin.page(page_pk),
                                              'all_num_pages': pagin.num_pages, 'num_page': page_pk, 'lang_code': str(request.session['LANGUAGE_SESSION_KEY']).upper(),
                                                   'form': form, 'columns': MainColumnModel.objects.filter(
            Q(country__code=str(request.session['LANGUAGE_SESSION_KEY']).upper()) |
            Q(country__code='WL')), 'info': InfoModel.objects.filter(
            Q(country__code=str(request.session['LANGUAGE_SESSION_KEY']).upper()) |
            Q(country__code='WL')).first(), 'seo_text': mark_safe(
            InfoModel.objects.filter(Q(country__code=str(request.session['LANGUAGE_SESSION_KEY']).upper()) |
                                     Q(country__code='WL')).first().text)})
