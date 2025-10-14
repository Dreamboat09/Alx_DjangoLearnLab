from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

# Serializer for Author and Book models
class AuthorSerializer(serializers.ModelSerializer):
    # establishing a one-to-many relationship from Author to Book
    book = serializers.StringRelatedField(many=True)
    class Meta:
        model = Author
        fields = ['id', 'name', 'author']


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published_date']

    # Custom validation example
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value