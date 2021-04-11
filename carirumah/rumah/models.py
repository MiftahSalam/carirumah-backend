from django.db import models

# Create your models here.
class Developer(models.Model):
    name = models.CharField(max_length=60,blank=False,null=False,unique=True)
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Agent(models.Model):
    name = models.CharField(max_length=60)
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Source(models.Model):
    name = models.CharField(max_length=20,blank=False,null=False,unique=True)
    url = models.URLField()

    def __str__(self):
        return self.name

class ImageLink(models.Model):
    url = models.URLField()
    property_name = models.ForeignKey('Rumah',models.CASCADE)

    def __str__(self):
        return 'image for '+self.property_name.property_name

class Rumah(models.Model):
    PROPERTY_RUMAH = 'RM'
    PROPERTY_TANAH = 'TN'
    PROPERTY_APARTEMENT = 'AP'

    STATUS_JUAL = 'JL'
    STATUS_SEWA = 'SW'
    STATUS_JUAL_SEWA = 'JS'

    PROPERTY_TYPE = [
        (PROPERTY_RUMAH, 'Rumah'),
        (PROPERTY_TANAH, 'Tanah'),
        (PROPERTY_APARTEMENT, 'Apartement'),
    ]

    STATUS_TYPE = [
        (STATUS_JUAL, 'Jual'),
        (STATUS_SEWA, 'Sewa'),
        (STATUS_JUAL_SEWA, 'Jual/Sewa'),
    ]

    class Meta:
        ordering = ["-id"]

    property_name = models.CharField(max_length=250,null=False,blank=False)
    address = models.CharField(max_length=100,null=False,blank=False)
    price = models.CharField(max_length=50,null=False,blank=False)
    LT = models.CharField(max_length=20,blank=True)
    LB = models.CharField(max_length=20,blank=True)
    property_type = models.CharField(max_length=2,choices=PROPERTY_TYPE,null=False,blank=False)
    description = models.TextField(blank=True)
    release_date = models.CharField(max_length=50,blank=True,default='')
    publish_date = models.CharField(max_length=50,blank=True,default='')
    developer = models.ForeignKey(Developer,models.CASCADE,to_field='name',blank=True,default='-')
    agent = models.ManyToManyField(Agent,related_name='agent',blank=True)
    facility = models.TextField(blank=True)
    status = models.CharField(max_length=2,choices=STATUS_TYPE)
    certificate = models.CharField(max_length=50,blank=True)
    source = models.ForeignKey(Source,models.CASCADE,to_field='name',default='rumah123')
    
    def __str__(self):
        return self.property_name

