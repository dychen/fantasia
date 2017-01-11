from django.db.models.signals import post_save
from django.dispatch import receiver
from sportsbook.models import Odds
from sportsbook.webhooks import post_to_slack

ARB_DELTA = 5 # In seconds
MIN_MARGIN, MAX_MARGIN = (0.00, 1.00)

def format_arb_list(arbs):
    arbs = [arb for arb in arbs
            if arb.margin > MIN_MARGIN and arb.margin < MAX_MARGIN]
    return '\n'.join([arb.__unicode__() for arb in arbs])

@receiver(post_save, sender=Odds, dispatch_uid='sportsbook_calculate_arb')
def calculate_arb(sender, instance, **kwargs):
    """
    Args:
        sender [Odds]: Class of the signal being received.
        instance [Odds]: Model instance of the signal being received.
        kwargs [dict]: Example: {
            'update_fields': None,
            'raw': False,
            'signal': <django.db.models.signals.ModelSignal>,
            'using': 'default',
            'created': False
        }
    """
    results = instance.write_arbs(delta=5)
    post_to_slack(format_arb_list(results))
