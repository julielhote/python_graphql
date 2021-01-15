import graphene
import graphql_jwt

import hackernews.links.schema
import hackernews.users.schema


class Query(hackernews.users.schema.Query, hackernews.links.schema.Query, graphene.ObjectType):
    pass


class Mutation(hackernews.users.schema.Mutation, hackernews.links.schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
