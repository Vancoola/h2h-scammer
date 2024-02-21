from django import template
from django.template.defaultfilters import stringfilter
from sport.models import TopListModel

register = template.Library()


@register.simple_tag()
def top_list(league, team):
    return TopListModel.objects.filter(league=league, team__team_id=team).values_list('place')[0][0]