from django.db import models

class Geo(models.Model):
    name = models.CharField(max_length=25)

    def _str_(self): #show the actual geo name on the dashboard
        return self.name

    class Meta: #show Geo Locations Geo Locations of geo
        verbose_name_plural = 'Geo Locations'

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("weather_or_not", kwargs={"slug": str(self.slug)})
    