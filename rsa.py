import sys
sys.set_int_max_str_digits(10000000)

p = 311
q = 317
#公開鍵1
n = p * q
l = (p-1) * (q-1)
#公開鍵2(1よりも大きくてlより小さいかつ、lとの最大公約数が1である数字。3とか65537がよく使われる。)
e = 65537
#秘密鍵(e*d mod l =1 になる数字かつ、1より大きくてlより小さい)
def get_e(e,l):
    for d in range(2,l):
        if (e * d) % l == 1:
            return d

d = get_e(e,l)

#暗号化
#c(暗号文)は、m(平文)をe(公開鍵2)乗してn(公開鍵1)で割った余り。
def encryption(m,e,n):
    c = (m ** e) % n
    
    return c

#復号
#m(平文)は,c(暗号文)をd(秘密鍵)乗したものをn(公開鍵1)で割った余り。
def decryption(c,d,n):
    m = (c ** d) % n
    
    return m


print("暗号化:0 復号:1")
i = input()

if int(i) == 0:
    print(f'あなたの公開鍵1は「{n}」です。')
    print(f'あなたの公開鍵2は「{e}」です。')
    print("暗号化する数値を入力してください:")
    m = input()
    m_int = int(m)
    
    c = encryption(m_int,e,n)
    
    print(f'暗号化結果:{c}')
    
else:
    print(f'あなたの公開鍵1は「{n}」です。')
    print(f'あなたの秘密鍵は「{d}」です。')
    print("復号したい暗号文を縫う力してください:")
    c = input()
    c_int = int(c)
    d_int = int(d)
    
    m = decryption(c_int,d_int,n)
    
    print(m)