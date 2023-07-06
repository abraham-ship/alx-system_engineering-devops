# Networking basics #0
## General
* Allowed editors: vi, vim, emacs<br>
* All your Bash script files will be interpreted on Ubuntu 20.04 LTS<br>
* All your files should end with a new line<br>
* A README.md file, at the root of the folder of the project, is mandatory<br>
* All your Bash script files must be executable<br>
* Your Bash script must pass shellcheck without any error<br>
* The first line of all your Bash scripts should be exactly #!/usr/bin/env bash<br>
* The second line of all your Bash scripts should be a comment explaining what is the script doing<br>

## Task 0.
Questions:<br>

What is the OSI model?<br>

1.	Set of specifications that network hardware manufacturers must respect<br>
2.	The OSI model is a conceptual model that characterizes the communication functions of a telecommunication system without regard to their underlying internal structure and technology<br>
3.	The OSI model is a model that characterizes the communication functions of a telecommunication system with a strong regard for their underlying internal structure and technology<br>
How is the OSI model organized?<br>

1.	Alphabetically<br>
2.	From the lowest to the highest level<br>
3.	Randomly<br>

## Task 1.
Questions:<br>

What type of network a computer in local is connected to?<br>

1.	Internet<br>
2.	WAN<br>
3.	LAN<br>
What type of network could connect an office in one building to another office in a building a few streets away?<br>

1.	Internet<br>
2.	WAN<br>
3.	LAN<br>
What network do you use when you browse www.google.com from your smartphone (not connected to the Wifi)?<br>

1.	Internet<br>
2.	WAN<br>
3.	LAN<br>

## Task 2.
Questions:<br>

What is a MAC address?<br>

1.	The name of a network interface<br>
2.	The unique identifier of a network interface<br>
3.	A network interface<br>
What is an IP address?<br>

1.	Is to devices connected to a network what postal address is to houses<br>
2.	The unique identifier of a network interface<br>
3.	Is a number that network devices use to connect to networks<br>

## Task 3.
Questions:<br>

Which statement is correct for the TCP box:<br>
1.	It is a protocol that is transferring data in a slow way but surely<br>
2.	It is a protocol that is transferring data in a fast way and might loss data along in the process<br>
Which statement is correct for the UDP box:<br>
1.	It is a protocol that is transferring data in a slow way but surely<br>
2.	It is a protocol that is transferring data in a fast way and might loss data along in the process<br>
Which statement is correct for the TCP worker:<br>
1.	Have you received boxes x, y, z?<br>
2.	May I increase the rate at which I am sending you boxes?<br>

## Task 4.
Write a Bash script that displays listening ports:<br>

*	That only shows listening sockets<br>
*	That shows the PID and name of the program to which each socket belongs<br>
Example:<br>
```bash
sylvain@ubuntu$ sudo ./4-TCP_and_UDP_ports
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 *:sunrpc                *:*                     LISTEN      518/rpcbind
tcp        0      0 *:ssh                   *:*                     LISTEN      1240/sshd
tcp        0      0 *:32938                 *:*                     LISTEN      547/rpc.statd
tcp6       0      0 [::]:sunrpc             [::]:*                  LISTEN      518/rpcbind
tcp6       0      0 [::]:ssh                [::]:*                  LISTEN      1240/sshd
tcp6       0      0 [::]:33737              [::]:*                  LISTEN      547/rpc.statd
udp        0      0 *:sunrpc                *:*                                 518/rpcbind
udp        0      0 *:691                   *:*                                 518/rpcbind
udp        0      0 localhost:723           *:*                                 547/rpc.statd
udp        0      0 *:60129                 *:*                                 547/rpc.statd
udp        0      0 *:3845                  *:*                                 562/dhclient
udp        0      0 *:bootpc                *:*                                 562/dhclient
udp6       0      0 [::]:47444              [::]:*                              547/rpc.statd
udp6       0      0 [::]:sunrpc             [::]:*                              518/rpcbind
udp6       0      0 [::]:50038              [::]:*                              562/dhclient
udp6       0      0 [::]:691                [::]:*                              518/rpcbind
Active UNIX domain sockets (only servers)
Proto RefCnt Flags       Type       State         I-Node   PID/Program name    Path
unix  2      [ ACC ]     STREAM     LISTENING     7724     518/rpcbind         /run/rpcbind.sock
unix  2      [ ACC ]     STREAM     LISTENING     6525     1/init              @/com/ubuntu/upstart
unix  2      [ ACC ]     STREAM     LISTENING     8559     835/dbus-daemon     /var/run/dbus/system_bus_socket
unix  2      [ ACC ]     STREAM     LISTENING     9190     1087/acpid          /var/run/acpid.socket
unix  2      [ ACC ]     SEQPACKET  LISTENING     7156     378/systemd-udevd   /run/udev/control
sylvain@ubuntu$
```

## Task 5.
Write a Bash script that pings an IP address passed as an argument.<br>

Requirements:<br>

*	Accepts a string as an argument<br>
*	Displays Usage: 5-is_the_host_on_the_network {IP_ADDRESS} if no argument passed<br>
*	Ping the IP 5 times<br>
Example:<br>
```bash
sylvain@ubuntu$ ./5-is_the_host_on_the_network 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=63 time=12.9 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=63 time=13.6 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=63 time=7.83 ms
64 bytes from 8.8.8.8: icmp_seq=4 ttl=63 time=11.3 ms
64 bytes from 8.8.8.8: icmp_seq=5 ttl=63 time=7.57 ms

--- 8.8.8.8 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4006ms
rtt min/avg/max/mdev = 7.570/10.682/13.679/2.546 ms
sylvain@ubuntu$
sylvain@ubuntu$ ./5-is_the_host_on_the_network
Usage: 5-is_the_host_on_the_network {IP_ADDRESS}
sylvain@ubuntu$ 
```
