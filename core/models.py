from django.db import models
from django.contrib.auth.models import User
import sys, os
from PIL import Image
from pickletools import optimize
sys.path.append('desafio_hubbi')
import settings



def upload_thumbnail(instance, filename):
    return f'images/{instance}-{filename}'


class Produto(models.Model):
    descricao = models.CharField(max_length=255, null=False, blank=False)
    foto = models.ImageField(upload_to=upload_thumbnail,null=False, blank=False)
    preco = models.FloatField(null=False, blank=False)

    @staticmethod
    def resize_image(img, new_width=300):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)
        original_width, original_height = img_pil.size

        if original_width <= new_width:
            img_pil.close()
            return
        
        new_height_rounded = round((new_width * original_height) / original_width)
        new_img = img_pil.resize((new_width, new_height_rounded), Image.LANCZOS)
        new_img.save(
            img_full_path,
            optimize=True,
            quality=80
        )
    
    
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        if self.foto: self.resize_image(self.foto)
       

    def __str__(self):
        return self.descricao

    # class Meta:
    #     managed = True
    #     db_table = 'Produto'


class Compra(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False)
    # class Meta:
    #     managed = True
    #     db_table = 'Compra'

    def __str__(self):
        return self.id


class CompraProduto(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.PROTECT, null=False, blank=False)
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False)


    # class Meta:
    #     managed = True
    #     db_table = 'CompraProduto'