import socket

#connection details
bot_owner = "Laserbear"
nick = "Alfred_Nimoy"
chan = "#Nimoy"
sock = socket.socket()
sock.connect(("irc.foonetic.net",6667))
sock.send("USER " + nick + " 0 * :" + bot_owner + "\r\n")
sock.send("NICK " + nick + "\r\n")

def databasecheck(data): #checks whether data contains trigger
  pass

def trigger_response(trigger): #selects random response corresponding to trigger
  pass
  
def teachable(data): #determines whether a trigger response can be learned
  if "is" in data:
    if not data.startswith("is"):
     learn(data.split("is")[0], data.split(":")[2])
  else:
    return 0

def learn(trigger, response):
  pass

notfoundresponses = ["I dunno, m8", "Looks around nervously"]
replied = 0
while 1:
   replied = 0
   data = sock.recv(1024)
   print data
   if data[0:4] == "PING":
      sock.send(data.replace("PING", "PONG"))
   if data[0]!=':':
      continue
   if data.split(" ")[1] == "001":
      sock.send("MODE " + nick + " +B\r\n")
      sock.send("JOIN " + chan + "\r\n")
  if databasecheck(data)[0] == 1 and not teachable(data):
    sock.send("PRIVMSG " + chan + " :databasecheck(data)[1]\r\n")
  else:
    sock.send("PRIVMSG " + chan + " :" + notfoundresponses[randint(1,len(notfoundresponses))] +"\r\n")
    
