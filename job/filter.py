import django_filters
from .models import Job

class JobFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Job
        fields = '__all__'
        exclude= ['owner', 'job_description', 'image', 'slug']