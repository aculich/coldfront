from django.dispatch import receiver
from django_q.tasks import async_task

from common.djangolibs.utils import import_from_settings
from core.djangoapps.project.views import (ProjectAddUsersView,
                                           ProjectRemoveUsersView)
from core.djangoapps.subscription.signals import (subscription_activate_user,
                                                  subscription_remove_user)
from core.djangoapps.subscription.views import (SubscriptionActivateRequestView,
                                                SubscriptionAddUsersView,
                                                SubscriptionDeleteUsersView,
                                                SubscriptionRenewView)


@receiver(subscription_activate_user, sender=ProjectAddUsersView)
@receiver(subscription_activate_user, sender=SubscriptionActivateRequestView)
@receiver(subscription_activate_user, sender=SubscriptionAddUsersView)
def activate_user(sender, **kwargs):
    subscription_user_pk = kwargs.get('subscription_user_pk')
    async_task('extra.djangoapps.freeipa.tasks.add_user_group', subscription_user_pk)


@receiver(subscription_remove_user, sender=ProjectRemoveUsersView)
@receiver(subscription_remove_user, sender=SubscriptionDeleteUsersView)
@receiver(subscription_remove_user, sender=SubscriptionRenewView)
def remove_user(sender, **kwargs):
    subscription_user_pk = kwargs.get('subscription_user_pk')
    async_task('extra.djangoapps.freeipa.tasks.remove_user_group', subscription_user_pk)
