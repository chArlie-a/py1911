from django.db import models


# Create your models here.
class Issue(models.Model):
    title = models.CharField(max_length=20)
    option1_votes = models.IntegerField(default=0, verbose_name='选项1票数')
    option2_votes = models.IntegerField(default=0, verbose_name='选项2票数')
    option3_votes = models.IntegerField(default=0,null=True, blank=True, verbose_name='选项3票数')
    option4_votes = models.IntegerField(default=0,null=True, blank=True, verbose_name='选项4票数')

    def __str__(self):
        return self.title


class Option(models.Model):
    option1 = models.CharField(max_length=20, default='是', unique=True)
    option2 = models.CharField(max_length=20, default='不是', unique=True)
    option3 = models.CharField(max_length=20, null=True, blank=True, unique=True)
    option4 = models.CharField(max_length=20, null=True, blank=True, unique=True)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='issues')
