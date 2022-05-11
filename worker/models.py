
from django.db import models
from django.contrib.auth.models import User
  
status=[
    ('active','Active'),
    ('accepted','Accepted'),
    ('completed','Completed'),
    ('cancel','Cancel')
]

    
    
class Exercises(models.Model):
    title = models.TextField()
    start_date = models.DateField(auto_now_add=True)
    dedline = models.DateField()
    status = models.CharField(max_length=50, choices=status, default='active')
    
    def __str__(self):
        return self.title
    
    
class Worker(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, blank=True,null=True)
    position = models.CharField(max_length=200)
    birth_date = models.DateField()
    def __str__(self):
        return str(self.name)
    
    
class Work_table(models.Model):
    worker_id = models.ForeignKey(Exercises, on_delete=models.CASCADE)
    name_id = models.ForeignKey(Worker, on_delete=models.CASCADE)
    title = models.TextField(null=True, blank=True)
    
    
    def __str__(self):
        return str(self.name_id)
    
    

    

    
    
    
    

