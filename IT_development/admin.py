from django.contrib import admin
from .models import (
    ContactRequest,
    Founder,
    Project,
    Service,
    TeamMember,
    Logo
)

admin.site.register(ContactRequest)
admin.site.register(Service)
admin.site.register(Founder)
admin.site.register(Project)
admin.site.register(TeamMember)
admin.site.register(Logo)