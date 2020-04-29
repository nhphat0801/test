from django.contrib import admin
from .models import Herb, Compound, Target
# Register your models here.
admin.site.register(Herb)
admin.site.register(Compound)
admin.site.register(Target)