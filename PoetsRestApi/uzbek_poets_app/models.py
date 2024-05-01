from django.contrib.admin import ModelAdmin
from django.contrib.auth import get_user_model
from django.db import models


class PoetsModel(models.Model):
    poet_name = models.CharField(max_length=255)
    poet_description = models.CharField(max_length=255)
    poet_image = models.ImageField(upload_to='poet_images')
    poet_about = models.TextField()
    poet_birthdate = models.CharField(max_length=11)
    poet_dead_date = models.CharField(max_length=11)
    poet_user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.poet_name

    class Meta:
        verbose_name_plural = 'Poets'
        db_table = 'poets'


class PoemsModel(models.Model):
    poem_name = models.CharField(max_length=255)
    poem_poem = models.TextField()
    poem_written_time = models.CharField(max_length=11, default='unknown')
    poem_poet_id = models.ForeignKey(PoetsModel, on_delete=models.CASCADE)
    poem_user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    search_field = ('poem_name',)

    def __str__(self):
        return self.poem_name

    class Meta:
        verbose_name_plural = 'Poems'
        db_table = 'poems'


class PoetAdmin(ModelAdmin):
    list_display = ('poet_name', 'poet_description', 'poet_user_id')
    search_fields = ('poet_name', 'poet_description')


class PoemAdmin(ModelAdmin):
    list_display = ('poem_name', 'poem_poet_id', 'poem_user_id')
    search_fields = ('poem_name', )
