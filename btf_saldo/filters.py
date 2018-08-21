import django_filters
from .models import Talento

class TalentosFilter(django_filters.FilterSet):
    class Meta:
        model = Talento
        fields = ['quem', ]