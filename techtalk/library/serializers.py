from .models import Book
from rest_framework import  serializers

# Serializers define the API representation.
class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'id', 'pages',]