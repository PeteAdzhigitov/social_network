from django.urls import path, include
# from .views import dashboard
from rest_framework import routers
from .views import *
app_name = 'dwitter'

# router = routers.SimpleRouter()
# router.register(r'dweets', DweetViewSet, basename="dweets")
# print(router.urls)

urlpatterns = [
    path('',DashboardList.as_view(),name='dashboard'),
    path('profile_list/',ProfileListView.as_view(),name='profile_list'),
    path('profile/<int:pk>',ProfileDetailView.as_view(),name='profile'),
    path('profile_update/<int:pk>',ProfileUpdateView.as_view(), name='profile_update'),
    path('dweet_delete/<int:pk>',DweetDeleteView.as_view(), name='dweet_delete'),
    path('dweet_update/<int:pk>',DweetUpdateView.as_view(), name='dweet_update'),
    path('api/v1/profiles_list',ProfilesAPIList.as_view() ),
    # path('api/v1/', include(router.urls))
    # path('api/v1/dweets_list',DweetViewSet.as_view({"get":"list"}) ),
    path('api/v1/dweets_list/<int:pk>/',DweetUpdateAPIView.as_view() )
]