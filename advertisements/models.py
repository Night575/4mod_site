from django.db import models
from django.contrib import admin
from django.utils.html import format_html


class Advertisement(models.Model):
    title = models.CharField(max_length=80, verbose_name="заголовок")
    description = models.TextField("описание")
    price = models.DecimalField("цена", max_digits=12, decimal_places=2)
    auction = models.BooleanField("возможность торга", help_text="Отметьте, если торг уместен")
    created_at = models.DateTimeField("дата создания", auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @admin.display(description="Дата создания")
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M")
            return format_html("<span style='color: red'>Сегодня в {}</span>", created_time)
        return self.created_at

    @admin.display(description="Дата обновления")
    def update_date(self):
        from django.utils import timezone
        if self.updated_at.date() == timezone.now().date():
            update_time = self.updated_at.time().strftime("%H:%M")
            return format_html("<span style='color: orange'>Сегодня в {}</span>", update_time)
        return self.updated_at

    class Meta:
        db_table = 'advertisements'
        verbose_name_plural = "Объявления"

    def __str__(self):
        return f'<Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price})>'
