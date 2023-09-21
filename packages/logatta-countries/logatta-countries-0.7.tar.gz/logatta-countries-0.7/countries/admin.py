from django.contrib import admin

# Register your models here.
from .models import City,Country,Nationality


class CityInline(admin.TabularInline):
    model = City
    extra = 1


class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country_code','name_ar')
    search_fields = ('id', 'name', 'country_code','name_ar')
    ordering = ['name']
    inlines = [CityInline]
    

class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','name_ar', 'get_country_name')
    search_fields = ('id', 'name', 'country__name','name_ar')
    
    def get_country_name(self, obj):
        return obj.country.name


class NationalityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','name_ar')
    search_fields = ('id', 'name','name_ar')
    ordering = ['name']
    

admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Nationality, NationalityAdmin)