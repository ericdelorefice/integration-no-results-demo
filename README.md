# integration-no-results-demo

Companion code for the article "Your Integration Says 'No Results.' It Means 'I Failed.'"

A tiny retriever sits between an agent and a fake vector store. When the store is down, the
original retriever catches the error and returns `[]`, so the agent tells the user there is
nothing in their documents. The fixed retriever logs the error and raises instead.

Run the demo (the swallowing version answering a question about a document that exists):

    python demo.py

Run the tests against the fixed retriever (3 pass):

    pip install pytest
    pytest -q

Run the same tests against the original retriever (the failure test fails, the two controls pass):

    RETRIEVER=before pytest -q

No network, no API keys, no real vector store. Synthetic data only.
