import cv2
import socket

# open the video file
cap = cv2.VideoCapture('DrivingThroughAHugeLEGOCity.mp4')

# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to a specific address and port
server_socket.bind(('localhost', 5001))

# listen for incoming connections
server_socket.listen(1)

# accept a connection
client_socket, client_address = server_socket.accept()

# loop through the frames of the video
while cap.isOpened():

    # read a frame from the video
    ret, frame = cap.read()

    # check if the frame was successfully read
    if ret:

        # convert the frame to bytes
        data = cv2.imencode('.jpg', frame)[1].tobytes()

        # send the frame to the client
        client_socket.sendall(data)

    # if the frame was not successfully read, break the loop
    else:
        break

# release the video capture and sockets
cap.release()
client_socket.close()
server_socket.close()
