from django.db import models

class StaffBase(models.Model):
    employeeNmae = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    salary = models.CharField(max_length=255)
    address = models.CharField(max_length=100)
    employmentDate = models.CharField(max_length=100)
    age = models.CharField(max_length=2)
    
    def __str__(self):
        return f"{self.employeeNmae}, {self.role}, {self.salary}, {self.address}, {self.employmentDate}, {self.age},"
    
class Manager(StaffBase):
    department = models.CharField(max_length=255)
    has_company_card = models.BooleanField(default=True)
    staffBase= models.OneToOneField(StaffBase, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.department}, {self.has_company_card}, {self.staffBase},"
    
class Intern(StaffBase):
    has_company_card = models.BooleanField(default=True)
    internship_end = models.CharField(max_length=255)
    internship_start = models.CharField(max_length=255)
    staffBase = models.OneToOneField(StaffBase, on_delete=models.CASCADE)
    mentor = models.OneToOneField(Manager, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.internship_end}, {self.internship_start}, {self.has_company_card}, {self.staffBase}, {self.mentor},"
