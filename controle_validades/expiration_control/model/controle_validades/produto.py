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

    def save_image_from_base64(self, memory_view_data):
        image = Image.open(BytesIO(memory_view_data))

        
        buffer = BytesIO()
        image.save(buffer, format="JPEG")

        # Create an InMemoryUploadedFile
        image_name = f'{self.iddetalhe}.jpg'
        image_file = InMemoryUploadedFile(
            buffer,
            None,
            image_name,
            'image/jpeg',
            buffer.tell(),
            None
        )
        self.imagem.save(image_name, image_file, save=True)

    def __str__(self):
        return self.dsdetalhe