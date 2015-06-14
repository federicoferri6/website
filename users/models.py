from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import ugettext as _

from petalerts.models import ModelWithLocation


class AreaSubscription(ModelWithLocation):
    user = models.ForeignKey(User)
    radius_km = models.PositiveIntegerField(
        help_text=_('Maximum distance from location '
                    'in Km. (1 to 7)'),
        validators=[
            MaxValueValidator(1),
            MinValueValidator(7)
        ])

    def clean(self):
        if self.user.areasubscription_set.count() >= 2:
            raise ValidationError(_('You can have 2 subscriptions at most.'))
        return super(AreaSubscription, self).clean()