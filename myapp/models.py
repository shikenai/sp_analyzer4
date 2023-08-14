from django.db import models


class GeneralSettings(models.Model):
    DEFAULT_DAYS = models.IntegerField(blank=True, verbose_name='画像描画時の取得日数')
    DEFAULT_LONG_MACD = models.IntegerField(blank=True, verbose_name='macd取得の長期スパン')
    DEFAULT_MIDDLE_MACD = models.IntegerField(blank=True, verbose_name='macd取得の中期スパン')
    DEFAULT_SHORT_MACD = models.IntegerField(blank=True, verbose_name='macd取得の短期スパン')