from django import forms
from models import Cashflow


class AddCashflowForm(forms.ModelForm):
    """Actual saving of the client."""

    class Meta:
        """Meta."""

        model = Cashflow
        fields = (
            'expense',
            'income',
        )

    def save(self, commit=True):
        """Save client."""
        cashflow = super(AddCashflowForm, self).save(commit=False)
        cashflow.expense = self.cleaned_data['expense']
        cashflow.income = self.cleaned_data['income']

        if commit:
            cashflow.save()

        return cashflow
