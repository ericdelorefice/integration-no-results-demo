import os
import pytest
from store import FakeVectorStore

# RETRIEVER=before runs the tests against the swallowing version.
if os.environ.get("RETRIEVER") == "before":
    from retriever_before import retrieve
    RetrievalError = Exception
else:
    from retriever_after import retrieve, RetrievalError


def test_a_store_that_is_down_raises():
    store = FakeVectorStore(docs=["the Q3 roadmap moves launch to May"], down=True)
    with pytest.raises(RetrievalError):
        retrieve(store, "when is the launch")


def test_an_empty_store_still_returns_nothing():  # control: passes on both versions
    assert retrieve(FakeVectorStore(), "when is the launch") == []


def test_a_healthy_store_still_finds_documents():  # control: passes on both versions
    store = FakeVectorStore(docs=["the Q3 roadmap moves launch to May"])
    assert retrieve(store, "when is the launch") == ["the Q3 roadmap moves launch to May"]
