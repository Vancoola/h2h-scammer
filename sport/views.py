from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DetailView
from sport.forms import QuestionForms
from sport.models import NewsModel, GameModel, TopListModel, LeagueModel
from django.utils.safestring import mark_safe
from django.http import HttpResponseNotFound, HttpResponseRedirect


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
        context['leagues'] = LeagueModel.objects.all()
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
                  {'lang_code': str(request.LANGUAGE_CODE).upper(), 'form': form, 'search': search, 'leagues': obj})


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
