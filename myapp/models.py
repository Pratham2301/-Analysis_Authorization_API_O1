from django.db import models

# Create your models here.

class Info(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100, unique=True)
    college=models.CharField(max_length=500)
    
    
class LoginInfoKey(models.Model):
    email=models.EmailField(max_length=100)
    college=models.CharField(max_length=500)
    key=models.CharField(max_length=500, unique=True)
    
    
class CollegeKey(models.Model):
    college=models.CharField(max_length=500)
    key=models.CharField(max_length=500, unique=True)


# {
#     "name" : "Pratham",
#     "email" : "rajbhojpr@rknec.edu",
#     "college" : "Rcoem"
# }

# {
#     "email" : "rajbhojpr@rknec.edu",
#     "college": "RCOEM",
#     "key" : "123"
# }