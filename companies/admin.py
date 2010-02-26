from pressroom.companies.models import Company, CompanyAdmin
from django.contrib import admin

admin.site.register(Company, CompanyAdmin)