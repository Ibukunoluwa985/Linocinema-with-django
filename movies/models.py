from django.contrib.auth.models import User
import urllib.parse as urlparse
from django.db import models
from PIL import Image

def youtude_id(value):
    query = urlparse.urlparse(value)
    if query.hostname == 'youtu.be':
        return query.path[1:]
    if query.hostname in ('www.youtube.com', 'youtube.com'):
        if query.path == '/watch':
            p = urlparse.parse_qs(query.query)
            return p['v'][0]
        if query.path[:7] == '/embed/':
            return query.path.split('/')[2]
        if query.path[:3] == '/v/':
            return query.path.split('/')[2]
    return None

GENRE_CHOICES = (
   ('Action', 'Action'),
   ('Animation', 'Animation'),
   ('Crime', 'Crime'),
   ('Comedy', 'Comedy'),
   ('Drama', 'Drama'),
   ('Documentary', 'Documentary'),
   ('Family', 'Family'),
   ('Horror', 'Horror'),
   ('Romance', 'Romance'),
   ('Sci-fi', 'Sci-fi'),
)

class Movies(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True,)
    permission = models.IntegerField(default=1)
    image = models.ImageField(upload_to='movie_img', default='no-image.png')
    image_link = models.CharField(max_length=1000, default="None", blank=False, null=False)
    slider_image = models.ImageField(upload_to='slider_img/movies', default='no-image.png')
    title = models.CharField(max_length=250, null=True)
    language = models.CharField(max_length=250, default='English')
    rate = models.CharField(max_length=250, null=True)
    trailer = models.CharField(max_length=250, null=True)
    genre = models.CharField(choices=GENRE_CHOICES, max_length=250, null=True)
    year = models.PositiveIntegerField()
    link = models.CharField(max_length=500, null=True)
    mb = models.PositiveIntegerField()
    director = models.CharField(max_length=250, null=True)
    director_link = models.CharField(max_length=500, null=True)
    subtitle = models.CharField(max_length=500, blank=True, null=True)
    added_on = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=5000, null=True)

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        self.trailer = youtude_id(self.trailer)
        super(Movies, self).save(*args, **kwargs)
        image = Image.open(self.image)
        image.thumbnail((500, 500))
        image.save(self.image.path)
        slider_image = Image.open(self.slider_image)
        slider_image.thumbnail((500, 300))
        slider_image.save(self.slider_image.path)