import graphene
import App1.schema

class Query(App1.schema.Query,
            graphene.ObjectType):
    pass

class Mutation(App1.schema.Mutation,
                graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)