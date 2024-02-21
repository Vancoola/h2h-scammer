from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DetailView
from sport.forms import QuestionForms
from sport.models import NewsModel, GameModel, TopListModel, LeagueModel, MainColumnModel, InfoModel
from django.utils.safestring import mark_safe
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.db.models import Q
from rest_framework import viewsets
from .serializer import *
from rest_framework.response import Response


class TopListViewSet(viewsets.ViewSet):
    def create(self, request, *args, **kwargs):
        print(request.data)
        serializers = TopListSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'message': 'Top list successfully'})
        else:
            return Response(serializers.errors)


class GameViewSet(viewsets.ViewSet):
    def create(self, request):
        print(request.data)
        serializer = GameSerializer(data=json.loads(request.data))
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Game'})
        else:
            return Response(serializer.errors)


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

import json
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['country_code'] = context['object'].country.name
        context['league_name'] = context['object'].name
        context['games'] = context['object'].games.all
        context['lang_code'] = str(self.request.LANGUAGE_CODE).upper()
        # print(context['object'].games.first)
        context['columns'] = MainColumnModel.objects.filter(Q(country__code=str(self.request.LANGUAGE_CODE).upper()) |
                                                            Q(country__code='WL'))
        context['info'] = InfoModel.objects.filter(Q(country__code=str(self.request.LANGUAGE_CODE).upper()) |
                                                   Q(country__code='WL')).first()
        context['seo_text'] = mark_safe(InfoModel.objects.filter(Q(country__code=str(self.request.LANGUAGE_CODE).upper()) |
                                     Q(country__code='WL')).first().text)
        return context


class IndexTV(TemplateView):
    template_name = 'main/index.html'

    def post(self, req, *args, **kwargs):
        context = self.get_context_data()
        if self.request.POST['search'] != '':
            return HttpResponseRedirect('search/' + self.request.POST['search'])
        if context["form"].is_valid():
            context["form"].save()
        return super(TemplateView, self).render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = QuestionForms(self.request.POST)
        context['lang_code'] = str(self.request.LANGUAGE_CODE).upper()
        context['leagues'] = LeagueModel.objects.all().order_by('-games__update')
        context['columns'] = MainColumnModel.objects.filter(Q(country__code=str(self.request.LANGUAGE_CODE).upper()) |
                                                            Q(country__code='WL'))
        context['info'] = InfoModel.objects.filter(Q(country__code=str(self.request.LANGUAGE_CODE).upper()) |
                                                            Q(country__code='WL')).first()
        context['seo_text'] = mark_safe(InfoModel.objects.filter(Q(country__code=str(self.request.LANGUAGE_CODE).upper()) |
                                                            Q(country__code='WL')).first().text)
        return context


def SearchTV(request, search):
    global obj
    if request.method == 'POST':
        form = QuestionForms(request.POST)
        if form.is_valid():
            form.save()

    if LeagueModel.objects.filter(name__contains=search).exists():
        obj = LeagueModel.objects.filter(name__contains=search)
    else:
        return HttpResponseNotFound("Тут могла быть ваша реклама или красивое окно '404'")
    form = QuestionForms()

    return render(request, 'main/search-page.html',
                  {'lang_code': str(request.LANGUAGE_CODE).upper(), 'form': form, 'search': search, 'leagues': obj,
                   'columns': MainColumnModel.objects.filter(Q(country__code=str(request.LANGUAGE_CODE).upper()) |
                                                            Q(country__code='WL')), 'info': InfoModel.objects.filter(Q(country__code=str(request.LANGUAGE_CODE).upper()) |
                                                   Q(country__code='WL')).first(), 'seo_text': mark_safe(InfoModel.objects.filter(Q(country__code=str(request.LANGUAGE_CODE).upper()) |
                                                            Q(country__code='WL')).first().text)})


def News(request):
    if request.method == 'POST':
        form = QuestionForms(request.POST)
        if form.is_valid():
            form.save()

    form = QuestionForms()
    return render(request, 'main/news.html', {'news':
        NewsModel.objects.filter(
            Q(local__code=str(request.LANGUAGE_CODE).upper()) | Q(local__code='wl')),
        'lang_code': str(request.LANGUAGE_CODE).upper(), 'form': form, 'columns': MainColumnModel.objects.filter(Q(country__code=str(request.LANGUAGE_CODE).upper()) |
                                                            Q(country__code='WL')), 'info': InfoModel.objects.filter(Q(country__code=str(request.LANGUAGE_CODE).upper()) |
                                                   Q(country__code='WL')).first(), 'seo_text': mark_safe(InfoModel.objects.filter(Q(country__code=str(request.LANGUAGE_CODE).upper()) |
                                                            Q(country__code='WL')).first().text)})


def NewsPage(request, slug):
    if request.method == 'POST':
        form = QuestionForms(request.POST)
        if form.is_valid():
            form.save()

    form = QuestionForms()
    obj = get_object_or_404(NewsModel, slug=slug)
    return render(request, 'main/news-page.html', {'logo': obj.logo, 'text': mark_safe(obj.text),
                                                   'title': obj.title, 'lang_code': str(request.LANGUAGE_CODE).upper(),
                                                   'form': form, 'columns': MainColumnModel.objects.filter(Q(country__code=str(request.LANGUAGE_CODE).upper()) |
                                                            Q(country__code='WL')), 'info': InfoModel.objects.filter(Q(country__code=str(request.LANGUAGE_CODE).upper()) |
                                                   Q(country__code='WL')).first(), 'seo_text': mark_safe(InfoModel.objects.filter(Q(country__code=str(request.LANGUAGE_CODE).upper()) |
                                                            Q(country__code='WL')).first().text)})
