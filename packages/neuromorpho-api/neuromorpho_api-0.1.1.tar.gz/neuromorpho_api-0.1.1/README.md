neuromorpho-api
===============

Querying the [neuromorpho.org](https://neuromorpho.org/) database in Python
with [requests](https://pypi.org/project/requests/).

## Installation

```bash
pip install neuromorpho-api
```

## Quickstart

```python
>>> from neuromorpho_api import requestor as requests

>>> neuron_endpoint = "https://neuromorpho.org/api/neuron/"
>>> resp = requests.get(neuron_endpoint + "fields")
>>> resp.json()
{'Neuron Fields': ['neuron_id',
  'neuron_name',
  'archive',
  'age_scale',
  'gender',
  ...
```

## What is this package?

The `neuromorpho-api` package provides a `requests.Session` instance with a
custom `SSLContext` needed for interacting with
[neuromorpho.org](https://neuromorpho.org/).

### Why can't I just use `requests` directly?

You may see something like the following:

```python
>>> import requests
>>> requests.get("https://neuromorpho.org/api/neuron/id/1")
Traceback (most recent call last)
   ...
SSLError: HTTPSConnectionPool(host='neuromorpho.org', port=443): Max retries exceeded with url: /api/neuron/id/1 (Caused by SSLError(SSLError(1, '[SSL: DH_KEY_TOO_SMALL] dh key too small (_ssl.c:1006)')))
```

It appears the key provided by `neuromorpho.org` is incompatible with the
default Python SSL cipher.
This package works around this issue using [Robin De Schepper's solution
posted on Stack Overflow](https://stackoverflow.com/a/76217135).
At some point in the future, the neuromorpho certificate may (hopefully) be
updated, at which point this package will be archived.
