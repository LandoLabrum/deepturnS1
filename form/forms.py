from django import forms
from lead.models import lead_model


class LeadForm(forms.ModelForm):
    title = forms.CharField(label='',
                                  widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Your description",
                "class": "new-class-name two",
                "id": "my-id-for-textarea",
                "rows": 20,
                'cols': 120
            }
        )
    )
    price = forms.DecimalField(initial=199.99)

    class Meta:
        model = lead_model
        fields = [
            'title',
            'description',
            'price'
        ]


class RawLeadForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(
        attrs={"placeholder": "Your title"}))
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Your description",
                "class": "new-class-name two",
                "id": "my-id-for-textarea",
                "rows": 20,
                'cols': 120
            }
        )
    )
    price = forms.DecimalField(initial=199.99)
