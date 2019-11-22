# Register your models here.
from django.contrib import admin
from django.contrib.admin.templatetags.admin_list import date_hierarchy
from django.contrib.admin.views.main import ChangeList
from django.db.models import Count
from django.db.models.functions import TruncDay
from .models import EmailSubscriber


@admin.register(EmailSubscriber)
class EmailSubscriberAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "created_at") # display these table columns in the list view
    ordering = ("-created_at",) 
    date_hierarchy= ('created_at')
    change_list_template= 'pages/admin/change_liste_dataemail.html'
    
    def changelist_view(self, request, extra_context=None):
    # Aggregate new subscribers per day
        chart_data = (
            EmailSubscriber.objects.annotate(date=TruncDay("created_at"))
            .values("date")
            .annotate(nombre_email=Count("id"))
            .order_by("-date")
        )
        data={
            "chart_data": chart_data,
            'nom':'Hans'
        }
        print(chart_data)
        extra_context = extra_context or data
        return super().changelist_view(request, extra_context=extra_context)