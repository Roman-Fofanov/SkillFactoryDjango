from django.forms import DateInput
from django_filters import FilterSet, DateFilter
from .models import News

class NewsFilter(FilterSet):
    date = DateFilter(field_name='datetime', widget=DateInput(attrs={'type': 'date'}), label='Поиск по дате',
                      lookup_expr='date__gte')
    class Meta:
       model = News
       fields = {
           'name': ['icontains'],
           'author': ['exact'],
       }