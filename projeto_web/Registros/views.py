# Registros/views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied, RequestAborted
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Registro, Comentario
from django.shortcuts import render
from django.http import HttpResponse


def pesquisa_list_view(request):
    queryset = Registro.objects.all()
    pesquisa = request.GET['pesquisa']
    return render(request, 'pesquisa_listagem.html', {'pesquisa': pesquisa, "object_list": queryset})


class RegistroListViewAll(ListView):
    model = Registro
    template_name = 'registro_listagem_all.html'


class RegistroListView(LoginRequiredMixin, ListView):
    template_name = 'registro_listagem.html'
    login_url = 'login'

    def get_queryset(self):
        return Registro.objects.all()  # object_list


class RegistroDetailView(DetailView):
    model = Registro
    template_name = 'registro_detail.html'
    login_url = 'login'


class RegistroUpdateView(LoginRequiredMixin, UpdateView):
    model = Registro
    fields = ('nome_popular', 'nome_cientifico', 'especie', 'altura_max', 'diametro', 'bairro', 'local', 'clima', 'regiao',
              'origem', 'latitude', 'longitude', 'extincao', 'desc', 'image')
    template_name = 'registro_edicao.html'
    success_url = reverse_lazy('registro_list_all')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class RegistroCommentView(LoginRequiredMixin, CreateView):
    model = Comentario
    fields = ('comentario',)
    template_name = 'registro_comentario.html'
    success_url = reverse_lazy('registro_list_all')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.autor = self.request.user
        form.instance.registro_id = self.kwargs['pk']
        return super().form_valid(form)


class RegistroDeleteView(LoginRequiredMixin, DeleteView):
    model = Registro
    template_name = 'registro_delecao.html'
    success_url = reverse_lazy('registro_list_all')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class RegistroCreateView(LoginRequiredMixin, CreateView):
    model = Registro
    template_name = 'registro_novo.html'
    fields = ('nome_popular', 'nome_cientifico', 'especie', 'altura_max', 'diametro', 'bairro', 'local', 'clima', 'regiao',
              'origem', 'latitude', 'longitude', 'extincao', 'desc', 'image')
    success_url = reverse_lazy('home')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.doador = self.request.user
        form.save()
        return super().form_valid(form)


class ComentarioDeleteView(LoginRequiredMixin, DeleteView):
    model = Comentario
    template_name = 'comentario_delecao.html'
    success_url = reverse_lazy('registro_list_all')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
