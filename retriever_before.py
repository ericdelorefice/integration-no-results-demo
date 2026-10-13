import logging

log = logging.getLogger(__name__)


def retrieve(store, query):
    try:
        return store.search(query)
    except Exception as e:
        log.warning("search failed, returning no results: %s", e)
        return []
