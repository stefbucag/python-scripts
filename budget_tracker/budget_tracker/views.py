"""View moduel fo client."""
from django import forms
from django.db.models import Sum
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView

from forms import AddCashflowForm
from models import Cashflow


class TrackerView(TemplateView):
    """View moduel fo client."""

    template_name = 'index.html'

    def get(self, request):
        """Get cashflow."""
        track = Cashflow.objects.all()

        total_expenses = Cashflow.objects.aggregate(Sum('expense'))
        total_income = Cashflow.objects.aggregate(Sum('income'))
        savings = total_income['income__sum'] - total_expenses['expense__sum']
        args = {
            'cashflow': track,
            'total_expenses': total_expenses['expense__sum'],
            'total_income': total_income['income__sum'],
            'savings': savings
        }
        return render(request, self.template_name, args)


class CashFlowView(TemplateView):
    """Page that handles cashflow."""

    template_name = 'add.html'

    def get(self, request):
        """Get clients."""
        form = AddCashflowForm()

        return render(request, self.template_name, {'form': form})

    def clean(self):
        """Clean form data."""
        cleaned_data = super(self).clean()
        expense = cleaned_data.get('expense')
        income = cleaned_data.get('income')

        if expense == 0 and income == 0:
            raise forms.ValidationError(
                "Expense and Income cannot be both 0."
            )

    def post(self, request):
        """Save client."""
        form = AddCashflowForm(request.POST)
        # self.clean()

        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            return redirect(reverse('tracker'))

        args = {'form': form}
        return render(request, self.template_name, args)
