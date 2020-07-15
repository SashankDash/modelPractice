from django.contrib import admin
from myapp.models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
 list_display = ['eno','eaddr','ename','esal']


admin.site.register(Employee,EmployeeAdmin)
#admin.site.register(Employee)