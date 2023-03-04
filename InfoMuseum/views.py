from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from InfoMuseum.forms import MediaForm

from django.views.generic import DetailView
from InfoMuseum.models import Media

class MuseumImage(TemplateView):

    form = MediaForm
    template_name = 'img.html'

    def post(self, request, *args, **kwargs):

        form = MediaForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save()
            return HttpResponseRedirect(reverse_lazy('image_display', kwargs={'pk': obj.id}))

        context = self.get_context_data(form=form)
        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class ImageDisplay(DetailView):
    model = Media
    template_name = 'image_display.html'
    context_object_name = 'img'