from django.db import models


class Swiped(models.Model):
    '''滑动记录'''
    STATUS = (
        ('superlike', '超级喜欢'),
        ('like', '喜欢'),
        ('dislike', '不喜欢'),
    )

    uid = models.IntegerField(verbose_name='滑动者的 UID')
    sid = models.IntegerField(verbose_name='被滑动者的 UID')
    status = models.CharField(max_length=8, choices=STATUS)
    time = models.DateTimeField(auto_now_add=True)


class Friend(models.Model):
    '''好友'''
    uid1 = models.IntegerField()
    uid2 = models.IntegerField()
