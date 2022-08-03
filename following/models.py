from django.db import models
from LITReview import settings


class Following(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="followings")
    followed_user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="followers")

    class Meta():
        constraints = [models.UniqueConstraint(fields=['user', 'followed_user'], name='unique following')]
