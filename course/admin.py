from django.contrib import admin

# Register your models here.
from .models import Ques,ValidUser
admin.site.register(Ques)
admin.site.register(ValidUser)
