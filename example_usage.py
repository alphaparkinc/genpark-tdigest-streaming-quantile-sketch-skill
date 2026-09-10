from client import TDigest

def main():
    print("=== Testing t-Digest Streaming Quantile Sketch ===")
    td = TDigest(delta=50)
    for i in range(1, 101):
        td.add(i)

    q50 = td.quantile(0.5)
    print("Estimated median:", q50)
    assert 40 <= q50 <= 60
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
