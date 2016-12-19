from django.contrib import admin
from ticketsystem.models import Product,Priority,Ticket,Status

# Register your models here.

#admin.site.register(Product)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['name','department',]
    list_filter=['department',]
    search_fields=['department__name',]
    

@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    pass



@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display=['title','creator','priority','status','create_date',]
    list_filter=['priority',]
    search_fields=['creator__user__username','title',]

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    pass