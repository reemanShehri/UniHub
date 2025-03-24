from django.contrib import admin
from .models import *  # استيراد النموذج

# تسجيل النموذج في واجهة الإدارة
admin.site.register(Post)
admin.site.register(University)
admin.site.register(Tag)
admin.site.register(Course)
admin.site.register(Board)
admin.site.register(Student)
admin.site.register(Reply)

admin.site.register(Notification)
admin.site.register(Announcement)
admin.site.register(Admin)