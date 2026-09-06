from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Bolsista, SessaoTrabalho
from .sync import sincronizar_historico_bolsista_bg


@receiver(post_save, sender=Bolsista)
def sync_bolsista_on_save(sender, instance, **kwargs):
    """Quando o admin edita um bolsista, reenvia o histórico completo para a nuvem."""
    sincronizar_historico_bolsista_bg(instance)


@receiver(post_save, sender=SessaoTrabalho)
def sync_sessao_on_save(sender, instance, **kwargs):
    """
    Quando bate ou fecha o ponto, reenvia o histórico completo do bolsista dono da sessão.
    Um único disparo garante que o saldo de pendência e as sessões estejam atualizados.
    """
    sincronizar_historico_bolsista_bg(instance.bolsista)
