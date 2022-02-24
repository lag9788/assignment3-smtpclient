## File: solution.py
## Name: Luis Grados

from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver,port))
    # Fill in end
    
    recv = clientSocket.recv(1024).decode()
    
    #print(recv) #You can use these print statement to validate return codes from the server.
    #if recv[:3] != '220':
    #   print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv = clientSocket.recv(1024).decode()
    #print(recv1) 
    #if recv1[:3] != '250':
    #    print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    # Fill in start
    mailFrom = "MAIL FROM: <lag98@gmail.com>\r\n"
    clientSocket.send(mailFrom.encode())
    recv = clientSocket.recv(1024)
    recv = recv.decode()
    #print("After MAIL FROM command: "+recv)
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    rcptTo = "RCPT TO: <lag9788@nyu.edu>\r\n"
    clientSocket.send(rcptTo.encode())
    recv = clientSocket.recv(1024)
    recv = recv.decode()
    #print("After RCPT TO command: "+recv)
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    data = "DATA\r\n"
    clientSocket.send(data.encode())
    recv = clientSocket.recv(1024)
    recv = recv.decode()
    #print("After DATA command: "+recv)
    # Fill in end

    # Send message data.
    # Fill in start
    subject = "Subject: Email Test\r\n\r\n" 
    clientSocket.send(subject.encode())
    date = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())
    date = date + "\r\n\r\n"
    clientSocket.send(date.encode())
    clientSocket.send(msg.encode())
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    clientSocket.send(endmsg.encode())
    recv_msg = clientSocket.recv(1024)
    #print("Response after sending message body:"+recv_msg.decode())
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    quit = "QUIT\r\n"
    clientSocket.send(quit.encode())
    recv = clientSocket.recv(1024)
    #print(recv.decode())
    clientSocket.close()
    # Fill in end

if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')


