from django.db import models

# Create your models here.

class ContactMessage(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    subject=models.CharField(max_length=200,blank=True)
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.email}"

class Education(models.Model):
    fulldegree=models.CharField(max_length=100)
    fullname=models.CharField(max_length=200)
    vname=models.CharField(max_length=100)
    subject= models.JSONField(default=list)
    text=models.TextField()
    degree=models.CharField(max_length=10)
    interested=models.JSONField(default=list)
    

    def __str__(self):
        return self.degree

class Skill(models.Model):
    no=models.CharField(max_length=2, default="01")
    shortname=models.CharField(max_length=5)
    fullname=models.CharField(max_length=50)
    text=models.TextField()

    def __str__(self):
        return self.shortname

class Project(models.Model):
    image=models.ImageField(upload_to="main/imange/",null=True,blank=True)
    complete=models.CharField(max_length=200)
    no=models.CharField(max_length=2,default="01")
    fullname=models.CharField(max_length=60)
    text=models.TextField()
    tech=models.JSONField(default=list)
    github = models.URLField(blank=True, null=True)
    live_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.fullname

    



