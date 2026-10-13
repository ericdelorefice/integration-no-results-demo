"""A tiny stand-in for a vector store client. It can be empty, or it can be down."""


class FakeVectorStore:
    def __init__(self, docs=None, down=False):
        self.docs = docs or []
        self.down = down

    def search(self, query, k=3):
        if self.down:
            raise TimeoutError("vector store did not answer within 5s")
        words = set(query.lower().split())
        hits = [d for d in self.docs if words & set(d.lower().split())]
        return hits[:k]
