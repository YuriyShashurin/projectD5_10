from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from pets import models
from django.shortcuts import redirect

# Create your views here.
# def main_page(request):
#     return render(request, 'base.html', {})

PETS = 'pets'

class PetsListView (ListView):
    model = models.Pet
    template_name = 'index.html'
    context_object_name = PETS

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["animal"] = models.Animal.objects.all()
        context["blog5"] = models.Blog.objects.all().order_by('-pk')[:5]
        context["pets_count"] = models.Pet.objects.all()
        return context

class CatListView (ListView):
    model = models.Pet
    template_name = 'index.html'
    context_object_name = PETS

    def get_queryset(self):
        queryset = models.Pet.objects.filter(type_id=1)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["animal"] = models.Animal.objects.all()
        context["blog5"] = models.Blog.objects.all().order_by('-pk')[:5]
        context["pets_count"] = models.Pet.objects.all()
        
        return context

class DogListView (ListView):
    model = models.Pet
    template_name = 'index.html'
    context_object_name = PETS

    def get_queryset(self):
        queryset = models.Pet.objects.filter(type_id=2)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["animal"] = models.Animal.objects.all()
        context["blog5"] = models.Blog.objects.all().order_by('-pk')[:5]
        context["pets_count"] = models.Pet.objects.all()
        return context

class ParrotListView (ListView):
    model = models.Pet
    template_name = 'index.html'
    context_object_name = PETS

    def get_queryset(self):
        queryset = models.Pet.objects.filter(type_id=3)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["animal"] = models.Animal.objects.all()
        context["blog5"] = models.Blog.objects.all().order_by('-pk')[:5]
        context["pets_count"] = models.Pet.objects.all()
        return context


class PetInfoView(DetailView):
    model = models.Pet
    template_name = 'pet_info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["animal"] = models.Animal.objects.all()
        context["blog5"] = models.Blog.objects.all().order_by('-pk')[:5]
        context["pets_count"] = models.Pet.objects.all()
        return context

def add_like(request):
        if request.method == 'POST':
            pet_id = request.POST['id']
            if not pet_id:
                return redirect('/pets/{}'.format(pet_id))
            else:
                pet = models.Pet.objects.filter(id=pet_id).first()
                if not pet:
                    return redirect('/pets/{}'.format(pet_id))
                pet.like += 1
                pet.save()
                return redirect('/pets/{}'.format(pet_id))
        else:
            return redirect('/pets/{}')


class BlogLisView(ListView):
    model = models.Blog
    template_name = 'blogs.html'
    context_object_name = 'blogs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["animal"] = models.Animal.objects.all()
        context["pets_count"] = models.Pet.objects.all()
        context["blog5"] = models.Blog.objects.all().order_by('-pk')[:5]
        return context

class BlogDetailView(DetailView):
    model = models.Blog
    template_name = 'blogpost.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["animal"] = models.Animal.objects.all()
        context["pets_count"] = models.Pet.objects.all()
        context["blog5"] = models.Blog.objects.all().order_by('-pk')[:5]
        return context

def handler404(request, exception):
    context ={}
    context["animal"] = models.Animal.objects.all()
    context["pets_count"] = models.Pet.objects.all()
    context["blog5"] = models.Blog.objects.all().order_by('-pk')[:5]
    return render(request, 'blog-404.html', context)

class ContactsPageView(TemplateView):
    template_name = 'aboutus.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["animal"] = models.Animal.objects.all()
        context["pets_count"] = models.Pet.objects.all()
        context["blog5"] = models.Blog.objects.all().order_by('-pk')[:5]
        return context

