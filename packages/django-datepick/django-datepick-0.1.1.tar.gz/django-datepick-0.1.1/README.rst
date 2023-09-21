========
Datepick
========

Django-datepick is a Django app to add a date, time and datetime pickers to
your forms.

Install
-------

Install the app with ``pip install django-datepick``.

Usage with forms
----------------

Change the widget used in your ``forms.py`` to use the widgets included in this app::

    from django import forms
    from datepick import widgets

    class MyForm(forms.Form):
        date_field = forms.DateField(widget=widgets.DateInput)
        datetime_field = forms.DateTimeField(widget=widgets.DateTimeInput)
        time_field = forms.TimeField(widget=widgets.TimeInput)

Usage with models
-----------------

Change the field used in your ``models.py`` to use the fields from this app::

    from django.db import models
    from datepick import fields

    class MyDateModel(models.Model):
        d = fields.DateField()
        dt = fields.DateTimeField()
        t = fields.TimeField()

Override the admin widget
-------------------------

Same as with any widget, register the model overriding the widget(s) in
`admin.py`::

    from datepick.widgets import DateInput, SplitDateTimeWidget, TimeInput

    class MyDateModelAdmin(admin.ModelAdmin):
        formfield_overrides = {
            models.DateField: {"widget": DateInput},
            # DON'T models.DateTimeField: {"widget": DateTimeInput}
            models.DateTimeField: {"widget": SplitDateTimeWidget}
            models.TimeField: {"widget": TimeInput},
        }

`DateTimeInput` doesn't work in the admin, as it expects a multivalue field.

Why?
----

Each time you use a date field in Django, the form is a text input. Any
frontend would like a datepicker of somekind. Turns out browsers and cellphones
already have a datepicker. It looks like this in a browser:


.. image:: https://raw.githubusercontent.com/xbello/django-datepick/master/docs/Firefox_Date.png
   :width: 150px

.. image:: https://raw.githubusercontent.com/xbello/django-datepick/master/docs/Chromium_Date.png
   :width: 150px

.. image:: https://raw.githubusercontent.com/xbello/django-datepick/master/docs/Chromium_Video.gif
   :width: 150px


And looks like this in a cellphone:

.. image:: https://raw.githubusercontent.com/xbello/django-datepick/master/docs/Android_Date.jpg
   :width: 150px

.. image:: https://raw.githubusercontent.com/xbello/django-datepick/master/docs/Android_Time.jpg
   :width: 150px

.. image:: https://raw.githubusercontent.com/xbello/django-datepick/master/docs/Android_DateTime.jpg
   :width: 150px


It doesn't need Javascript or extra CSS.

More info:

https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/time

https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/date

https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/datetime-local
