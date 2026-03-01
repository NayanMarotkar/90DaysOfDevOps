Day 15 – Networking Concepts: DNS, IP, Subnets & Ports
Task 1 – DNS
When I type google.com in a browser:

Browser asks DNS server to resolve the domain.
DNS returns an IP address.
Browser connects to that IP using TCP.
Then HTTP/HTTPS request is sent.
DNS Record Types:

A → Maps domain to IPv4 address
AAAA → Maps domain to IPv6 address
CNAME → Alias to another domain
MX → Mail exchange server
NS → Name server for domain
Command: dig google.com

Observation: Found A record with public IP and TTL value.Public IP: 142.251.211.14 TTL: 263 seconds

Task 2 – IP Addressing
IPv4: 32-bit address written as 4 octets (e.g., 192.168.1.10)

Public IP: Accessible on internet (e.g., 8.8.8.8)

Private IP: Used inside local networks (e.g., 192.168.1.5)

Private ranges: 10.0.0.0/8 172.16.0.0 – 172.31.255.255 192.168.0.0/16

Command: ip addr show

Observation: My system IP is private 172.31.x.x/20) it also showing scop is dynamic if instance is rebooted 
it will change unless we use elastic ip addr. MAC addr - 02:79:67:46:20:77 

Task 3 – CIDR & Subnetting
/24 means: Subnet mask 255.255.255.0 Total IPs: 256 Usable hosts: 254

/16: Subnet mask 255.255.0.0 Total IPs: 65,536 Usable hosts: 65,534

/28: Subnet mask 255.255.255.240 Total IPs: 16 Usable hosts: 14

Why subnet? To divide large networks into smaller manageable parts.

CIDR Table
CIDR | Subnet Mask | Total IPs | Usable Hosts /24 | 255.255.255.0 | 256 | 254 /16 | 255.255.0.0 | 65536 | 65534 /28 | 255.255.255.240 | 16 | 14

Task 4 – Ports
Port is a logical endpoint for communication.

Common Ports:

22 → SSH 80 → HTTP 443 → HTTPS 53 → DNS 3306 → MySQL 6379 → Redis 27017 → MongoDB

Command: ss -tulpn

Observation: Port 22 listening (SSH service).

Task 5 – Putting It Together
curl http://myapp.com:8080 involves: DNS resolution → IP routing → TCP connection → Port 8080 → Application response.

App can't reach DB 10.0.1.50:3306:

Check network connectivity (ping)
Check port open (nc / telnet)
Check firewall/security group
Check DB service status
What I Learned
