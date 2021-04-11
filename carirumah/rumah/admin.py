from django.contrib import admin

from .models import Rumah, Source, ImageLink, Developer, Agent

# Register your models here.
class RumahAdmin(admin.ModelAdmin):
    list_display = ['property_name', 'address','price','LT','LB']
    class Meta:
        model = Rumah

class SourceAdmin(admin.ModelAdmin):
    list_display = ['name','url']
    class Meta:
        model = Source

class ImageLinkAdmin(admin.ModelAdmin):
    list_display = ['property_name','url']
    class Meta:
        model = ImageLink

class DeveloperAdmin(admin.ModelAdmin):
    list_display = ['name','contact']
    class Meta:
        model = Developer

class AgentAdmin(admin.ModelAdmin):
    list_display = ['name','contact']
    class Meta:
        model = Agent

admin.site.register(Rumah,RumahAdmin)
admin.site.register(Source,SourceAdmin)
admin.site.register(ImageLink,ImageLinkAdmin)
admin.site.register(Developer,DeveloperAdmin)
admin.site.register(Agent,AgentAdmin)