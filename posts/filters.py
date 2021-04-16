import django_filters
from django.db.models import Q

from posts.models import Post


class PostFilter(django_filters.FilterSet):
    author_email = django_filters.CharFilter(field_name='author__email', lookup_expr='icontains')
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    author_name = django_filters.CharFilter(method='author_name_filter')
    
    class Meta:
        model = Post
        fields = ('id', 'author_name', 'author_email', 'title')

    def author_name_filter(self, queryset, name, value):
        return queryset.filter(
            Q(author__first_name__icontains=value) | Q(author__last_name__icontains=value)
        )