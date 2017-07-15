from django import forms
from schedule.models import Event


class AddAppointmentForm(forms.ModelForm):
    """Actual saving of the client."""

    class Meta:
        """Meta."""

        model = Event
        fields = (
            'title',
            'start',
            'end',
        )

    def save(self, commit=True):
        """Save appointment."""
        appointment = super(AddAppointmentForm, self).save(commit=False)
        appointment.name = self.cleaned_data['title']

        if commit:
            appointment.save()

        return appointment
