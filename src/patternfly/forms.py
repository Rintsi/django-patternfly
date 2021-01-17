from django.forms import EmailInput, NumberInput, PasswordInput, Textarea, TextInput, URLInput
from django.utils.safestring import mark_safe

from .bootstrap import get_bootstrap_setting, get_field_renderer, get_form_renderer, get_formset_renderer
from .exceptions import BootstrapError
from .text import text_value
from .utils import add_css_class, render_tag

FORM_GROUP_CLASS = "pf-c-form__group"

def render_formset(formset, **kwargs):
    """Render a formset to a Bootstrap layout."""
    renderer_cls = get_formset_renderer(**kwargs)
    return renderer_cls(formset, **kwargs).render()


def render_formset_errors(formset, **kwargs):
    """Render formset errors to a Bootstrap layout."""
    renderer_cls = get_formset_renderer(**kwargs)
    return renderer_cls(formset, **kwargs).render_errors()


def render_form(form, **kwargs):
    """Render a form to a Bootstrap layout."""
    renderer_cls = get_form_renderer(**kwargs)
    return renderer_cls(form, **kwargs).render()


def render_form_errors(form, type="all", **kwargs):
    """Render form errors to a Bootstrap layout."""
    renderer_cls = get_form_renderer(**kwargs)
    return renderer_cls(form, **kwargs).render_errors(type)


def render_field(field, **kwargs):
    """Render a field to a Bootstrap layout."""
    renderer_cls = get_field_renderer(**kwargs)
    return renderer_cls(field, **kwargs).render()


def render_label(
    content,
    required=False,
    label_for=None,
    label_class="pf-c-form__label",
    label_container_class="pf-c-form__group-label",
    label_title_class="pf-c-form__label-text",
    label_required_class="pf-c-form__label-required",
    label_title="",
):
    """Render a label with content."""
    attrs = {}
    label_attrs = { "class": label_title_class }
    container_attrs = { "class": label_container_class }
    required_attrs = { "class": label_required_class }

    if label_for:
        attrs["for"] = label_for
    if label_class:
        attrs["class"] = label_class
    if label_title:
        attrs["title"] = label_title
    title = render_tag("span", attrs=label_attrs, content=content)
    label_content = [title]
    if required:
        required_span = render_tag("span", attrs=required_attrs, content=mark_safe("&#42;"))
        label_content.append(required_span)

    label = render_tag("label", attrs=attrs, content=mark_safe("\n".join(label_content)))
    return render_tag("div", attrs=container_attrs, content=label)



def resolve_button_class_from_type(button_class, button_type=None):
    default_class="pf-m-primary"
    reset_class="pf-m-link"
    link_class="pf-m-link"
    if button_class:
        # If button class is already defined, use that
        return button_class
    if button_type == None:
        # If no type is defined return default
        return default_class
    elif button_type == "reset":
        return reset_class
    elif button_type == "link":
        return link_class

    return default_class

def render_button(
    content,
    button_type=None,
    button_class=None,
    size="",
    href="",
    name=None,
    value=None,
    title=None,
    extra_classes="",
    id="",
):
    """Render a button with content."""
    attrs = {}
    classes = add_css_class("pf-c-button", resolve_button_class_from_type(button_class, button_type))
    size = text_value(size).lower().strip()
    if size == "xs":
        classes = add_css_class(classes, "btn-xs")
    elif size == "sm" or size == "small":
        classes = add_css_class(classes, "btn-sm")
    elif size == "lg" or size == "large":
        classes = add_css_class(classes, "btn-lg")
    elif size == "md" or size == "medium":
        pass
    elif size:
        raise BootstrapError('Parameter "size" should be "xs", "sm", "lg" or empty ("{size}" given).'.format(size=size))

    if button_type:
        if button_type not in ("submit", "reset", "button", "link"):
            raise BootstrapError(
                (
                    'Parameter "button_type" should be "submit", "reset", "button", "link" or empty '
                    '("{button_type}" given).'
                ).format(button_type=button_type)
            )
        if button_type != "link":
            attrs["type"] = button_type


    classes = add_css_class(classes, extra_classes)
    attrs["class"] = classes

    if href:
        tag = "a"
        if button_type and button_type != "link":
            raise BootstrapError(
                'Button of type "{button_type}" is not allowed a "href" parameter.'.format(button_type=button_type)
            )
        attrs["href"] = href
        # Specify role for link with button appearance
        attrs.setdefault("role", "button")
    else:
        tag = "button"

    if id:
        attrs["id"] = id
    if name:
        attrs["name"] = name
    if value:
        attrs["value"] = value
    if title:
        attrs["title"] = title
    return render_tag(tag, attrs=attrs, content=mark_safe(content))


def render_field_and_label(field, label, field_class="", label_for=None, label_class="", layout="", **kwargs):
    """Render a field with its label."""
    if layout == "horizontal":
        if not label_class:
            label_class = get_bootstrap_setting("horizontal_label_class")
        if not field_class:
            field_class = get_bootstrap_setting("horizontal_field_class")
        if not label:
            label = mark_safe("&#160;")
        label_class = add_css_class(label_class, "control-label")
    html = field
    if field_class:
        html = '<div class="{field_class}">{html}</div>'.format(field_class=field_class, html=html)
    if label:
        html = render_label(label, label_for=label_for, label_class=label_class) + html
    return html


def render_form_group(content, css_class=FORM_GROUP_CLASS):
    """Render a Bootstrap form group."""
    return '<div class="{css_class}"><div class="pf-c-form__actions pf-u-pt-md">{content}</div></div>'.format(css_class=css_class, content=content)


def is_widget_with_placeholder(widget):
    """
    Return whether this widget should have a placeholder.

    Only text, text area, number, e-mail, url, password, number and derived inputs have placeholders.
    """
    return isinstance(widget, (TextInput, Textarea, NumberInput, EmailInput, URLInput, PasswordInput))
