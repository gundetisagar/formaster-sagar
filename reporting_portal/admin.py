from django.contrib import admin
from reporting_portal.models import (
    Category,
    SubCategory
)


admin.site.register(Category)
admin.site.register(SubCategory)
