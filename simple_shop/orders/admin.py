import csv
import datetime

from django.contrib import admin
# Register your models here.
from django.http import HttpResponse
from django.urls import reverse
from django.utils.html import format_html
from orders.models import OrderItem, Order


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_field = ['product']
    extra = 0


def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; \
        filename=Orders-{}.csv'.format(datetime.datetime.now().strftime("%d/%m/%Y"))
    writer = csv.writer(response)

    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    # Первая строка- оглавления
    writer.writerow([field.verbose_name for field in fields])
    # Заполняем информацией
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response


export_to_csv.short_description = 'Экспорт в CSV'


def order_details(obj):
    """
    Подробнее о заказе

    :param obj:
    :return:
    """
    return format_html('<a href="{}">Посмотреть</a>'.format(reverse('orders:AdminOrderDetail', args=[obj.id])))


order_details.short_description = 'Детали заказа'


class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'city', 'paid', 'updated', order_details]
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]

    actions = [export_to_csv]


admin.site.register(Order, OrderAdmin)
