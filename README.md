# IMPORTANT NOTE:
I had not done inter-process communication programming prior to this, and as a result
I consulted the official Python documentation on this topic [here](https://docs.python.org/3/library/socket.html#socket-objects).  

I followed through the examples to understand what was happening, and tried a couple of things.
I also consulted this [guide](https://www.geeksforgeeks.org/computer-networks-set-1/g/), and the
other articles in that series which provided much [source code](https://www.geeksforgeeks.org/simple-chat-room-using-python/). However, there are some edits in order
to satisfy my requirements (regarding HOST and PORT). 

I have left some comments here and there to explain what the parts do.

## How to run
Download the files, and go to the folder where ```server.py``` and ```client.py``` are located.  
Then run:  
```
python server.py
```  
to start the server and (in a new terminal window)  
```
python client.py
```  
to start the client instance.

Also note that currently there is a limit of 5 clients, which you can change if you want to by altering line 29 of ```server.py``` (change ```server.listen(num)```.