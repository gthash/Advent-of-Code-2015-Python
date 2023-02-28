import hashlib

def main():
    count = 0
    result = hashlib.md5(b"ckczppom0")
    while (result.hexdigest()[0:6] != "000000"):
        count += 1
        result = hashlib.md5(bytes("ckczppom" + str(count), "utf-8"))
    print(count)

if __name__ == "__main__":
    main()

