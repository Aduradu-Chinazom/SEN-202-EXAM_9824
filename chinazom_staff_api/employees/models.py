from django.db import models

class StaffBase(models.Model):
    employeeNmae = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    salary = models.CharField(max_length=255)
    address = models.CharField(max_length=100)
    employmentDate = models.CharField(max_length=100)
    age = models.CharField(max_length=2)

    def get_role_label(self):
        return "Staff"

    def __str__(self):
        return f"{self.employeeNmae}, {self.role}, {self.salary}, {self.address}, {self.employmentDate}, {self.age}"

class Manager(StaffBase):
    department = models.CharField(max_length=255)
    has_company_card = models.BooleanField(default=True)

    def get_role_label(self):
        return "Manager"

    def __str__(self):
        return f"{self.employeeNmae}, {self.department}, {self.has_company_card}"

class Intern(StaffBase):
    has_company_card = models.BooleanField(default=True)
    internship_end = models.CharField(max_length=255)
    internship_start = models.CharField(max_length=255)
    mentor = models.OneToOneField(Manager, on_delete=models.CASCADE, related_name='intern_mentee')

    def get_role_label(self):
        return "Intern"

    def __str__(self):
        return f"{self.employeeNmae}, {self.internship_start}, {self.internship_end}, {self.has_company_card}, {self.mentor}"

#this are my superuser details
#username: Chinazom
#password: thefortchurch