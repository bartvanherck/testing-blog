title: Verifying HTTP websockets traffic with wireshark
tags: wireshark
date: 2013-07-26 18:03:00
category: testing
Summary: I really do like the [wireshark](http://www.wireshark.org/) tool. It is a so called network packet analyzer and helped me a lot in the past. For the project where I am working on, there were 2 problems.

I really do like the [wireshark](http://www.wireshark.org/) tool. It is a so called network packet analyzer and helped me a lot in the past. For the project where I am working on, there were 2 problems:

*   Wireshark does not capture data at localhost on windows.
*   Wireshark did not dissect our websocket traffic correctly.

### Sniffing traffic for the localhost interface on windows. ###

The [official wiki of wireshark](http://wiki.wireshark.org/CaptureSetup/Loopback) says it all:

> You can not capture on the local loopback address 127.0.0.1 with a Windows packet capture driver like WinPcap.


This is a problem for me, because I do test on my machine and &nbsp;with the loopback device. This because our application will be running on a machine and never has any access to any network. This means the requirement of many thousands of clients is not for us, but that is another issue.

There is howver another solution for this and that is the use of another tool. This tool is called [RawCap](http://www.netresec.com/?page=RawCap). It is a free command line network sniffer for windows that will be part of my toolbox from now onwords, together with wireshark of course. To run the tool you need administrator privileges, this is normal because the tool connects to the network devices at lowlevel and a normal user normal never can have access to hardware drivers at that level.

The usage of the program is also very simple: Just run it in a terminal and follow the options. There are also commandline options, but to see what they are, you have to check the manual on the [website of RawCap](http://www.netresec.com/?page=RawCap). The program will log all traffic in a file. That file can be opened in wireshark for further investigation.

An example of the terminal output I got and typed in is:

    E:\tools rawcap
    Interfaces:
     0\. 172.16.0.151 Wireless Network Connection Wireless80211
     1\. 172.16.0.153 Local Area Connection Ethernet
     2\. 192.168.6.1 VMware Network Adapter VMnet1 Ethernet
     3\. 192.168.111.1 VMware Network Adapter VMnet8 Ethernet
     4\. 127.0.0.1 Loopback Pseudo-Interface 1 Loopback
    Select interface to sniff [default '0']: 4
    Output path or filename [default 'dumpfile.pcap']:
    Sniffing IP : 127.0.0.1
    File : dumpfile.pcap
    Packets : 15370^C


With this usefull program, problem 1 is solved.

### Dissection of JSON WebSocket traffic ###
It is possible that like in our case, the WebSocket traffic is not at an HTTP port. In our case the traffic is at port 5000\. That port is also used for IPA, or GSM over IP. Because of this problem, our traffic is seen like unreadable data, because the data will not be unmasked.

![dissection json](http://3.bp.blogspot.com/-ODxrLrjgqcg/UfJDFZL0mLI/AAAAAAAAAFs/Rp6jygw4Pe4/s1600/1.png)

Lucky for us there is a solution. Go to the Preferences Window and search for HTTP in the Protocols dropdown. At the right side an option TCP Ports will be available. Here we can add our custom port.

![preferences](http://4.bp.blogspot.com/-iIOO2e007gM/UfJDHdI2DwI/AAAAAAAAAGA/owOIuXx5vRE/s1600/4.png)

That is not enough, because our WebSockets use Json. Search in the same dropdown for Websocket and select in the Dissect websocket text dropdown box the "As json" option.

![websockets settings](http://3.bp.blogspot.com/-7M-J4YnxpeM/UfJDHhKafdI/AAAAAAAAAF8/TbkUoUQ9WO0/s1600/5.png)

After applying our problem has been solved. The json data can be seen as plain text now.

![problem solved](http://4.bp.blogspot.com/-sRKNNjb_nQc/UfJDIsoN3FI/AAAAAAAAAGQ/QVg3UcWkyIU/s1600/6.png)

All the options are there for inspecting the data. Pretty handy for debugging if something is wrong, that wireshark tool.
