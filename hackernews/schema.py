import graphene
from graphene_django import DjangoObjectType

from hackernews.links.models import Link


class LinkType(DjangoObjectType):
    class Meta:
        model = Link


class Query(graphene.ObjectType):
    links = graphene.List(LinkType)

    def resolve_links(self, info, **kwargs):
        return Link.objects.all()


schema = graphene.Schema(query=Query)
