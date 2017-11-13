from line import LineClient, LineGroup, LineContact

try:
    client = LineClient("playbotone", "Kongkalikong20")
    #client = LineClient(authToken="EmBP4mgqjEWSSAyDpHqc.PlwVZTTm9mw9Pkts9rZiRa.NFwaEqaIWvkfVY+vp+oyp0im2+v3I4a6Th3RJZ8ZCqE=")
except:
    print "Login Failed"

while True:
    op_list = []

    for op in client.longPoll():
        op_list.append(op)

    for op in op_list:
        sender   = op[0]
        receiver = op[1]
        message  = op[2]
        
        msg = message.text
        receiver.sendMessage("[%s] %s" % (sender.name, msg))

