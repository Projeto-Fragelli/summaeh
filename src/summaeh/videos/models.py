from django.conf import settings
from django.db import models

from model_utils.models import TimeStampedModel
from .validators import is_youtube_video


class Video(TimeStampedModel):
    """
    Representa um vídeo do youtube.
    """

    event = models.ForeignKey(
        'events.Event',
        related_name='videos',
        verbose_name='Evento',
        on_delete=models.CASCADE
    )
    link = models.URLField(
        'Link',
        max_length=200,
        help_text='Link do vídeo no Youtube (ex.: https://youtube.com/...)',
        validators=[is_youtube_video],
    )
    name = models.CharField(
        'Nome',
        max_length=200,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Usuário',
        related_name='videos',
        on_delete=models.PROTECT,
        help_text='Usuário responsável pelo vídeo.',
    )

    def __str__(self):
        return self.name

    def new_comment(self, user, comment):
        """
        Cria um comentário no vídeo para o usuário dado.
        """
        self.comments.create(user=user, comment=comment)

    def num_votes(self, event):
        """
        Retorna a quantidade de vídeos um evento possui.
        """
        return self.votes.filter(event=event).count()



class Comment(TimeStampedModel):
    """
    Comentário em um vídeo.
    """

    video = models.ForeignKey(
        Video,
        related_name='comments',
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Usuário',
        related_name='comments',
    )
    comment = models.TextField()


class Like(TimeStampedModel):
    """
    Um like para um vídeo.
    """

    video = models.ForeignKey(
        Video,
        related_name='likes',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='likes',
        on_delete=models.PROTECT,
    )


class Vote(TimeStampedModel):
    """
    Um voto para um vídeo.
    """
    event = models.ForeignKey(
        'events.Event',
        related_name='votes',
        on_delete=models.CASCADE
    )
    video = models.ForeignKey(
        Video,
        related_name='votes',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='votes',
        on_delete=models.PROTECT,
    )