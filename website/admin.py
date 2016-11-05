from django.contrib import admin

# Register your models here.
from .models import Patient, Doctor, Rx, Note, Case, Adherence

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Rx)
admin.site.register(Note)
admin.site.register(Case)
admin.site.register(Adherence)