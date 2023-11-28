from flask import Flask, render_template, request, Response
from mobility import Motor
import threading
import time
import picamera
import io
from gripper import Gripper

app = Flask(__name__)

cmdVel = [0, 0]

SPEEDMOD = 0.2

FORWARDMULT = 100
STEERMULT = 80

cmdDict = {
    "forwardKey" : 0,
    "backwardKey" : 0,
    "leftKey" : 0,
    "rightKey" : 0
}

gripper = Gripper(21)
gripper.open()
global gripperOpen
gripperOpen = True

stopCmds = ["forwardStop", "backwardStop", "leftStop", "rightStop"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/drive', methods=['POST'])
def drive():
    command = request.form['command']

    global cmdVel
    global gripperOpen
    
    if command == "forward":
        cmdVel = [100, 0]
        print(f"Command Received: {command}")
        return
    elif command == "backward":
        cmdVel = [-100, 0]
        print(f"Command Received: {command}")
        return
    elif command == "left":
        cmdVel = [0, 100]
        print(f"Command Received: {command}")
        return
    elif command == "right":
        cmdVel = [0, -100]
        print(f"Command Received: {command}")
        return
    elif command == "stop":
        cmdVel = [0, 0]
        print(f"Command Received: {command}")
        return
    elif command == "gripper":
        if gripperOpen:
            gripper.close()
            gripperOpen = False
            print("closing")
        else:
            gripper.open()
            gripperOpen = True
            print("opening")
    
    if command in cmdDict:
        cmdDict[command] = 1
        print(f"Command Received: {command}")
        
    if command in stopCmds:
        cmdDict[command[:-4] + "Key"] = 0
        print(f"Command Received: {command}")
    
    cmdVel[0] = (FORWARDMULT * cmdDict["forwardKey"]) - (FORWARDMULT * cmdDict["backwardKey"])
    cmdVel[1] = (STEERMULT * cmdDict["leftKey"]) - (STEERMULT * cmdDict["rightKey"])
    
    cmdVel = [max(min(cmd * SPEEDMOD, 100), -100) for cmd in cmdVel]
    
    return 'Command received: ' + command

def gen(camera):
    while True:
        stream = io.BytesIO()
        camera.capture(stream, format='jpeg')
        camera.vflip = True
        stream.seek(0)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + stream.read() + b'\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(picamera.PiCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

def driveThread():
    MotorA = Motor(19, 16)
    MotorB = Motor(20,26)
    global cmdVel
    while True:
        Motor.move(cmdVel[0], cmdVel[1])
        # print(cmdVel)
        time.sleep(0.2)

if __name__ == '__main__':
    # Start drive thread
    threading.Thread(target=driveThread).start()
    # Start web server
    app.run(debug=False, host='0.0.0.0')
