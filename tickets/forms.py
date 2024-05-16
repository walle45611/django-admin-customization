from django import forms
from django.forms import ModelForm, RadioSelect
from tickets.models import Ticket


class BookingForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=64)
    last_name = forms.CharField(label='Last Name', max_length=64)
    payment_method = forms.ChoiceField(
        choices=[
            ('CC', 'Credit card'),
            ('DC', 'Debit card'),
            ('ET', 'Ethereum'),
            ('BC', 'Bitcoin')
        ],
        label='Payment Method'
    )

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['payment_method'].widget.attrs.update(
            {'class': 'form-select'})


class TicketAdminForm(ModelForm):
    first_name = forms.CharField(label="First name", max_length=32)
    last_name = forms.CharField(label="Last name", max_length=32)

    class Meta:
        model = Ticket
        fields = ["concert", "first_name",
                  "last_name", "payment_method", "is_active"]
        widgets = {
            "payment_method": RadioSelect(),
        }

    def __init__(self, *args, **kwargs):
        instance = kwargs.get("instance")
        initial = kwargs.get('initial', {})

        if instance:
            customer_full_name_split = instance.customer_full_name.split(
                " ", maxsplit=1)
            initial.update({
                "first_name": customer_full_name_split[0],
                "last_name": customer_full_name_split[1] if len(customer_full_name_split) > 1 else ""
            })

        kwargs['initial'] = initial
        super(TicketAdminForm, self).__init__(
            *args, **kwargs)

    def save(self, commit=True):
        self.instance.customer_full_name = (
            self.cleaned_data["first_name"] +
            " " + self.cleaned_data["last_name"]
        )
        return super().save(commit)
