from django.db.models.fields import DateField, DateTimeField, TimeField
from . import forms


class DateField(DateField):
    def formfield(self, **kwargs):
        return super().formfield(
            **{
                "form_class": forms.DateField,
                **kwargs,
            }
        )


class DateTimeField(DateTimeField):
    def formfield(self, **kwargs):
        return super().formfield(
            **{
                "form_class": forms.DateTimeField,
                **kwargs,
            }
        )


class TimeField(TimeField):
    def formfield(self, **kwargs):
        return super().formfield(
            **{
                "form_class": forms.TimeField,
                **kwargs,
            }
        )
