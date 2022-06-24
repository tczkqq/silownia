from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Statistics)
admin.site.register(models.Service)
admin.site.register(models.PaymentMethods)
admin.site.register(models.Messages)
admin.site.register(models.Visits)
admin.site.register(models.Payments)
admin.site.register(models.UserService)
