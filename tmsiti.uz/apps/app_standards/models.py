from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from ..app_NLS.models import LeadershipModel


class StandardTypesModel(models.Model):
    standard_type = models.CharField(max_length=255)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.standard_type

    class Meta:
        db_table = 'StandardsTypes'
        verbose_name_plural = 'StandardsTypes'


class ElectronicStandardTypesModel(models.Model):
    electronic_standard_type = models.CharField(max_length=255)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.electronic_standard_type

    class Meta:
        db_table = 'ElectronicStandardsTypes'
        verbose_name_plural = 'Electronic Standards Types'


class StandardsModel(models.Model):
    standard_type = models.ForeignKey(StandardTypesModel, on_delete=models.CASCADE)
    standard_code = models.CharField(max_length=55)
    standard_description = models.CharField(max_length=255)
    standard_text = RichTextField(null=True)
    standard_file = models.FileField(upload_to='Standards/%y/%m/%d/', null=True)
    standard_year = models.CharField(max_length=15)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.standard_type} {self.standard_code}'

    class Meta:
        db_table = 'standards'
        verbose_name_plural = 'standards'


class ElectronicStandardsModel(models.Model):
    standard_type = models.ForeignKey(ElectronicStandardTypesModel, on_delete=models.CASCADE)
    standard_code = models.CharField(max_length=55)
    standard_description = models.CharField(max_length=255)
    standard_text = RichTextField(null=True)
    standard_file = models.FileField(upload_to='Standards/%y/%m/%d/', null=True)
    standard_year = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.standard_type} {self.standard_code}'

    class Meta:
        db_table = 'electronic_standards'
        verbose_name_plural = 'Electronic Standards'


class BuildingRegulationsModel(models.Model):
    doc_number = models.IntegerField()
    doc_type = models.CharField(max_length=20)
    doc_code = models.CharField(max_length=20)
    doc_title = models.CharField(max_length=255)
    doc_text = RichTextField()
    doc_file = models.FileField(upload_to='BuildingRegulations/%y/%m/%d/', null=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.doc_title

    class Meta:
        db_table = 'building_regulations'
        verbose_name_plural = 'Building Regulations'


class MessagesModel(models.Model):
    msg_fio = models.CharField(max_length=255)
    msg_email = models.EmailField()
    msg_phone_number = models.CharField(max_length=20)
    msg_management = models.ForeignKey(LeadershipModel, on_delete=models.CASCADE)
    msg_text = models.TextField()

    def __str__(self):
        return self.msg_fio

    class Meta:
        db_table = 'messages'
        verbose_name_plural = 'Messages'
