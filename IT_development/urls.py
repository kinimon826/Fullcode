from django.urls import path
from .views import (
    ContactRequestCreateView,
    ServiceListView,
    ProjectListView,
    FounderListView,
    TeamMemberListView,
    LogoListView,
    SiteSettingsListView,
)

urlpatterns = [
    path('contact/', ContactRequestCreateView.as_view(), name='contact-request-create'),
    path('services/', ServiceListView.as_view(), name='services-list'),
    path('projects/', ProjectListView.as_view(), name='projects-list'),
    path('founders/', FounderListView.as_view(), name='founders-list'),
    path('team/', TeamMemberListView.as_view(), name='team-list'),
    path('logos/', LogoListView.as_view(), name='logos-list'),
    path('site/', SiteSettingsListView.as_view(), name='site-settings-list'),
]