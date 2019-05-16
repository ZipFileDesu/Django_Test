from django.contrib import admin
from django.http import HttpResponse, request

from .models import Question
from .models import Choice

admin.site.register(Question)
admin.site.register(Choice)

