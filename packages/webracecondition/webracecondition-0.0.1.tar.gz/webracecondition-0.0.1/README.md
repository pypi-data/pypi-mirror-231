# webracecondition
> Tiny package to test webraceconditions

## Install
```bash
pip install webracecondition
```

## How to use
```python
from webracecondition import Engine, Request

engine = Engine("https://your-target.com")
for i in range(3):
    engine.add_request(Request("GET", "/demo"))

# Single-packet attack 
for roundtrip in engine.single_packet_attack():
    print(roundtrip)
```

## License
[MIT](LICENSE)