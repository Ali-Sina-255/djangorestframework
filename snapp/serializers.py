from rest_framework import serializers
from .models import Books, Author


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = "__all__"

    def validate(self, attrs):
        print('validate function is clled !')
        return attrs


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = "__all__"
