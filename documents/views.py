from django.shortcuts import render, redirect  

# Create your views here.
from django.http import HttpResponse
from .models import Document
from django.template import loader
from .forms import DocumentForm
from datetime import datetime
from rest_framework import generics
from .models import Document
from .serializers import DocumentSerializer, DocumentCreateSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

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
          return redirect('/tracking')
  return render(request, "documents/new.html", {'form': form})

def show(request):  
    documents = Document.objects.all()  
    return render(request,"documents/show.html",{'documents':documents})  

def edit(request, id):  
    document = Document.objects.get(id=id)  
    return render(request,'documents/edit.html', {'document':document}) 

def update(request, id):  
    document = Document.objects.get(id=id)  
    form = DocumentForm(request.POST, instance = document)
    if form.is_valid():
        form.save()  
        return redirect("/tracking")  
    return render(request, 'documents/edit.html', {'document': document})  

def destroy(request, id):  
    document = Document.objects.get(id=id)  
    document.delete()  
    return redirect("/documents")  

def approved(request):  
    document = Document.objects.get(id=request.GET.get('id'))  
    document.approved = True
    document.save()  
    return redirect("/admin/documents/document/") 

def disapproved(request):  
    document = Document.objects.get(id=request.GET.get('id'))  
    document.approved = False
    document.save()  
    return redirect("/admin/documents/document/") 

@api_view(["POST"])
def create_document(request):
    serializer = DocumentCreateSerializer(data=request.data)
    print("Data", request.data)
    print("User", request.user.id)
    if serializer.is_valid():
        # user = Document.objects.create(serializer.validated_data)
        serializer.save(creator=request.user, updater=request.user)        
        return Response({"message": "Document createdwwwwwwwww"}) 
    else:
        data = {
          "error": True,
          "errors": serializer.errors,          
        }
        return Response(data) 

@csrf_exempt
@api_view(["GET"])
def tracking(request):
    documents = Document.objects.filter(creator_id=request.user.id)
    # return Response(latest_post_list, status=HTTP_200_OK)
    # the many param informs the serializer that it will be serializing more than a single article.
    serializer = DocumentSerializer(documents, many=True)
    return Response({"documents": serializer.data})


class DocumentList(generics.ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class DocumentDetail(generics.RetrieveAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    
class DocumentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
