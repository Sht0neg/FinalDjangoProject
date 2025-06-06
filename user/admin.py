from django.contrib import admin
from user.models import *
from vacancy.models import *

admin.site.register(Profile)
admin.site.register(Vacancy)