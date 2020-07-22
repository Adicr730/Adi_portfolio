from django.db import models

class Blog(models.Model):
    title=models.CharField(max_length=200)
    date=models.DateField()
    text=models.TextField()
    url = models.URLField(blank=True)
    
    def __str__(self):
        return self.title