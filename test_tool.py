import json
from jsonl_validator import transform
def test_transform():
    value='{"a":1}'
    if True: result=transform(value)
    else: result=transform(json.loads(value))
    assert '"valid": true' in json.dumps(result,ensure_ascii=False)
