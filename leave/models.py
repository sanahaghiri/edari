from django.db import models
from user.models import *
# Create your models here.

LEAVE_TYPES = (
    ('D', 'روزانه'),
    ('C', 'ساعتی'),
)


class LeaveModel(models.Model):
    user = models.ForeignKey(PersonelModel, verbose_name="کاربر", on_delete=models.CASCADE)
    days_or_clock = models.CharField(verbose_name="روزانه یا ساعتی",choices=LEAVE_TYPES, max_length=5)
    is_accept = models.BooleanField(default=False, verbose_name="تاییدیه")
    is_reject = models.BooleanField(default=False, verbose_name="رد کردن")
    clock_leave_date = models.DateTimeField(verbose_name="تاریخ مرخصی", auto_now=False, auto_now_add=False,blank=True,null=True)
    days_start_date = models.DateTimeField(verbose_name="تاریخ شروع", auto_now=False, auto_now_add=False,blank=True,null=True)
    days_end_date = models.DateTimeField(verbose_name="تاریخ پایان", auto_now=False, auto_now_add=False,blank=True,null=True)
    clock_start_time = models.CharField(
        verbose_name="ساعت شروع", max_length=10, null=True, blank=True
    )
    clock_end_time = models.CharField(
        verbose_name="ساعت پایان", max_length=10, null=True, blank=True
    )
    description = models.TextField(verbose_name="توضیحات", null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "مرخصی ها"
        verbose_name_plural = "مرخصی ها"

    def __str__(self):
        return self.user.first_name