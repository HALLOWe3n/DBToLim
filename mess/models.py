from django.db import models


class Message(models.Model):
    email = models.EmailField(max_length=254)
    message = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Created: {}, from email: {} - text: {}...'.format(
            self.created, self.email, self.message[:15]
        )
