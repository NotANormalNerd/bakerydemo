from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    ModelAdminGroup,
    modeladmin_register
)

from bakerydemo.heroteasers.models import HeroTeaserMainPanel, HeroTeaserSidePanel, TRexTeaser

"""
N.B. To see what icons are available for use in Wagtail menus and StreamField block types,
enable the styleguide in settings:

INSTALLED_APPS = (
   ...
   'wagtail.contrib.styleguide',
   ...
)

or see https://thegrouchy.dev/general/2015/12/06/wagtail-streamfield-icons.html

This demo project includes the full font-awesome set via CDN in base.html, so the entire
font-awesome icon set is available to you. Options are at https://fontawesome.com/icons .
"""


class HeroTeaserMainPanelAdmin(ModelAdmin):
    # These stub classes allow us to put various models into the custom "Wagtail Bakery" menu item
    # rather than under the default Snippets section.
    model = HeroTeaserMainPanel


class HeroTeaserSidePanelAdmin(ModelAdmin):
    model = HeroTeaserSidePanel


class TRexTeaserAdmin(ModelAdmin):
    menu_label = "T-Rex Teasers"  # ditch this to use verbose_name_plural from model
    menu_icon = "fa-users"  # change as required
    menu_order = 210  # will put in 3rd place (000 being 1st, 100 2nd)
    model = TRexTeaser


class HeroTeasersAdminGroup(ModelAdminGroup):
    menu_label = "HeroTeasers"
    menu_icon = "fa-suitcase"  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (HeroTeaserMainPanelAdmin, HeroTeaserSidePanelAdmin)

# When using a ModelAdminGroup class to group several ModelAdmin classes together,
# you only need to register the ModelAdminGroup class with Wagtail:
modeladmin_register(HeroTeasersAdminGroup)
modeladmin_register(TRexTeaserAdmin)
