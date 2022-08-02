from django.core.validators import slug_re
from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Artikel(models.Model):
    judul = models.CharField(max_length=255)
    konten = models.TextField()
    kategori = models.CharField(max_length=45)
    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, editable=False)

    def save(self):
        self.slug = slugify(self.judul)
        return super().save()

    def get_absolute_url(self):
        return reverse('artikel:detail', kwargs={'slug': self.slug})

    def __str__(self):
        return '{}. {}'.format(self.id, self.judul)
