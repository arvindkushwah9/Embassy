from django.shortcuts import render, redirect  

# Create your views here.
from django.http import HttpResponse
from .models import Document
from django.template import loader
from .forms import DocumentForm
from datetime import datetime
from rest_framework import generics
from .models import Document
from .serializers import DocumentSerializer

def index(request):
  documents = Document.objects.all()
  context = {'documents': documents}
  return render(request, 'documents/index.html', context)

def new(request):
  print(request.method)
  if request.method == 'GET':
      form = DocumentForm()
  else:
      form = DocumentForm(request.POST)
      user = request.user
      print("Valid form", form.is_valid())

      if form.is_valid():
          print('valid')
          # title = form.cleaned_data['title']
          # image = form.cleaned_data['image']
          instance = form.save(commit=False)
          instance.creator_id = user.id
          instance.updater_id = user.id
          instance.pub_date = datetime.now()
          instance.update_date = datetime.now()
          instance.save()
          # form.save()
          return redirect('/documents')
  return render(request, "documents/new.html", {'form': form})

def show(request):  
    documents = Document.objects.all()  
    return render(request,"documents/show.html",{'documents':documents})  

def edit(request, id):  
    document = Document.objects.get(id=id)  
    return render(request,'documents/edit.html', {'document':document}) 

def update(request, id):  
    document = Document.objects.get(id=id)  
    form = documentForm(request.POST, instance = document)  
    if form.is_valid():  
        form.save()  
        return redirect("/documents")  
    return render(request, 'documents/edit.html', {'document': document})  

def destroy(request, id):  
    document = Document.objects.get(id=id)  
    document.delete()  
    return redirect("/documents")  

class DocumentList(generics.ListAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class DocumentDetail(generics.RetrieveAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    
class DocumentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer