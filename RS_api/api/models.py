from django.db import models


class DateManage(models.Model):
    created_at=models.DateTimeField(
        verbose_name="登録時間",
        auto_now_add=True,
    )
    date = models.DateField(
        verbose_name="日時",
    )
    start_time = models.DateTimeField(
        verbose_name="開始時間",
    )
    end_time = models.DateTimeField(
        verbose_name="終了時間",
    )
    # press_ave_3min=models.FloatField(
    #     verbose_name="圧力センサ値",
    #     blank=True
    # )
    # work_or_sabori=models.FloatField(
    #     verbose_name="勤怠状況",
    #     blank=True
    # )

    def __str__(self):
        return self.date

