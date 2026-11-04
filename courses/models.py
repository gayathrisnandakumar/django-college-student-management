from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=100)
    course=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='student_photos/',null=True,blank=True)
    def __str__(self):
        return self.name
