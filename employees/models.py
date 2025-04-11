from django.db import models
from django.utils.timezone import now

class Role(models.Model):
    title = models.CharField(max_length=50)
    rank = models.PositiveIntegerField(help_text="Lower numbers are higher in the hierarchy (e.g., CEO=1)")
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

class ContactInfo(models.Model):
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    postal_code = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.ForeignKey(Role, on_delete=models.PROTECT)
    manager = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='subordinates')
    contact_info = models.OneToOneField(ContactInfo, null=True, blank=True, on_delete=models.SET_NULL)
    date_joined = models.DateField()
    last_promotion_date = models.DateField(null=True, blank=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=50, choices=[('active', 'Active'), ('on_leave', 'On Leave'), ('terminated', 'Terminated')])

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    # def save(self, *args, **kwargs):
    #     is_new = self.pk is None
    #     if not is_new:
    #         old = self.__class__.objects.get(pk=self.pk)
    #         if old.role != self.role:
    #             EmployeeRoleHistory.objects.filter(
    #                 employee=self,
    #                 end_date__isnull=True
    #             ).update(end_date=now().date())

    #             EmployeeRoleHistory.objects.create(
    #                 employee=self,
    #                 role=self.role,
    #                 start_date=now().date()
    #             )
    #     super().save(*args, **kwargs)  # Save once, always

    #     if is_new:
    #         EmployeeRoleHistory.objects.create(
    #             employee=self,
    #             role=self.role,
    #             start_date=now().date()
    #         )

class EmployeeRoleHistory(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name='role_history')
    role = models.ForeignKey('Role', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['-start_date']  # Optional: show most recent roles first

    def __str__(self):
        return f"{self.employee.first_name} {self.employee.last_name} - {self.role.title} ({self.start_date} to {self.end_date or 'Present'})"

