
from . import views
from django.urls import path

urlpatterns = [
   
    path('',views.signup),
    path('register/',views.create_user, name="signup"),
    path('login/', views.login),
    path('login_request/',views.login_request, name='login_request'),
    path('table/',views.data, name="index_data"),
    path('deleteuser/', views.deleteuser, name="delete_user_info"),
    path('searchdata/',views.searchdata, name="index"),
    path('show_all_data/',views.show_all_data),
    path('updateuser/',views.updateuser),
    
]
