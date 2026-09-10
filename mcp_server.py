import sys
import json
from client import TDigest

def main():
    td = TDigest()
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        req = json.loads(line)
        method = req.get("method")
        params = req.get("params", {})
        if method == "add":
            for val in params.get("values", []):
                td.add(val)
            res = {"status": "ok"}
        elif method == "quantile":
            q = td.quantile(params.get("q", 0.5))
            res = {"quantile": q}
        else:
            res = {"error": "unknown method"}
        sys.stdout.write(json.dumps({"id": req.get("id"), "result": res}) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
