# Registros/urls.py
from django.urls import path
from .views import RegistroListView, RegistroUpdateView, RegistroDetailView, RegistroDeleteView, RegistroCreateView,\
	RegistroCommentView, ComentarioDeleteView, RegistroListViewAll, pesquisa_list_view


urlpatterns = [
	path('<int:pk>/edit/', RegistroUpdateView.as_view(), name='registro_edit'),
	path('<int:pk>/', RegistroDetailView.as_view(), name='registro_detail'),
	path('<int:pk>/delete/', RegistroDeleteView.as_view(), name='registro_delete'),
	path('', RegistroListView.as_view(), name='registro_list'),
	path('list/', RegistroListViewAll.as_view(), name='registro_list_all'),
	path('new/', RegistroCreateView.as_view(), name='registro_new'),
	path('<int:pk>/comentario/', RegistroCommentView.as_view(), name='registro_comment'),
	path('<int:pk>/comentario/delete/', ComentarioDeleteView.as_view(), name='comment_delete'),
	path('search/', pesquisa_list_view, name='search_list')
]
