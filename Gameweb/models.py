from django.db import models

class Game(models.Model) :
    title = models.CharField(blank=False,default='Prosze podać tytuł',max_length=40,null=True)
    kind = models.CharField(blank=True,max_length=10,null=True)
    realese_date = models.DateField(blank=True,null=True)
    text = models.TextField(blank=True,null=True)
    iko = models.ImageField(upload_to='icons',blank=True,null=True)
    metacritick_rating = models.DecimalField(default=5,blank =True,max_digits=4,decimal_places=2,null=True)
    platform = models.TextField(max_length=100, default='PC',null=True)

    def __str__(self):
        return self.title + ' ({})'.format(self.realese_date)
