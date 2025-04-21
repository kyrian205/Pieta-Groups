from django.db import models

# Complaint Model
class Complaint(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    date_submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Complaint from {self.name}'

# Admission Model
class Admission(models.Model):
    name = models.CharField(max_length=200)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    address = models.TextField()
    parent_name = models.CharField(max_length=200)
    parent_contact = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f'Admission for {self.name}'

# Result Model
class Result(models.Model):
    student_id = models.CharField(max_length=20, unique=True)
    subject_1 = models.CharField(max_length=100)
    subject_2 = models.CharField(max_length=100)
    subject_3 = models.CharField(max_length=100)
    subject_4 = models.CharField(max_length=100)
    subject_5 = models.CharField(max_length=100)
    total_score = models.IntegerField()

    def __str__(self):admin
        return f'Result for {self.student_id}'