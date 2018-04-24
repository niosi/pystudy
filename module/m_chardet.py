# coding=utf-8
import chardet

chinese = "天王盖地虎,小鸡炖蘑菇".encode("gbk")
chres = chardet.detect(chinese)
print(chres)
english = "The tiger, chicken stew mushroom".encode("gbk")
enres = chardet.detect(english)
print(enres)
japanese = "天王蓋地虎、小鶏はきのこ。".encode("euc-jp")
jpres = chardet.detect(japanese)
print(jpres)
