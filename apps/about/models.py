from django.db import models
from django.urls import reverse

class About(models.Model):
    first_txt = models.CharField(max_length=200)
    second_txt = models.CharField(max_length=200)
    third_txt = models.CharField(max_length=200)
    fourth_txt = models.CharField(max_length=200)
    fifth_txt = models.CharField(max_length=200)
    modified_date = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('first_txt', args=[self.first_txt])

    def __str__(self):
        return self.first_txt
    
    class Meta:
        # Piirangu, et saab luua ainult üks kirje
        constraints = [
            models.UniqueConstraint(fields=['first_txt', 'second_txt', 'third_txt', 'fourth_txt', 'fifth_txt'], name='unique_fields')
        ]