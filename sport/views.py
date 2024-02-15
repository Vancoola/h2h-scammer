from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DetailView
from sport.forms import QuestionForms
from sport.models import NewsModel, GameModel, TopListModel, LeagueModel
from django.utils.safestring import mark_safe


# from rest_framework import viewsets
# from main.models import LeaguesModel, GameModel, TeamsModel, GameTHRModel
# from main.serializer import LeaguesSerializer
# from rest_framework.response import Response

# Create your views here.


# class LLMVS(viewsets.ViewSet):
#     def create(self, request):
#         obj = LeaguesSerializer(data=request.POST)
#         if obj.is_valid():
#             obj.save()
#             return Response({'ok'})
#         else:
#             return Response(obj.errors)


class PersonalVS(DetailView):
    model = LeagueModel
    template_name = 'main/in-person-meeting-template.html'
    slug_url_kwarg = 'game_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print(context['object'].league_top.first().place)
        context['country_code'] = context['object'].country.name
        context['league_name'] = context['object'].name
        # print(context['object'].games.first)
        return context


class IndexTV(TemplateView):
    template_name = 'main/index.html'

    def post(self, req, *args, **kwargs):
        context = self.get_context_data()
        # print(context['form'].is_valid())
        if context["form"].is_valid():
            context["form"].save()
        return super(TemplateView, self).render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = QuestionForms(self.request.POST)
        # context['lang_code'] = str(self.request.LANGUAGE_CODE).upper()
        # context['toplist'] = TopListModel.objects.filter(league=)
        print(GameModel.objects.all())
        print(LeagueModel.objects.all().values('name'))
        context['leagues'] = LeagueModel.objects.all()
        # context[]
        return context


def SearchTV(request, search):
    if request.method == 'POST':
        form = QuestionForms(request.POST)
        if form.is_valid():
            form.save()

    form = QuestionForms()

    return render(request, 'main/search-page.html',
                  {'lang_code': str(request.LANGUAGE_CODE).upper(), 'form': form, 'search': search})


def News(request):
    if request.method == 'POST':
        form = QuestionForms(request.POST)
        if form.is_valid():
            form.save()

    form = QuestionForms()
    return render(request, 'main/news.html', {'news':
                                                  NewsModel.objects.filter(
                                                      local__code_country=str(request.LANGUAGE_CODE)),
                                              'lang_code': str(request.LANGUAGE_CODE).upper(), 'form': form})


def NewsPage(request, slug):
    if request.method == 'POST':
        form = QuestionForms(request.POST)
        if form.is_valid():
            form.save()

    form = QuestionForms()
    obj = get_object_or_404(NewsModel, slug=slug)
    return render(request, 'main/news-page.html', {'logo': obj.logo, 'text': mark_safe(obj.text),
                                                   'title': obj.title, 'lang_code': str(request.LANGUAGE_CODE).upper(),
                                                   'form': form})

# class Register(CreateView):
#     form_class = RegisterForms
#     template_name = 'main/register.html'
#     success_url = reverse_lazy('index')
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context


# def PersonVS(req, game_slug):
#     game = get_object_or_404(GameModel, slug=game_slug)
#     print(GameTHRModel.objects.filter(game=game).values()[0]['team_status'])
#     print([x for x in GameTHRModel.objects.filter(game=game).values() if x['team_status'] == 'away'])
#     home_players = GameModel.objects.filter(slug=game_slug).values_list('game__team__team_name')[0]
#     away_players = GameModel.objects.filter(slug=game_slug).values_list('game__team__team_name')[1]
#     return render(req, 'main/in-person-meeting-template.html', {'lang_code': str(req.LANGUAGE_CODE).upper(), 'game':game, 'home_players':home_players, 'away_players': away_players})
