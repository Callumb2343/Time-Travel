import time
import socket

def main():
    # set x,y,z to be 0 (3D Space)
    x = 0
    y = 0
    z = 0
    # set w,v,u to be time for w, v and u for perpendicular time
    w = time.time()
    v = time.time()
    u = time.time()

    # Define the coordinates for x,y,z,w,v,u
    MyUser = f"Defined Coordinates: {x, y, z, w, v, u}"

    # define 2 functions: 1 function that contains x,y,z and another that contains w,v,u
    def D1(x, y, z):
        return [x, y, z]

    def D2(w, v, u):
        return [w, v, u]

    # Create an array of the function of (w,v,u) and make the array equal to the (x,y,z) function
    myArray = D1(x, y, z)

    # Make the 2 functions equal each other, enabling (x,y,z)==(w,v,u). This plots
    # (x,y,z) coordinates inside an array of (w,v,u)
    myArray.extend(D2(w,v,u))

    # Create an input for the coordinates of x,y,z,w,v,u and get the user to have to
    # plug in the coordinates for where they wish to communicate to
    CommunicationInput = input("Enter the coordinates for where you would like to communicate to: {x, y, z, w, v, u}")

    # Create another input so that the user can also enter the dimension code to scan for
    # the coordinates of x,y,z,w,v,u
    DimensionCodeScanner = input("Enter the dimension code: {x, y, z, w, v, u}")

    # Print the current coordinates of the dimension the user is located in by making (x,y,z,w,v,u) equal to 0
    MyCurrentCoordinates = (x, y, z, w, v, u) == 0
    print(MyCurrentCoordinates)

    # create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # get local machine name
    host = socket.gethostname()

    port = 9999

    # connection to hostname on the port
    client_socket.connect((host,port))

    # receive data from the server
    data = client_socket.recv(1024)

    print(f"Received data: {data.decode('utf-8')}")

    # close the socket
    client_socket.close()

if __name__ == "__main__":
    main()
