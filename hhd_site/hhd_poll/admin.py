from django.contrib import admin

# Register your models here.
from .models import Question
from .models import Choice
from .models import *

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(HHD_db)
