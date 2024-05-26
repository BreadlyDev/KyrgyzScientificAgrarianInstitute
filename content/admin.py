from django.contrib import admin
from . import models as m

admin.site.register(m.Book)
admin.site.register(m.Message)
admin.site.register(m.Module)


class SliderImageInline(admin.TabularInline):
    model = m.SliderImage
    extra = 1
    fields = ('image',)

    verbose_name = 'Изображение слайда'
    verbose_name_plural = 'Изображения слайдов'


class SliderAdmin(admin.ModelAdmin):
    inlines = [SliderImageInline]

    list_display = ('title', 'page')
    search_fields = ('title', 'page')
    list_filter = ('page',)

    class Meta:
        model = m.Slider


admin.site.register(m.Slider, SliderAdmin)
admin.site.register(m.SliderImage)
