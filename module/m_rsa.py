import rsa

# rsa加密
def rsaEncrypt(strstr):
    # 生成公钥、私钥
    # (pubkey, privkey) = rsa.newkeys(1024)
    with open("public.pem") as pubrd:
        pubkey = rsa.PublicKey.load_pkcs1_openssl_pem(pubrd.read())#加载开头为BEGIN PUBLIC KEY 使用 load_pkcs1_openssl_pem，加载开头为BEGIN RSA PUBLIC KEY使用load_pkcs1
    with open("prvkey.pem") as prvrd:
        privkey = rsa.PrivateKey.load_pkcs1(prvrd.read())
    # 明文编码格式
    content = strstr.encode('utf-8')
    # 公钥加密
    crypto = rsa.encrypt(content, pubkey)
    return (crypto, privkey)


# rsa解密
def rsaDecrypt(str, pk):
    # 私钥解密
    content = rsa.decrypt(str, pk)
    con = content.decode('utf-8')
    return con


(a, b) = rsaEncrypt("hello")
print('加密后密文：')
print(a)
content = rsaDecrypt(a, b)
print('解密后明文：')
print(content)
