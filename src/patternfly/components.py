from django.utils.safestring import mark_safe
from django.utils.translation import gettext as _

from patternfly.utils import render_tag

from .text import text_value


def render_alert(content, alert_type=None, dismissible=True):
    """Render a Bootstrap alert."""
    button = ""
    if not alert_type:
        alert_type = "info"
    css_classes = ["pf-c-alert", "pf-m-" + text_value(alert_type)]
    if dismissible:
        close = _("close")
        button = (
            '<div class="pf-c-alert__action"><button type="button" class="pf-c-button pf-m-plain" data-dismiss="alert" aria-label="{close}"><i class="fas fa-times></i></button></div>'
        ).format(close=close)
    button_placeholder = "__BUTTON__"
    return mark_safe(
        render_tag(
            "div",
            attrs={"class": " ".join(css_classes), "role": "alert"},
            content=mark_safe(button_placeholder) + text_value(content),
        ).replace(button_placeholder, button)
    )
