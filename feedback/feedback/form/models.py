from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    student_name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.ForeignKey(Subject ,on_delete=models.CASCADE )
    details = models.TextField()
    happy = models.BooleanField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.student_name
    
#------------------------new change ------------------------------------
class Report(models.Model):
     title = models.CharField(max_length=100)
     description = models.TextField()
     cost = models.IntegerField()
     create_at = models.DateTimeField(auto_now_add=True)
     def __str__(self):
         return self.title
