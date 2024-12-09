from django.urls import path
from core import views
urlpatterns = [

    path('',views.index , name = "index"),
    path('signup/',views.signup, name="signup"),
    path('signin/',views.SigninView.as_view(), name="signin"),
    path('logout/',views.LogoutView.as_view(),name="logout"),
    #path('logout/',views.Logout,name="logout"),
    path('settings/', views.SettingView.as_view(),name="settings"),
    path('upload/', views.UploadPost,name="upload"),

]