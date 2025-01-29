# Network Traffic Analysis CTF Challenge

This CTF challenge focuses on network traffic analysis. Participants must analyze the generated traffic to answer questions about:
- Protocol identification
- Traffic patterns
- User behavior simulation
- Network forensics

## Challenge Objectives:
1. Identify all protocols being used (HTTP, DNS, FTP, Telnet).
2. Determine the frequency of different types of requests.
3. Map out the simulated user behavior pattern.
4. Find hidden flags in specific traffic patterns.

## Setup
1. **Clone this repository:**
   ```sh
   git clone https://github.com/btrigo/part-I-CTF-challenges.git
   cd part-I-CTF-challenges
2. install dependencies
- pip install -r requirements.txt

3. build the docker container
- docker build -t traffic-gen .

4. run the container
- docker run -d traffic-gen

##Capturing and analyzing traffic

- use Wireshark or tcpdump to capture packets: tcpdump -i eth0 -w capture.pcap

- Open capture.pcap in Wireshark and apply filters:
   -  HTTP traffic: tcp.port == 80
   -  DNS queries: udp.port == 53
   -  FTP commands: tcp.port == 21
   -  Telnet connections: tcp.port == 23
 
## Challenge questions:
1. How many unique domains were queried via DNS?
2. Which HTTP method is used the most?
3. Identify a suspicious FTP command.
4. Extract the hidden flag from Telnet traffic.

5. ##Additional Notes
- The script generates simulated network traffic.
- Ensure your system allows outgoing connections for analysis.
- Modify traffic_generator.py to tweak request frequency and domains.
