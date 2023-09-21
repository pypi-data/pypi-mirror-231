"""
app config
"""

# Django
from django.apps import AppConfig  # pylint: disable=import-error

# AA SRP
from ckeditor_skins import __version__


class CkeditorSkinsConfig(AppConfig):  # pylint: disable=too-few-public-methods
    """
    application config
    """

    name = "ckeditor_skins"
    label = "ckeditor_skins"
    verbose_name = f"Django CKeditor Skins v{__version__}"
