from django.shortcuts import render
from django.http import request
from rest_framework.views import APIView
from .serializers import PersonSerializer
from .models import Person

def index(request):
    return render(request, "index.html")

class PersonAPIViews(APIView):
    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        #check if data is valid then save else return error
        if serializer.is_valid():
            serializer.save()
            return render(request, "index.html", context={"message": "Save Successful"})
        else:
            return render(request, "index.html", context={"message": "Save Not Successful"})

    def get(self, request, id=None):
        #fetch all persons
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return render(request, "names-list.html", context={"persons": serializer.data})