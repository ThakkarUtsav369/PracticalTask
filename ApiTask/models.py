from django.db import models

class BaseModel(models.Model):
    """
    An abstract base model containing common fields for other models.

    Attributes:
        created_at (DateTimeField): The date and time when the instance was created.
        updated_at (DateTimeField): The date and time when the instance was last updated.
        is_active (BooleanField): A flag indicating whether the instance is active or not.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Company(BaseModel):
    """
    A model representing a company.

    Attributes:
        name (CharField): The name of the company.
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Employee(BaseModel):
    """
    A model representing an employee.

    Attributes:
        first_name (CharField): The first name of the employee.
        last_name (CharField): The last name of the employee.
        phone_number (CharField, optional): The phone number of the employee.
        salary (DecimalField, optional): The salary of the employee.
        company (ForeignKey): The company to which the employee belongs.
    """
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name
