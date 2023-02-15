from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
  # tuple
  USER = (
    (1, 'HOD'),
    (2, 'STAFF'),
    (3, 'STUDENT'),
  )
  user_type = models.CharField(choices=USER, max_length=50, default=1)
  profile_Pic = models.ImageField(upload_to='media/profilePic')


class Course(models.Model):
  objects = None
  course_name = models.CharField(max_length=100)
  create_date = models.DateTimeField(auto_now_add=True)
  update_date = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return self.course_name


class SessionYear(models.Model):
  objects = None
  session_start = models.CharField(max_length=50)
  session_end = models.CharField(max_length=50)
  
  def __str__(self):
    return self.session_start + "-" + self.session_end


class Student(models.Model):
  # it will delete the (Student) from admin as well as from students Model
  objects = None
  admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
  address = models.TextField()
  gender = models.CharField(max_length=100)
  # it will only delete the (Course) from students Model not from admin
  course_id = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
  session_year_id = models.ForeignKey(SessionYear, on_delete=models.DO_NOTHING)
  create_date = models.DateTimeField(auto_now_add=True)
  update_date = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return self.admin.first_name + " " + self.admin.last_name


class Staff(models.Model):
  objects = None
  admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
  address = models.TextField()
  gender = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return self.admin.first_name + " " + self.admin.last_name
