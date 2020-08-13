from django.db import models

class Articles(models.Model):
    title=models.CharField(max_length=120)
    content= models.TextField()

    def ___str___(self):
        return self.title