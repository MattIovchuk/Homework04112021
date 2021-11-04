worklist = []

list_of_users = []
list_of_users.append('Head')
first_message = 'Welcome to test chat!'
first_send = list_of_users[0] + ' : ' + first_message
worklist.append(first_send)

def send_message(chatname, message) :
  send = chatname + ' : ' + message
  worklist.append(send)

def create(create_name):
  list_of_users.append(create_name)
  send_message(create_name, 'I am joined the chat!')
  your_name = create_name

def reading():
  for messages in worklist:
    print(messages)
  send_message(list_of_users[0], 'The reading command was carried out.')

def update(chatname, message):
  search = list_of_users.count(chatname)
  if search > 0 :
    send_message(chatname, message)
  else :
    send_message(list_of_users[0], 'The username was not found in the chat. Please create this user using the (create(%your username%)) command.')

def delete(chatname):
  global worklist
  del_marker = chatname + ' : '
  for i in range (len(worklist)-1) :
    if del_marker in worklist[i-1]:
      del worklist[i-1]
  send_message(list_of_users[0], chatname + ' was removed from the chat.')
  for i in range(list_of_users.count(chatname)):
    list_of_users.remove(chatname)