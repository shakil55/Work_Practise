from django.db import models

class Tool(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50)
    pricing = models.CharField(max_length=50)
    rating = models.FloatField()
    link = models.URLField()
    image = models.ImageField(upload_to='tool_images/')
    tags = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

