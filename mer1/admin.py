from django.contrib import admin
from .models import bidzaiavka, Osavatel, project, Uslugi, Comanda, Logo

admin.site.register(bidzaiavka)
admin.site.register(Uslugi)
admin.site.register(Osavatel)
admin.site.register(project)
admin.site.register(Comanda)
admin.site.register(Logo)