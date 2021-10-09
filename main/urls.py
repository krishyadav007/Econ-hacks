from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.home, name="home"),
    path('details/<int:id>/', views.detail, name="detail"),
    path('addInfras/', views.add_Infras, name="add_Infras"),
    path('editInfras/<int:id>/', views.edit_Infras, name="edit_Infras"),
    path('deleteInfras/<int:id>/', views.delete_Infras, name="delete_Infra"),
    path('addreview/<int:id>/', views.add_review, name="add_review"),
    path('editreview/<int:Infra_id>/<int:review_id>/', views.edit_review, name="edit_review"),
    path('deletereview/<int:Infra_id>/<int:review_id>/', views.delete_review, name="delete_review"),
    
]
