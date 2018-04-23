import hmac

message = b"Hello"
key = b"dckey"
h = hmac.new(key, message, digestmod="md5")
res = h.hexdigest()
print(res)