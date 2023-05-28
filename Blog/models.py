from django.db import models

# Create your models here.
class Blog(models.Model):
    image = models.ImageField(upload_to='uploads/images', null=True, blank=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
