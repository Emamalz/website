from django.contrib import admin
from .models import Team, HealthCheckEntry

admin.site.register(Team)
admin.site.register(HealthCheckEntry)
