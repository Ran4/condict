#!/usr/bin/env python3
from typing import Dict, Any

    
def when(x: Any, d: Dict) -> Dict:
    """
    Used to build conditional dicts.
    
    Usage:

    >>> some_dict = {
    ...     "some_mandatory_value": "OK",
    ...     **when(hasattr(user, id), {
    ...         "user_id": user.id,
    ...     })
    ... }
    
    If the `user` object has an `id` attribute, `some_dict` will be
    
        `{"some_mandatory_value": "OK", "user_id": 34}`

    otherwise it will be 
    
        `{"some_mandatory_value": "OK"}` 
    """
    return d if x else {}
