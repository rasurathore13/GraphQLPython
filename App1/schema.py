import graphene
from graphene_django import DjangoObjectType
from .models import Book
from django.db.models import Q

class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = ['name','aurthor']

class BookMutation(graphene.Mutation):
    book = graphene.Field(BookType)

    class Arguments:
        name = graphene.String()
        aurthor = graphene.String()

    def mutate(self, info, name, aurthor, **kwargs):
        new_book = Book(name=name, aurthor=aurthor)
        new_book.save()
        return BookMutation(book=new_book)

class Mutation(graphene.ObjectType):
    add_book = BookMutation.Field()

class Query(graphene.ObjectType):
    all_books = graphene.List(BookType, search=graphene.String())
    def resolve_all_books(self, info, search=None, **kwargs):
        if search != None:
            filter = (
                Q(name__iexact=search) | 
                Q(aurthor__iexact=search)
            )
            return Book.objects.filter(filter)
        return Book.objects.all()