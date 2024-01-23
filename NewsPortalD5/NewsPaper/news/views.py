from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from datetime import datetime

# Create your views here.
class NewsList(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'

class NewsDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'


    # def get_context_data(self, **kwargs):
    #     # С помощью super() мы обращаемся к родительским классам
    #     # и вызываем у них метод get_context_data с теми же аргументами,
    #     # что и были переданы нам.
    #     # В ответе мы должны получить словарь.
    #     context = super().get_context_data(**kwargs)
    #     # К словарю добавим текущую дату в ключ 'time_now'.
    #     context['time_now'] = datetime.utcnow()
    #     # Добавим ещё одну пустую переменную,
    #     # чтобы на её примере рассмотреть работу ещё одного фильтра.
    #     context['next_sale'] = None
    #     return context

