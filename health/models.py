from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class HealthCheckEntry(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    card_title = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    comments = models.TextField(blank=True)
    actions = models.TextField(blank=True)
    solutions = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.team.name} - {self.card_title}"
