from django.db import models

class Post(models.Model):
    title =models.CharField(max_length=500)
    content = models.TextField()
    extract = models.CharField(max_length=1000)
    date_puh = models.DateTimeField()
    author = models.CharField(max_length=250, default ='lyneker')
    create_at =models.DateTimeField(auto_now_add=True)
