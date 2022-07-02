from django.db import models

# Create your models here.


class Marks(models.Model):
    mark = models.CharField(max_length=100, unique=True, blank=False)

    def __str__(self):
        return self.mark

    class Meta:
        db_table = 'marks'


class Models(models.Model):
    model = models.CharField(max_length=100, unique=True, blank=False)

    def __str__(self):
        return self.model

    class Meta:
        db_table = 'models'


class Cars(models.Model):
    reg_num = models.CharField(max_length=9, unique=True)
    mark = models.ForeignKey(Marks, to_field='mark', on_delete=models.PROTECT)
    model = models.ForeignKey(Models, to_field='model', on_delete=models.PROTECT)
    release_year = models.IntegerField()
    owner_id = models.ForeignKey('accounts.CRMUser', to_field='username', on_delete=models.PROTECT)

    def __str__(self):
        return self.reg_num

    class Meta:
        db_table = 'cars'
