import requests
file1 = open('input.txt', 'r')
input_ip = file1.readlines()
l="1.2.3.4"
for ip in input_ip:
    
        r = requests.post("https://www.ipvoid.com/ip-to-asn/", headers={"X-Forwarded-IP":l} ,data={'ip':ip})
        #print(r.status_code, r.reason
        with open('output.txt', 'w') as f:
            f.write(r.text)
        o = open("output.txt",'r')
        str="IP: "+ip
        lines = o.readlines()
        c=0
        for line in lines:
            c=c+1
            if str in line:
                print("\n")
                print(lines[c-1][73:])
                print(lines[c])
                print(lines[c+1])
                print("#######################################################")
    