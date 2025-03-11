from django.urls import path
from myapp.views import home
from myapp.apiview import student_list, student_detail,register_user

# from .apiviews import 

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(title="Student API", default_version='v1'),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', home),
    path('students/', student_list, name="student_list"),  # GET & POST
    path('students/<int:pk>/', student_detail, name="student_detail"),  # GET, PUT, DELETE 
    path('api/register/', register_user, name='register_user'),  # User Registration
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   
 
]