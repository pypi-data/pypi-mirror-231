===========
json_dunder
===========

Encdoe objects with a __json__ dunder method and decode objects with a __from_json__ dunder method.


.. code-block:: python

    import json_dunder

    # Use tells json to use this class
    coder = json_dunder.JsonDunderTypeCoder().use()

    @coder.register
    class A:
        def __init__(self, x):
            self.x = x

        def __eq__(self, other):
            if isinstance(other, self.__class__):
                return self.x == other.x
            return False

        def __json__(self):
            return {"x": self.x}

        @classmethod
        def __from_json__(cls, d: dict):
            return cls(**d)

    @coder.register
    class B:
        def __init__(self, a, y):
            self.a = a
            self.y = y

        def __eq__(self, other):
            if isinstance(other, self.__class__):
                return self.a == other.a and self.y == other.y
            return False

        def __json__(self):
            return {"a": self.a, "y": self.y}

        @classmethod
        def __from_json__(cls, d: dict):
            return cls(**d)

    a = A(1)
    b = B(a, 2)

    sa = json_dunder.dumps(a)
    assert sa == '{"x": 1, "__json_type__": "__main__.A"}'

    sb = json_dunder.dumps(b)
    assert sb == '{"a": {"x": 1, "__json_type__": "__main__.A"}, "y": 2, "__json_type__": "__main__.B"}'

    obj = json_dunder.loads(sa)
    assert obj == a

    obj = json_dunder.loads(sb)
    assert obj.a == a
    assert obj == b


Install
=======

.. code-block::

    pip install json_dunder