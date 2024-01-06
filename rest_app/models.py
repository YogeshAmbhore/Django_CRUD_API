from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=230, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    country_code_choices = [
        ('GB', 'United Kingdom'),
        ('US', 'United States'),
        ('IN', 'INDIA'),
    ]
    country_code = models.CharField(max_length=2, choices=country_code_choices, default='IN')

    def __str__(self):
        return self.name

