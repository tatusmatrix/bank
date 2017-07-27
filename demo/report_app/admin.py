from django.contrib import admin

from report_app.models import MyReport, MyReportNew, SeriousBank
# Register your models here.

admin.site.register(MyReport)
admin.site.register(MyReportNew)
admin.site.register(SeriousBank)

