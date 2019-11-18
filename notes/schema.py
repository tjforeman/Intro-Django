from django.conf import settings
from graphene_django import DjangoObjectType
import graphene
import .models from Note 

class NoteType(DjangoObjectType):

    class Meta:
        model = note
        interfaces = (graphene.relay.Node,)

    class Query(graphene.ObjectType):

        notes = graphene.List(NoteType)

        def reslove_notes(self, info):
            return Node.objects.all()

    schema = graphene.Schema(query=Query)