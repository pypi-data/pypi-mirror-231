from .gql import GraphQLProvider


class TokenProvider:
    def __init__(self, raw_provider: GraphQLProvider):
        self.raw_provider = raw_provider

    def get_transfers(self):
        self.raw_provider.events(filter={})
