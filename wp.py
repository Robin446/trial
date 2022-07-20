from os import sep


with open('/Users/baaghi/Desktop/neer world/whatsapp problem/output2.html','w') as s:
    lines = ['9886579791', '9739522030', '6375017161','3965397612']
    print(*lines, sep="\n")
    for lines in lines:
        s.write(f'<a target="blank"href={"https://api.whatsapp.com/send/?phone=91"+lines+"&text=Namasteji"} >'+lines+'</a> ')