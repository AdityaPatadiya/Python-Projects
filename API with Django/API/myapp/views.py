from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Author
from .serializers import AuthorSerializer


class AuthorDataView(APIView):
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response({
            "name": "J.K. Rowlinr",
            "description": "A author of a wizard story book.",
            "books": [
                {
                    "id": 1,
                    "title": "Harry Potter 1: The Philosopher's Stone.",
                    "chapters": [
                        {"id": 100, "title": "The Boy WHo Lived"},
                        {"id": 101, "title": "The Vanishing Glass"}
                    ]
                }
            ]
        })
