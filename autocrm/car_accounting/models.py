from django.db import models

# Create your models here.


class Marks(models.Model):
    mark = models.CharField(max_length=100, unique=True, blank=False)

    class Meta:
        db_table = 'marks'


class Models(models.Model):
    mark = models.ForeignKey(Marks, to_field='mark', on_delete=models.CASCADE)
    model = models.CharField(max_length=100, unique=True, blank=False)

    def __str__(self):
        return f'{self.mark} {self.model}'

    class Meta:
        db_table = 'models'


class Cars(models.Model):
    reg_num = models.CharField(max_length=9, unique=True)
    model = models.ForeignKey(Models, on_delete=models.PROTECT)
    release_year = models.IntegerField()

    def __str__(self):
        return self.reg_num

    class Meta:
        db_table = 'cars'
