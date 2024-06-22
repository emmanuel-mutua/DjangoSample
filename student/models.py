from django.db import models
class Student(models.Model):
    first_name =models.CharField(max_length=20)
    last_name =models.CharField(max_length=20)
    email =models.EmailField()
    code = models.PositiveSmallIntegerField()
    date_of_birth = models.DateField()
    country = models.CharField(max_length=20)
    bio = models.TextField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

# Create your models here.
# class Class(models.Model):
#     class_id = models.PositiveSmallIntegerField()
#     class_number = models.PositiveSmallIntegerField()
#     class_trainer_name = models.CharField(max_length=20)
#     class_location = models.CharField(max_length=20)
#     class_capacity = models.PositiveSmallIntegerField()
#     class_level = models.CharField(max_length=20)
#     class_name = models.CharField(max_length=15)
#     class_days = models.PositiveSmallIntegerField()
#     class_student_names = models.TextField()
#     class_course = models.CharField(max_length=25)
#     def __str__(self):
#         return f"{self.class_id} {self.class_capacity}"
    

# class Course(models.Model):
#     name = models.CharField(max_Length = 20)
#     description = models.CharField()
#     location = models.CharField()
#     course_type = models.CharField(max_Length = 20)
#     course_duration = models.IntegerField()
#     course_level = models.CharField()
#     course_fee = models.IntegerField()
#     course_trainer = models.CharField()
#     course_students = models.IntegerField()
#     course_date = models.DateField()
#     def __str__(self):
#         return f"{self.name}{self.name}"


# class Teacher(models.Model):
#     teacher_id = models.PositiveSmallIntegerField()
#     teacher_first_name = models.CharField(max_length=20)
#     teacher_email = models.EmailField()
#     phone_number = models.CharField(max_length=20)
#     department = models.CharField(max_length=20)
#     photo = models.ImageField()
#     experience = models.CharField(max_length=20)
#     teacher_last_name = models.CharField(max_length=20)
#     date_of_birth = models.DateField()
#     salary = models.PositiveSmallIntegerField()
#     def __str__(self):
#         return f"{self.teacher_id} {self.teacher_last_name}"
















      


