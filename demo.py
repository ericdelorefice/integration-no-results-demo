from agent import answer
from store import FakeVectorStore
import retriever_before

store = FakeVectorStore(docs=["the Q3 roadmap moves launch to May"], down=True)
docs = retriever_before.retrieve(store, "when is the launch")
print(answer("when is the launch?", docs))
