from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, DeleteView, UpdateView
from portfolio.models import Profile, Projects, Skills, Contact
from portfolio.forms import CustomUserCreationForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin




class Index(TemplateView):
    template_name =  "portfolio/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['skills'] = Skills.objects.all()  #[:5]
        context['projects'] = Projects.objects.all()
        context['profile'] = Profile.objects.first()
        return context
    
    


# view for registration of users
class Register(CreateView):
    form_class = CustomUserCreationForm
    success_url = '/'
    template_name = 'portfolio/register.html'
    
    def form_valid(self, form):
        messages.success(self.request, "Your registration is successful. Congrats !")
        return super().form_valid(form)
    


class Dashboard(LoginRequiredMixin ,TemplateView):
    template_name = "portfolio/overview.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        context['skill'] = Skills.objects.count()  
        context['project'] = Projects.objects.count()
        context['message'] = Contact.objects.count()
        return context
    
    

# View for list of messages
class MessagesView(TemplateView):
    template_name = "portfolio/messages.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = Contact.objects.all()
        context['profile'] = Profile.objects.first()
        return context


# Function view to send Message
def sendMessage(request):
   
    if request.method == 'POST':
        name_gotten = request.POST.get('name')
        email_gotten = request.POST.get('email')
        phone_gotten = request.POST.get('phone')
        msg_gotten = request.POST.get('msg')
     
        contact = Contact(name = name_gotten, email = email_gotten, phone = phone_gotten, message = msg_gotten)
      
        contact.save()
        messages.success(request, "Message sent successfully")
      
    context = {
       "skills" :  Skills.objects.all(),
       "projects" : Projects.objects.all(),
       "profile" : Profile.objects.first()
    }    
            
    return render(request, 'portfolio/index.html', context= context)

# View to delete a message
class DeleteMessage(DeleteView):
    model = Contact
    success_url = reverse_lazy('messages_page')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        return context
    
    
   
   
   
    
 # View for list of works or projects done   
class ProjectsView(TemplateView):
    template_name = "portfolio/projects.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        context['projects'] = Projects.objects.all()
        return context    
 
 
 
# Create or add more projects 
class CreateProjectsView(CreateView):
    model = Projects
    success_url = reverse_lazy('projects_page')
    fields = ['description', 'image']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        return context 
    
    

# Update already existing projects
class UpdateProjectsView(UpdateView):
    model = Projects
    success_url = reverse_lazy('projects_page')
    fields = ['description', 'image']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        return context
    
    

# Delete Skills
class DeleteProjectView(DeleteView):
    model = Projects
    success_url = reverse_lazy('projects_page')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        return context
  
   
   
   
   
   
# list of skills 
class SkillsView(TemplateView):
    template_name = "portfolio/skills.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['skills'] = Skills.objects.all()
        context['profile'] = Profile.objects.first()
        return context
  
  
    
# Add and Create more skills
class CreateSkillView(CreateView):
    model = Skills
    success_url = reverse_lazy('skills_page')
    fields = ['name', 'level']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        return context
    




# Update Skills
class UpdateSkillsView(UpdateView):
    model = Skills
    success_url = reverse_lazy('skills_page')
    fields = ['name', 'level']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        return context
    
    
    
# Delete Skills
class DeleteSkills(DeleteView):
    model = Skills
    success_url = reverse_lazy('skills_page')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        return context
    
    




# For profile bio view
class ProfileView(TemplateView):
    template_name = "portfolio/profile.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        return context
    



# Update profile view here
class UpdateProfileView(UpdateView):
    model = Profile
    success_url = reverse_lazy('profile_page')
    fields = [
        'name', 
        'profile_image', 
        'about_image', 
        'skill_image', 
        'phone', 
        'email', 
        'facebook', 
        'twitter', 
        'instagram', 
        'whatsapp',         
        'num_of_clients',
        'cv',
        'personal_info',
    ]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        return context
    