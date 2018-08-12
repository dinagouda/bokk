from django.contrib import admin

# Register your models here.
from bokk.models import children,political,poetry,artdesign,programing


admin.site.register(children)
admin.site.register(political)
admin.site.register(poetry)
admin.site.register(artdesign)
admin.site.register(programing)
