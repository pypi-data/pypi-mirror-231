import json
import json.decoder


__all__ = [
    'get_json_type', 'JsonDunderEncoder', 'JsonDunderTypeEncoder', 'JsonDunderTypeDecoder', 'JsonDunderTypeCoder',
    'load', 'loads', 'dump', 'dumps', 'JSONDecodeError',
]


load = json.load
loads = json.loads
dump = json.dump
dumps = json.dumps
JSONDecodeError = json.JSONDecodeError


def is_iter(obj):
    try:
        if not isinstance(obj, (str, bytes, bytearray)):
            iter(obj)
            return True
    except TypeError:
        pass
    return False


def get_json_type(obj):
    # Get the name from the class
    return f"{obj.__module__}.{obj.__name__}"


class JsonDunderEncoder(json.JSONEncoder):
    """Simple dunder encoder that does not encode types."""
    def use(self):
        json._default_encoder = self
        return self

    def default(self, obj):
        if hasattr(obj, "__json__"):
            return obj.__json__()
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)


class JsonDunderTypeEncoder(JsonDunderEncoder):
    """Json dunder encoder that adds a decoder type key if the object has a `__from_json__` method."""
    VALUES_KEY = "_values_"
    get_json_type = staticmethod(get_json_type)

    def default(self, obj):
        if hasattr(obj, "__json__"):
            d = obj.__json__()
            if hasattr(obj.__class__, "__from_json__"):
                if isinstance(d, dict):
                    if "__json_type__" not in d:
                        d["__json_type__"] = self.get_json_type(obj.__class__)
                else:
                    d = {"__json_type__": self.get_json_type(obj.__class__), self.VALUES_KEY: d}
            return d

        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)


class JsonDunderTypeDecoder(json.JSONDecoder):
    VALUES_KEY = "_values_"

    def use(self):
        json._default_decoder = self
        return self

    def __init__(self, *objs, **kwargs):
        super().__init__(**kwargs)

        self.dunder_objs = {}
        for obj in objs:
            self.register(obj)

        if self.object_hook is None:
            self.object_hook = self._object_hook

    get_json_type = staticmethod(get_json_type)

    def register(self, obj):
        if not hasattr(obj, "__from_json__"):
            raise AttributeError(
                "Decodable json dunder types require a '__from_json__' classmethod."
            )

        name = self.get_json_type(obj)
        if name not in self.dunder_objs:
            self.dunder_objs[name] = obj
        return obj

    def deregister(self, obj):
        if isinstance(obj, str):
            name = obj
        else:
            name = self.get_json_type(obj)
        self.dunder_objs.pop(name, None)

    def _object_hook(self, obj):
        try:
            name = obj.pop("__json_type__", None)
            if not name:
                raise KeyError("Not a json dunder type. No key '__json__type__'.")
            if isinstance(obj, dict) and len(obj) == 2 and self.VALUES_KEY in obj:
                obj = obj[self.VALUES_KEY]
            decoder = self.dunder_objs[name].__from_json__
        except (KeyError, AttributeError):
            return obj
        else:
            return decoder(obj)

    def _nested_object_hook(self, obj):
        if isinstance(obj, dict):
            # Decode nested object first
            for k, v in obj.items():
                obj[k] = self._nested_object_hook(v)

            # Decode this object
            obj = self._object_hook(obj)

        elif is_iter(obj):
            # Decode nested object
            out = []
            for o in obj:
                out.append(self._nested_object_hook(o))

        return obj

    def decode(self, s, _w=json.decoder.WHITESPACE.match):
        """Return the Python representation of ``s`` (a ``str`` instance
        containing a JSON document).

        """
        obj, end = self.raw_decode(s, idx=_w(s, 0).end())
        end = _w(s, end).end()
        if end != len(s):
            raise json.JSONDecodeError("Extra data", s, end)

        return self._nested_object_hook(obj)


class JsonDunderTypeCoder(JsonDunderTypeDecoder, JsonDunderTypeEncoder):
    def use(self):
        json._default_encoder = self
        json._default_decoder = self
        return self

    def __init__(self, *obj, **kwargs):
        encoder_keys = [
            "skipkeys",
            "ensure_ascii",
            "check_circular",
            "allow_nan",
            "sort_keys",
            "indent",
            "separators",
            "default",
        ]
        other = {k: kwargs.pop(k) for k in list(kwargs.keys()) if k in encoder_keys}
        JsonDunderTypeEncoder.__init__(self, **other)
        JsonDunderTypeDecoder.__init__(self, *obj, **kwargs)
