from . import util
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .forms import EntryForm
from .models import MyEntries
import markdown2
from django.views.generic import ListView
import random
from django.contrib import messages

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def my_entry(request, title): 
    myentry = util.list_entries()  
    if title in myentry:
        text = markdown2.markdown(util.get_entry(title))
        return render(request, "encyclopedia/my_entry.html", {'text': text})                
    else:
        return render(request, 'encyclopedia/pagenotexist.html')

class SearchResultsView(ListView):
    model = MyEntries
    template_name = 'encyclopedia/search_results.html'
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = MyEntries.objects.filter(title__icontains=query)
        return object_list

def create_entry(request):    
    if request.method == 'POST':
        form = EntryForm(request.POST or None) 
        if request.POST: 
            if form.is_valid(): 
                form.save(commit= False)   
                title = form.cleaned_data.get('title')
                mycontent = form.cleaned_data.get('content')
                content = '#' + title + "\n" + mycontent
                for entry in util.list_entries():
                    if title != entry:
                        form.save(commit=True)
                        util.save_entry(title, content)    
                    else: 
                        messages.info(request, 'The title already exists.')
                        return HttpResponseRedirect('/entry/')
    else:
        form = EntryForm()         
    return render(request, "encyclopedia/create_entry.html", {'form': form}) 

def list_entry(request):
    dataset = MyEntries.objects.all()
    return render(request, "encyclopedia/list_entry.html", {'dataset': dataset})

def detail_entry(request, id):
    form = MyEntries.objects.get(id=id)    
    context = {'form': form}
    return render(request, "encyclopedia/detail_entry.html", context)

def update_entry(request, id):
    context = {}
    obj = get_object_or_404(MyEntries, id = id) 
    form = EntryForm(request.POST or None, instance = obj)
    if form.is_valid(): 
        title = form.cleaned_data.get('title')
        content = form.cleaned_data.get('content')
        form.save() 
        return HttpResponseRedirect("/entry/"+id) 

    context["form"] = form   
    return render(request, "encyclopedia/update_entry.html", context) 


def random_entry(request):
    mylist = MyEntries.objects.all()
    mychoice = random.choice(mylist)
    content = markdown2.markdown(mychoice.content)
    return render(request, 'encyclopedia/random_entry.html', 
        {'mychoice': mychoice, 'content': content})

