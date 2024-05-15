from django.db import models
from django.contrib.auth import get_user_model


class NewsModel(models.Model):
    news_title = models.CharField(max_length=255)
    news_description = models.CharField(max_length=500)
    news_text = models.TextField()
    news_image = models.ImageField(upload_to='news/%y/%m/%d/')
    news_datetime = models.DateTimeField(auto_now=True)
    news_status = models.BooleanField(default=False)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    search_filed = ('news_title', 'news_description', 'news_text')

    def __str__(self):
        return self.news_title

    class Meta:
        db_table = 'news'
        verbose_name_plural = 'news'


class LeadershipModel(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    reception_days = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    bachelor = models.CharField(max_length=50, null=True)
    master = models.CharField(max_length=50, null=True)
    doctoral = models.CharField(max_length=50, null=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    search_filed = ('name', )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'leadership'
        verbose_name_plural = 'leadership'


class AnnouncementsModel(models.Model):
    ann_title = models.CharField(max_length=255)
    ann_description = models.CharField(max_length=500)
    ann_text = models.TextField()
    ann_image = models.ImageField(upload_to='news/%y/%m/%d/', null=True)
    ann_datetime = models.DateTimeField(auto_now=True)
    ann_status = models.BooleanField(default=False)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    search_filed = ('ann_title', 'ann_description', 'ann_text')

    def __str__(self):
        return self.ann_title

    class Meta:
        db_table = 'announcements'
        verbose_name_plural = 'announcements'


class StructuralUnitsModel(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField()
    image = models.ImageField(upload_to='StructuralUnits/')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'StructuralUnits'
        verbose_name_plural = 'StructuralUnits'
