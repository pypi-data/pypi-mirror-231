# python-vagrant-metadata

python-vagrant-metadata is a library for download vagrant box in vagrant cloud or customs site.

```python
import requests
from vagrant_metadata import fetch, forge_metadata_url

metadata = fetch(forge_metadata_url('ubuntu/trusty64'))
url = metadata.url_for_youngest_version('virtualbox')

response = requests.get(url)
if response.ok:
  with open('mybox.box', 'wb') as f:
    f.write(response.content)
```

If you need the checksum of box for specific versions, you can use provider as like
```python
import requests
from vagrant_metadata import fetch, forge_metadata_url

metadata = fetch(forge_metadata_url('ubuntu/trusty64'))
url = metadata.url_for('20190514.0.0','virtualbox')

response = requests.get(url)
if response.ok:
  with open('mybox.box', 'wb') as f:
    f.write(response.content)
```


If you need the checksum of box, you can use provider as like
```python
from vagrant_metadata import fetch, forge_metadata_url

metadata = fetch(forge_metadata_url('ubuntu/trusty64'))
provider = metadata.youngest()['virtualbox']
print(provider.url)
print(provider.checksum)
```

If you need the checksum of box for specific versions, you can use provider as like
```python
from vagrant_metadata import fetch, forge_metadata_url

metadata = fetch(forge_metadata_url('ubuntu/trusty64'))
provider = metadata['20190514.0.0']['virtualbox']
print(provider.url)
print(provider.checksum)
```

If you want only version with the specific provider, you can filtering as like
```python
from vagrant_metadata import fetch, forge_metadata_url

metadata = fetch(forge_metadata_url('ubuntu/trusty64'))
provider = metadata.keep_only_provider('virtualbox').youngest()['virtualbox']
print(provider.url)
print(provider.checksum)
```

# Build package

```python
python3 setup.py bdist_wheel
python3 -m twine upload --skip-existing --repository testpypi dist/*
python3 -m pip install --index-url https://test.pypi.org/simple/ python-vagrant-metadata
```