from flask import Flask, render_template, request
from mobility import Motor
import threading
import time

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

stopCmds = ["forwardStop", "backwardStop", "leftStop", "rightStop"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/drive', methods=['POST'])
def drive():
    command = request.form['command']

    global cmdVel
    
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

def driveThread():
    MotorA = Motor(13, 19)
    MotorB = Motor(3,2)
    global cmdVel
    while True:
        Motor.move(cmdVel[0], cmdVel[1])
        print(cmdVel)
        time.sleep(0.2)

if __name__ == '__main__':
    # Start drive thread
    threading.Thread(target=driveThread).start()
    app.run(debug=False, host='0.0.0.0')
