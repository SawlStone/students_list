# -*- coding: utf-8 -*-
from django.shortcuts import render
from django import forms
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from studentsdb_2.settings import ADMIN_EMAIL


class ContactForm(forms.Form):

    def __init__(self, *args, **kwargs):
        # call original initialisator
        super(ContactForm, self).__init__(*args, **kwargs)

        # this helper object allows us to customize form
        self.helper = FormHelper()

        # form tag attributes
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('contact_admin')

        # twitter bootstrap styles
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'

        # form buttons
        self.helper.add_input(Submit('send_button', 'Надіслати'))

    from_email = forms.EmailField(
        label="Ваша Емейл Адреса")

    subject = forms.CharField(
        label="Заголовок листа",
        max_length=128)

    message = forms.CharField(
        label="Текст повідомлення",
        max_length=2560,
        widget=forms.Textarea)


def contact_admin(request):
    # check if formwas posted
    if request.method == 'POST':
        # create a form instance ad populate it with data from the request
        form = ContactForm(request.POST)

        # check whether user data is valid
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['from_email']

            try:
                send_mail(subject, message, from_email, [ADMIN_EMAIL])
            except Exception:
                message = 'Під час відправки листа виникла непередбачуванна помилка.' \
                          'Спрбуйте скористатися данною формю пізніше.'
            else:
                message = 'Повідомлення успішно надісланне!'

            # redirect to same contact page with message
            return HttpResponseRedirect(
                '%s?status_message=%s' % (reverse('contact_admin'), message))
    else:
        form = ContactForm()

    return render(request, 'contact_admin/form.html', {'form': form})
