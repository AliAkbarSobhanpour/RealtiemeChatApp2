from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    pass


class Message(models.Model):
    """
        this model is for chats can be mor than this :
            now has :
                1.a text data that user sends
                2.a user that create this chat
                3.a creation date . 
        it can has emogy and other things and also a field whit mor capability of editing data.
    """
    text = models.TextField(verbose_name="text")
    Create_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    create_date = models.DateTimeField("creation date",auto_now=True)

    class Meta:
        verbose_name = "message"
        verbose_name_plural = "messages"

