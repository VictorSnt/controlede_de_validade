from io import BytesIO
from django.db import models
from django.conf import settings
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile


products_dir = settings.STATICFILES_DIRS[1]
class Produto(models.Model):
    iddetalhe = models.CharField(max_length=20, primary_key=True, unique=True)
    cdprincipal = models.CharField(max_length=20, unique=True)
    dsdetalhe = models.CharField(max_length=40, null=False)
    imagem = models.ImageField(upload_to=products_dir, null=True)

    def save_image_from_base64(self, base64_data:str):
        image = Image.open(BytesIO(bytes(base64_data.encode('utf-8'))))
        dados_binarios = base64_data.encode('utf-8')
        buffer = BytesIO(dados_binarios)
        image_name = f'{self.iddetalhe}.jpg'
        image = InMemoryUploadedFile(
            buffer, 
            None,   
            image_name, 
            'image/jpeg', 
            buffer.tell(),  
            None 
        )
        
        self.imagem.save(image_name, image, save=True)

    def __str__(self):
        return self.dsdetalhe