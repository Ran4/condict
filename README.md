# conDict - CONdictional Dictionary

Python library containing functions that helps with conditionally creating dicts.

## Example:

```python
>>> from condict import when
>>> user_id = 42
>>> some_dict = {
... "some_mandatory_value": "OK",
...     **when(user_id, {
...         "user_id": user_id,
...     })
... }
{
    "some_mandatory_value": "OK",
    "user_id": 42,
}
```
