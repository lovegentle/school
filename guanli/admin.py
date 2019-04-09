from django.contrib import admin

# Register your models here.
from django.contrib import admin



class ss(admin.ModelAdmin):
    list_display = ('xuehao', 'xingming', 'age')  # 页面显示


# list_editable = ('xingming','age')     #直接修改
# filter_horizontal = ('age',)
# list_per_page = 2       #分页
# search_fields = ('xuehao','xingming')      #查询
# list_filter = ('age','xuehao')             #辅助过滤查询
#admin.site.register(student, ss)
#admin.site.register(teacher)
#admin.site.register(login)