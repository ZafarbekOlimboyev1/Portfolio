from django.contrib.auth import get_user_model
from django.db import models
from ckeditor.fields import RichTextField


class SubsystemsModel(models.Model):
    sub_code = models.CharField(max_length=10)
    sub_name = models.CharField(max_length=255)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.sub_name

    class Meta:
        db_table = 'Subsystems'
        verbose_name_plural = 'Subsystems'


class GroupsModel(models.Model):
    group_number = models.CharField(max_length=10)
    group_name = models.CharField(max_length=255)
    sub_id = models.ForeignKey(SubsystemsModel, on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.group_name

    class Meta:
        db_table = 'Groups'
        verbose_name_plural = 'Groups'


class DocumentTypesModel(models.Model):
    doc_type = models.CharField(max_length=255)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.doc_type

    class Meta:
        db_table = 'doc_types'
        verbose_name_plural = 'DocTypes'


class DocumentsModel(models.Model):
    doc_code = models.CharField(max_length=10)
    doc_title = models.CharField(max_length=255)
    doc_file = models.FileField(upload_to='docs/%y/%m/%d/')
    doc_type_id = models.ForeignKey(DocumentTypesModel, on_delete=models.CASCADE)
    doc_group_id = models.ForeignKey(GroupsModel, on_delete=models.CASCADE)
    doc_time = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.doc_title

    class Meta:
        db_table = 'documents'
        verbose_name_plural = 'Documents'


class DocumentPartsModel(models.Model):
    part_title = models.CharField(max_length=255)
    part_text = RichTextField(null=True)
    part_doc_id = models.ForeignKey(DocumentsModel, on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.part_title

    class Meta:
        db_table = 'document_parts'
        verbose_name_plural = 'Documnet Parts'


class DocumentPlanModel(models.Model):
    plan_title = models.CharField(max_length=255)
    plan_text = RichTextField(null=True)
    plan_doc_id = models.ForeignKey(DocumentsModel, on_delete=models.CASCADE)
    plan_part_id = models.ForeignKey(DocumentPartsModel, on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    plan_subplan = models.BooleanField(default=False)

    def __str__(self):
        return self.plan_title

    class Meta:
        db_table = 'doc_plans'
        verbose_name_plural = 'DouPlans'


class DocumentSubPlansModel(models.Model):
    subplan_title = models.CharField(max_length=255)
    subplan_text = RichTextField()
    doc_plan_id = models.ForeignKey(DocumentPlanModel, on_delete=models.CASCADE)
    doc_id = models.ForeignKey(DocumentsModel, on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.subplan_title

    class Meta:
        db_table = 'doc_subplans'
        verbose_name_plural = 'DocSubPlans'


class DictionaryModel(models.Model):
    dict_code = models.CharField(max_length=50)
    dict_uz = models.CharField(max_length=255)
    dict_tr = models.CharField(max_length=255)
    dict_eng = models.CharField(max_length=255)
    dict_ru = models.CharField(max_length=255)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.dict_uz

    class Meta:
        db_table = 'dictionary'
        verbose_name_plural = 'Dictionary'
