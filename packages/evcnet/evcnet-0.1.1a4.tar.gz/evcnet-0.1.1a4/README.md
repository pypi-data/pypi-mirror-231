# python-evcnet
Python client to retrieve data from evc-net.com


```python
from evcnet import Evcnet
e = Evcnet(
    url='https://evcompany.evc-net.com',
    username='username@example.com',
    password='s3cret'
)
e.login()
e.total_usage()
{'totalUsage': 5659, 'totalProvided': 4217}
```
