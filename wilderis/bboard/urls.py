from django.urls import path
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from .views import MainView,RegisterView,ProductView,DetView

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('reg/', RegisterView.as_view(), name='reg'),
    path('prod/', ProductView.as_view(), name='product'),
    path('det/<int:pk>/', DetView.as_view(), name='detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
