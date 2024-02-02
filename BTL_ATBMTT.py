from tkinter import *
from tkinter import filedialog
import random
import base64
import codecs

window = Tk()
window.title("Mã Hóa RSA")
window.geometry('1400x600')

#global ban_ma 

# tạo khóa
def hamsoOle():
    p = int(text_SNT_p.get("1.0", "end-1c"))
    q = int(text_SNT_q.get("1.0", "end-1c"))
    phiN = (p - 1) * (q - 1)
    text_phiN.delete("1.0", "end")
    text_phiN.insert("1.0", str(phiN))

def tinh_modulo_n():
    p = int(text_SNT_p.get("1.0", "end-1c"))
    q = int(text_SNT_q.get("1.0", "end-1c"))
    n = p*q
    text_moduloN.delete("1.0", "end")
    text_moduloN.insert("1.0", str(n))

def Check_NTCN(a, b):
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            return False
    return True
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_random_prime():
    while True:
        random_num = random.randint(2, 1000)  # Giới hạn số nguyên tố từ 2 đến 1000 (có thể thay đổi theo nhu cầu)
        if is_prime(random_num):
            return random_num
def AutoCreatp_q():
    text_SNT_p.delete("1.0", "end")
    text_SNT_q.delete("1.0", "end")
    p = generate_random_prime();
    q = generate_random_prime();
    text_SNT_p.insert("1.0", str(p));
    text_SNT_q.insert("1.0", str(q));
    
def tudong():
    AutoCreatp_q()
    tinh_modulo_n()
    hamsoOle()
    find()
    find_khoaA()
    input_Kpub_Kpri()

 
#tìm khóa b   
def find_khoaB(phiN):
    while True:
        khoaB = random.randrange(2, 101)
        if Check_NTCN(khoaB, phiN)== TRUE and khoaB <phiN :
            return khoaB

# Sử dụng hàm find_khoaB và gán giá trị vào text_khoaB
def find():
    text_khoaB.delete("1.0", "end")
    phiN_value = int(text_phiN.get("1.0", "end-1c"))
    khoaB_value = find_khoaB(phiN_value)
    text_khoaB.insert("1.0", str(khoaB_value))
#tim ptu nghich dao 
def TimpPtuNgichDao(a,b):
    original_b = b
    x, y = 0, 1
    last_x, last_y = 1, 0
    while b != 0:
        thuong = a // b #chia lấy phần nguyên
        a, b = b, a % b #hoán đổi a và b, gán b = a % b
        x, last_x = last_x - thuong * x, x
        y, last_y = last_y - thuong * y, y
    return (last_x % original_b + original_b) % original_b  
def find_khoaA():
    text_khoaA.delete("1.0", "end")
    phiN_value = int(text_phiN.get("1.0", "end-1c"))
    khoaB_value = int (text_khoaB.get("1.0", "end-1c"))
    khoaA_value = TimpPtuNgichDao(khoaB_value,phiN_value)
    text_khoaA.insert("1.0", str(khoaA_value))
def input_Kpub_Kpri():
    #input vào ô khóa public
    text_khoaPublic.delete("1.0", "end")
    khoaB_value = int (text_khoaB.get("1.0", "end-1c"))
    n= int (text_moduloN.get("1.0", "end-1c"))
    text_khoaPublic.insert("1.0", "{ "+str(khoaB_value) + ", "+ str(n)+" }")

    #input vào ô khóa private
    text_KhoaPri.delete("1.0", "end")
    khoaA_value = int (text_khoaA.get("1.0", "end-1c"))
    p = int(text_SNT_p.get("1.0", "end-1c"))
    q = int(text_SNT_q.get("1.0", "end-1c"))
    text_KhoaPri.insert( "1.0","{ "+str(khoaA_value) + ", "+ str(p)+", "+ str(q)+" }") 
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
    if file_path:
        with codecs.open(file_path, 'r', 'utf-8') as file:
            content = file.read()
            text_banro.delete('1.0', END)  # Xóa nội dung hiện tại của text_banma
            text_banro.insert(END, content)  # Chèn nội dung từ file vào text_banma
def open_file2():
    file_path = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
    if file_path:
        with codecs.open(file_path, 'r', 'utf-8') as file:
            content = file.read()
            text_banma2.delete('1.0', END)  # Xóa nội dung hiện tại của text_banma
            text_banma2.insert(END, content)  # Chèn nội dung từ file vào text_banma            
def save_to_file1():
    content = text_banma.get("1.0", "end-1c")  # Lấy nội dung từ text_banma
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")  # Chọn đường dẫn tệp tin để lưu
    if file_path:
        with open(file_path, "w") as file:
            file.write(content)
def save_to_file2():
    content = text_banro2.get("1.0", "end-1c")  # Lấy nội dung từ text_banro
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")  # Chọn đường dẫn tệp tin để lưu
    if file_path:
        with open(file_path, "w") as file:
            file.write(content)            
#mã hóa ký tự
def ma_hoa_ascii():
    ban_ro = text_banro.get("1.0", "end-1c")  # Lấy nội dung bản rõ từ ô text_banro
    ban_ma = []  # Mảng để lưu bản mã

    for char in ban_ro:
        ascii_value = ord(char)  # Chuyển đổi ký tự thành giá trị ASCII
        ban_ma.append(ascii_value)  # Thêm giá trị ASCII vào mảng bản mã

    return ban_ma
def doi_co_so():
    #chuyen b sang he nhi phan
    a = []
    khoaB_value = int (text_khoaB.get("1.0", "end-1c"))
    while khoaB_value > 0:
        a.append(khoaB_value % 2)
        khoaB_value //= 2
    return a
def doi_co_so2():
    #chuyen a sang he nhi phan
    a = []
    khoaA_value = int (text_khoaA.get("1.0", "end-1c"))
    while khoaA_value > 0:
        a.append(khoaA_value % 2)
        khoaA_value //= 2
    return a
def binh_phuong_va_nhan():
    mahoaAsc = ma_hoa_ascii()
    array = []
    n_value = int (text_moduloN.get("1.0", "end-1c"))
    A = doi_co_so()
    
    for j in range(0, len(mahoaAsc), 1):
        p = 1
        for i in range(len(A) - 1, -1, -1):
            if A[i] == 0:
                p = (p * p) % n_value
            else:
                p = (((p * p) % n_value) * mahoaAsc[j]) % n_value
        array.append(p)
    return array

def chuyenMangSoNguyen_SangBase64():
    ban_ro = ""  # Chuỗi để lưu bản rõ
    array = binh_phuong_va_nhan()
    for ascii_value in array:
        base64_value = base64.b64encode(str(ascii_value).encode('utf-8'))  # Chuyển đổi số nguyên thành base64
        char = base64_value.decode('utf-8')  # Chuyển đổi giá trị base64 thành chuỗi ký tự
        ban_ro += char  # Thêm ký tự vào chuỗi bản rõ

    return ban_ro
def chuyenMangSoNguyen_SangBase64_returnArray():
    array = binh_phuong_va_nhan()
    ma_base64 = []  # Mảng để lưu các giá trị base64
    
    for ascii_value in array:
        base64_value = base64.b64encode(str(ascii_value).encode('utf-8'))  # Chuyển đổi số nguyên thành base64
        char = base64_value.decode('utf-8')  # Chuyển đổi giá trị base64 thành chuỗi ký tự
        ma_base64.append(char)  # Thêm giá trị base64 vào mảng
        
    return ma_base64
def ChuyenArrayBase64_ArraySoNguyen():
        array = chuyenMangSoNguyen_SangBase64_returnArray()
        so_nguyen = []  # Mảng để lưu các số nguyên
    
        for base64_value in array:
            byte_value = base64.b64decode(base64_value)  # Chuyển đổi base64 thành dãy byte
            ascii_value = int(byte_value.decode('utf-8'))  # Chuyển đổi dãy byte thành chuỗi và sau đó thành số nguyên
            so_nguyen.append(ascii_value)  # Thêm số nguyên vào mảng
        
        return so_nguyen
def binh_phuong_va_nhan2():
    mahoaAsc = ChuyenArrayBase64_ArraySoNguyen()
    #mahoaAsc = binh_phuong_va_nhan()
    array2 = []
    n_value = int (text_moduloN.get("1.0", "end-1c"))
    A = doi_co_so2()
    
    for j in range(0, len(mahoaAsc), 1):
        p = 1
        for i in range(len(A) - 1, -1, -1):
            if A[i] == 0:
                p = (p * p) % n_value
            else:
                p = (((p * p) % n_value) * mahoaAsc[j]) % n_value
        array2.append(p)
    return array2
def giai_ma_ascii2():
    array = binh_phuong_va_nhan2()
    ascii_string = ""  # Chuỗi để lưu các ký tự ASCII
    
    for number in array:
        ascii_char = chr(number)  # Chuyển đổi số nguyên thành ký tự ASCII
        ascii_string += ascii_char  # Thêm ký tự ASCII vào chuỗi
        
    return ascii_string
#hàm sự kiện cho nút tạo khoa
def bt_taokhoa():
    tinh_modulo_n()
    hamsoOle()
    find()
    find_khoaA()
    input_Kpub_Kpri()
#hàm sự kiên cho nút mã hóa 
def mahoa(): 
    
    text_banma.delete("1.0", "end")
    banma_value = chuyenMangSoNguyen_SangBase64() 
    text_banma.insert("1.0", str(banma_value))

def giaima():
    text_banro2.delete("1.0", "end") 
    banro_value = giai_ma_ascii2()
    text_banro2.insert("1.0", str(banro_value))

def chuyen():
    a =  text_banma.get("1.0", "end-1c")
    text_banma2.delete("1.0", "end") 
    text_banma2.insert("1.0", a)
    
#liệt kê các đối tượng xuất hiện 
#tạo 1 gợi ý
TaoKhoa_label = Label(window, text="TẠO KHÓA", foreground="Green", font=("Times New Roman", 15))

suggest_label = Label(window, text="Gợi ý cặp {p,q} ={691, 701}, {107, 199}", foreground="gray", font=("Times New Roman", 13))

SNTp_label= Label(window, text="Số nguyên tố bí mật p: ", foreground="black", font=("Times New Roman", 13))
text_SNT_p = Text(width="15", height="1",font=("Times New Roman", 12))
SNTq_label= Label(window, text="Số nguyên tố bí mật q: ", foreground="black", font=("Times New Roman", 13))
text_SNT_q = Text(width="15", height="1",font=("Times New Roman", 12))
phiN_label= Label(window, text=" Φn = (p-1)*(q-1): ", foreground="black", font=("Times New Roman", 13))
text_phiN = Text(width="15", height="1",font=("Times New Roman", 12))
moduloN_label= Label(window, text=" n = p * q = ", foreground="black", font=("Times New Roman", 13))
text_moduloN = Text(width="15", height="1",font=("Times New Roman", 12))
khoaB_label= Label(window, text=" Khóa mã hóa b: ", foreground="black", font=("Times New Roman", 13))
text_khoaB = Text(width="15", height="1",font=("Times New Roman", 12))
khoaA_label= Label(window, text=" Khóa giải mã a: ", foreground="black", font=("Times New Roman", 13))
text_khoaA = Text(width="15", height="1",font=("Times New Roman", 12))

khoaPublic_label= Label(window, text=" Khóa công khai", foreground="black", font=("Times New Roman", 13))
khoaPublic1_label= Label(window, text=" Kpub = {b,n} = ", foreground="black", font=("Times New Roman", 13))
text_khoaPublic = Text(width="15", height="1",font=("Times New Roman", 12))

khoaPri_label= Label(window, text=" Khóa bí mật", foreground="black", font=("Times New Roman", 13))
khoaPri1_label= Label(window, text=" Kpri = {a,p,q} = ", foreground="black", font=("Times New Roman", 13))
text_KhoaPri = Text(width="15", height="1",font=("Times New Roman", 12))
#các button
bt_taokhoa = Button(text="Tạo Khóa", width="8", height="1", foreground="yellow", background="blue",font=("Arial", 13, "bold"), command=bt_taokhoa)
bt_autotaokhoa = Button(text="Auto tạo khóa", width="12", height="1", foreground="yellow", background="blue",font=("Arial", 13, "bold"),command=tudong)

#màn hình mã hóa
MaHoa_label = Label(window, text="MÃ HÓA", foreground="Green", font=("Times New Roman", 15))
BanRo_label= Label(window, text="Bản rõ: ", foreground="black", font=("Times New Roman", 13))
text_banro= Text(width="20", height="6",font=("Times New Roman", 13))
BanMa_label= Label(window, text="Bản mã: ", foreground="black", font=("Times New Roman", 13))
text_banma= Text(width="20", height="6",font=("Times New Roman", 13))
bt_mahoa = Button(text="Mã hóa", width="8", height="1", foreground="yellow", background="blue",font=("Arial", 13, "bold"), command=mahoa)
bt_input1= Button(text="Input", width="4", height="2", foreground="yellow", background="blue",font=("Arial", 13, "bold"), command=open_file)
bt_inputsave1= Button(text="Save", width="4", height="1", foreground="yellow", background="blue",font=("Arial", 13, "bold"),command=save_to_file1)
bt_inputChange= Button(text="Chuyển", width="6", height="1", foreground="yellow", background="blue",font=("Arial", 13, "bold"),command=chuyen)

#màn hình giải mã
GiaiMa_label = Label(window, text="GIẢI MÃ", foreground="Green", font=("Times New Roman", 15))
BanMa2_label= Label(window, text="Bản mã: ", foreground="black", font=("Times New Roman", 13))
text_banma2= Text(width="20", height="6",font=("Times New Roman", 13))
Banro2_label= Label(window, text="Bản rõ: ", foreground="black", font=("Times New Roman", 13))
text_banro2= Text(width="20", height="6",font=("Times New Roman", 13))
bt_giaima = Button(text="Giải Mã", width="8", height="1", foreground="yellow", background="blue",font=("Arial", 13, "bold"),command=giaima)
bt_input2= Button(text="Input", width="4", height="2", foreground="yellow", background="blue",font=("Arial", 13, "bold"), command=open_file2)
bt_inputsave2= Button(text="Save", width="4", height="1", foreground="yellow", background="blue",font=("Arial", 13, "bold"),command=save_to_file2 )
bt_inputChange2= Button(text="Chuyển", width="6", height="1", foreground="yellow", background="blue",font=("Arial", 13, "bold"))

#hiển thị lên màn hình và vị trí
def displaytaoKhoa():
    TaoKhoa_label.pack()
    TaoKhoa_label.place(x=10,y=10)
    suggest_label.pack(), suggest_label.place(x=10,y =60)
    SNTp_label.pack()
    SNTp_label.place(x=10,y=100)
    text_SNT_p.pack() 
    text_SNT_p.place(x=180, y=100)
    SNTq_label.pack()
    SNTq_label.place(x=10,y=140)
    text_SNT_q.pack() 
    text_SNT_q.place(x=180, y=140)
    phiN_label.pack()
    phiN_label.place(x=10 , y= 180)
    text_phiN.pack()
    text_phiN.place(x=180, y=180 )
    moduloN_label.pack()
    moduloN_label.place(x=10, y = 220)
    text_moduloN.pack()
    text_moduloN.place(x=180, y=220)
    khoaB_label.pack()
    khoaB_label.place(x=10, y =260)
    text_khoaB.pack()
    text_khoaB.place(x=180, y= 260)
    khoaA_label.pack()
    khoaA_label.place(x=10, y =300)
    text_khoaA.pack()
    text_khoaA.place(x=180, y= 300)
    khoaPublic_label.pack()
    khoaPublic_label.place(x=10, y=340)
    khoaPublic1_label.pack()
    khoaPublic1_label.place(x=30, y=370)
    text_khoaPublic.pack()
    text_khoaPublic.place(x=180, y=370)

    khoaPri_label.pack()
    khoaPri_label.place(x=10, y=410)
    khoaPri1_label.pack()
    khoaPri1_label.place(x=30, y=440)
    text_KhoaPri.pack()
    text_KhoaPri.place(x=180, y=440)

    bt_taokhoa.pack()
    bt_taokhoa.place(x=180,y =500)
    bt_autotaokhoa.pack()
    bt_autotaokhoa.place(x=30,y =500)
def displaymahoa():
    MaHoa_label.pack(), MaHoa_label.place(x=600, y= 10)
    BanRo_label.pack(), BanRo_label.place(x=500, y=100)
    text_banro.pack(), text_banro.place(x=580,y=100)
    bt_mahoa.pack(), bt_mahoa.place(x=670, y= 250)
    BanMa_label.pack() , BanMa_label.place(x=500, y= 320)
    text_banma.pack(), text_banma.place(x=580, y= 320)
    bt_input1.pack(), bt_input1.place(x=780,y=150)
    bt_inputsave1.pack(), bt_inputsave1.place(x=600,y=460)
    bt_inputChange.pack(), bt_inputChange.place(x=680,y=460)
def displaygiaima():
    GiaiMa_label.pack(), GiaiMa_label.place(x=1100, y= 10)
    BanMa2_label.pack(), BanMa2_label.place(x=980, y=100)
    text_banma2.pack(), text_banma2.place(x=1060,y=100)
    bt_giaima.pack(), bt_giaima.place(x=1150, y= 250)
    Banro2_label.pack() , Banro2_label.place(x=980, y= 320)
    text_banro2.pack(), text_banro2.place(x=1060, y= 320)
    bt_input2.pack(), bt_input2.place(x=1250,y=150)
    bt_inputsave2.pack(), bt_inputsave2.place(x=1180,y=460)
    #bt_inputChange.pack(), bt_inputChange.place(x=680,y=460)

displaytaoKhoa()
displaymahoa()
displaygiaima()

window.mainloop()