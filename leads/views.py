from django.shortcuts import render, redirect, reverse
# from django.contrib.auth.forms import UserCreationForm
from .models import Lead
from .forms import LeadModelForm, CustomUserCreationForm
from django.views import generic

# class based views


class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse('login-page')


class LandingPageView(generic.TemplateView):
    template_name = "landing.html"


class LeadListView(generic.ListView):
    template_name = 'leads/lead_list.html'
    queryset = Lead.objects.all()
    context_object_name = 'leads'


class LeadDetailView(generic.DetailView):
    template_name = "leads/lead_detail.html"
    queryset =  Lead.objects.all()
    context_object_name = 'lead'


class LeadCreateView(generic.CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse('leads:lead-list')


class LeadUpdateView(generic.UpdateView):
    template_name = "leads/lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse('leads:lead-list')


class LeadDeleteView(generic.DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:lead-list')


# Create your views here.

def landing_view(request):
    return render(request, "landing.html")


def lead_list(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    return render(request, "leads/lead_list.html", context)


def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        "lead": lead
    }
    return render(request, "leads/lead_detail.html", context)


def lead_create(request):
    print(request.method)
    form = LeadModelForm()
    if request.method=="POST":
        form = LeadModelForm(request.POST)
        # this will again fill whatever values we have passed in each field otherwise passed LeadForm() in
        # context then fileds would not retain their values
        if form.is_valid():
            form.save()
            return redirect("/leads")
    context = {
        "form": form
    }
    return render(request, 'leads/lead_create.html', context)


def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method=="POST":
        form = LeadModelForm(request.POST,instance=lead)
        if form.is_valid():
            print("lead has been updated")
            form.save()
            return redirect("/leads")
    context = {
        "form": form,
        "lead": lead
    }
    return render(request, 'leads/lead_update.html', context)


def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/leads")


# def lead_update(request, pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadForm(instance=lead)
#     if request.method=="POST":
#         print("a POST request")
#         form = LeadForm(request.POST,instance=lead)
#         # this will again fill whatever values we have passed in each field otherwise passed LeadForm() in
#         # context then fileds would not retain their values
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             lead.first_name = first_name
#             lead.last_name = last_name
#             lead.age = age
#             print("lead has been updated")
#             lead.save()
#             return redirect("/leads")
#     context = {
#         "form": form,
#         "lead": lead
#     }
#     return render(request, 'leads/lead_update.html', context)

    # def lead_create(request):
    #     print(request.method)
    #     form = LeadForm()
    #     if request.method=="POST":
    #         print("a POST request")
    #         form = LeadForm(request.POST)
    #         # this will again fill whatever values we have passed in each field otherwise passed LeadForm() in
    #         # context then fileds would not retain their values
    #         if form.is_valid():
    #             print("form is validated")
    #             print(form.cleaned_data)
    #             first_name = form.cleaned_data['first_name']
    #             last_name = form.cleaned_data['last_name']
    #             age = form.cleaned_data['age']
    #             agent = Agent.objects.first()
    #             Lead.objects.create(first_name=first_name,
    #                                 last_name=last_name,
    #                                 age=age,
    #                                 agent=agent)
    #             print("lead has been created")
    #             form.save()
    #             return redirect("/leads")
    #     context = {
    #         "form": form
    #     }
    #     return render(request, 'leads/lead_create.html', context)
