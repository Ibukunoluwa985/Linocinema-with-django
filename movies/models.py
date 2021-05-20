from django.db import models
from django.contrib.auth.models import User

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
    image = models.ImageField(upload_to='movie_img', default='../static/images/no-image.png')
    image_link = models.CharField(max_length=1000, default="None", blank=False, null=False)
    title = models.CharField(max_length=250, null=True)
    language = models.CharField(max_length=250, default='English')
    rate = models.CharField(max_length=250, null=True)
    trailer = models.CharField(max_length=250, null=True)
    genre = models.CharField(choices=GENRE_CHOICES, max_length=250, null=True)
    year = models.IntegerField()
    link = models.CharField(max_length=500, null=True)
    mb = models.IntegerField()
    director = models.CharField(max_length=250, null=True)
    director_link = models.CharField(max_length=500, null=True)
    subtitle = models.CharField(max_length=500, blank=True, null=True)
    added_on = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=5000, null=True)

    def __str__(self):
        return f"{self.title}"