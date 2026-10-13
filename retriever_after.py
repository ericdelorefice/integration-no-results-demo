import logging

log = logging.getLogger(__name__)


class RetrievalError(RuntimeError):
    """The store could not be searched. This is not the same as finding nothing."""


def retrieve(store, query):
    try:
        return store.search(query)
    except TimeoutError as e:
        log.warning("search failed: %s", e)
        raise RetrievalError(f"could not search the vector store: {e}") from e
