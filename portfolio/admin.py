from django.contrib import admin
from .models import AboutMe, Experience, Education, Skill, Profile


@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'email', ]


admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Profile)
