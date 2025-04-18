from django.db import models


ACCESS_SELECT = (
    ("US", "کارمند"),
    ("MO", "مدیریت"),
)

class PersonelModel(models.Model):
    first_name = models.CharField(verbose_name="نام", max_length=50)
    last_name = models.CharField(verbose_name="نام خانوادگی", max_length=50)
    phone_number = models.CharField(verbose_name="شماره موبایل", max_length=11,unique=True)
    person_code = models.CharField(verbose_name="کد پرسنلی", max_length=50)
    password = models.CharField(verbose_name='رمز', max_length=50)
    access = models.CharField(verbose_name="سطح دسترسی", max_length=2,choices=ACCESS_SELECT)

    class Meta:
        verbose_name = "پرسنل"
        verbose_name_plural = "پرسنل"

    def __str__(self):
        return str(self.person_code)