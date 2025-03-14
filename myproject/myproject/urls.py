"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from myapp.views import cost_calculator_view, generate_agora_token, home, video_call
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('blog/', include('myapp.urls')),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login पर JWT Token मिलेगा
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh Token

    path('cost-calculator/', cost_calculator_view, name='cost_calculator'),
    path('get-token/<str:channel_name>/', generate_agora_token, name='get-agora-token'),
    path('video-call/', video_call, name='video-call'),
]



