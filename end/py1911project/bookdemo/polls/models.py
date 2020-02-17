from django.db import models


# Create your models here.
class Issue(models.Model):
    title = models.CharField(max_length=20, verbose_name='标题')
    creation_time = models.DateField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '问题'
        verbose_name_plural = verbose_name
        ordering = ['creation_time']

    def __str__(self):
        return self.title


class Option(models.Model):
    name = models.CharField(max_length=20, verbose_name='选项名称')
    votes = models.PositiveIntegerField(default=0, verbose_name='票数')
    creation_time = models.DateField(auto_now_add=True, verbose_name='创建时间')
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='issues', verbose_name='所选问题')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '选项'
        verbose_name_plural = verbose_name
        ordering = ['creation_time']
