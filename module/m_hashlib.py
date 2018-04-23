import hashlib

if __name__ == '__main__':
    str = b"Hello"
    str2 = b"He"
    str3 = b"llo"
    md5 = hashlib.md5()#MD5加密
    md52 = hashlib.md5()
    md5.update(str)
    md5res = md5.hexdigest()
    md52.update(str2)
    md52.update(str3)
    md5res2 = md52.hexdigest()
    print(md5res, md5res == md5res2)
    sha1 = hashlib.sha1()#sha1加密
    sha12 = hashlib.sha1()
    sha1.update(str)
    sha1res = sha1.hexdigest()
    sha12.update(str2)
    sha12.update(str3)
    sha12res2 = sha12.hexdigest()
    print(sha1res, sha1res == sha12res2)
    sha256 = hashlib.sha256() #sha256加密
    sha2562 = hashlib.sha256()
    sha256.update(str)
    sha256res = sha256.hexdigest()
    sha2562.update(str2)
    sha2562.update(str3)
    sha2562res = sha2562.hexdigest()
    print(sha256res, sha256res == sha2562res)
