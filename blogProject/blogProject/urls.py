from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views  # <-- thêm dòng này

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),

    # Thêm login, logout:
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
