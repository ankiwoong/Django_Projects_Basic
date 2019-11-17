from django.contrib import admin
from .models import Fcuser

# Register your models here.

class FcuserAdmin(admin.ModelAdmin):
    # 사용자명 / 비밀번호 확인
    list_display = ('username', 'password')

admin.site.register(Fcuser, FcuserAdmin)