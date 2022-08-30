from __future__ import unicode_literals

from django.db import models
from wagtail.admin.panels import FieldPanel, FieldRowPanel
from wagtail.fields import RichTextField
from wagtail.models import TranslatableMixin, DraftStateMixin, RevisionMixin, \
    Orderable
from wagtail.snippets.models import register_snippet


@register_snippet
class HeroTeaserMainPanel(TranslatableMixin, DraftStateMixin, RevisionMixin, Orderable, models.Model):
    """
    This provides editable text for the site footer. Again it uses the decorator
    `register_snippet` to allow it to be accessible via the admin. It is made
    accessible on the template via a template tag defined in base/templatetags/
    navigation_tags.py
    """
    body = RichTextField()

    panels = [
        FieldRowPanel([
            FieldPanel('go_live_at'),
            FieldPanel('expire_at'),
        ]),
        FieldPanel('body'),
    ]

    def __str__(self):
        return 'Heroteaser Main Panel'

    class Meta(TranslatableMixin.Meta, Orderable.Meta):
        verbose_name_plural = 'Heroteaser Main Panels'


@register_snippet
class HeroTeaserSidePanel(TranslatableMixin, DraftStateMixin, RevisionMixin, Orderable, models.Model):
    """
    This provides editable text for the site footer. Again it uses the decorator
    `register_snippet` to allow it to be accessible via the admin. It is made
    accessible on the template via a template tag defined in base/templatetags/
    navigation_tags.py
    """

    body = RichTextField()

    panels = [
        FieldRowPanel([
            FieldPanel('go_live_at'),
            FieldPanel('expire_at'),
        ]),
        FieldPanel("body"),
    ]

    def __str__(self):
        return "Hero Teaser Side Panel"

    class Meta(TranslatableMixin.Meta, Orderable.Meta):
        verbose_name_plural = 'Heroteaser Side Panels'


@register_snippet
class TRexTeaser(TranslatableMixin, DraftStateMixin, RevisionMixin, Orderable, models.Model):
    """
    This provides editable text for the site footer. Again it uses the decorator
    `register_snippet` to allow it to be accessible via the admin. It is made
    accessible on the template via a template tag defined in base/templatetags/
    navigation_tags.py
    """

    body = RichTextField()

    panels = [
        FieldRowPanel([
            FieldPanel('go_live_at'),
            FieldPanel('expire_at'),
        ]),
        FieldPanel("body"),
    ]

    def __str__(self):
        return 'T-Rex Teasers'

    class Meta(TranslatableMixin.Meta, Orderable.Meta):
        verbose_name_plural = 'T-Rex Teasers'
