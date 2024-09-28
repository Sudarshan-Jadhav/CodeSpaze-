from django.db import models

class ScriptedData(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=200)
    content = models.TextField()
    scripted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

