"""View moduel fo client."""
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView

from forms import AddAppointmentForm


class Appointment(TemplateView):
    """View module to add client."""

    template_name = 'appointment.html'

    def get(self, request):
        """Show form to add appointment."""
        form = AddAppointmentForm()

        args = {'form': form}
        return render(request, self.template_name, args)

    def post(self, request):
        """Save client."""
        pass
        '''
        form = AddClientForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            text = form.cleaned_data['name']
            form = AddClientForm()
            return redirect(reverse('client'))

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)
        '''
