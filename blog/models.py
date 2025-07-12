from django.db import models

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    imagem = models.ImageField(upload_to='imagens/')


    class Meta:
        verbose_name = 'Postagem'
        verbose_name_plural = 'Postagens'
        ordering = ['-pub_date']

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    texto = models.CharField(max_length=500)
    com_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'
        ordering = ['-com_date']

    def __str__(self):
        return f'Comentário em {self.post.titulo}'
