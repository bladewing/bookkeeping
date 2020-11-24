from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('summary/', views.SummaryView.as_view(), name='summary'),
    path('new_single_entry/', views.EntryUpdateForm.as_view(), name='new_single_entry'),
    path('<int:pk>/edit/', views.edit_single_entry, name='edit_single_entry'),
    path('<pk>/delete/', views.EntryDeleteForm.as_view(), name='single_entry_delete'),
]
