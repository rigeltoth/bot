from django.db import models

class Bot(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  name = models.CharField(max_length=200)
  resolution = models.IntegerField()
  scale = models.FloatField()
  voxel_size = models.FloatField()
  
  def __str__(self):
    return self.name
