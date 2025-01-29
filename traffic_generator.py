import random
import time
import subprocess
import socket
import http.client
import logging
from datetime import datetime
import threading
from ftplib import FTP
from telnetlib import Telnet

class TrafficGenerator:
    def __init__(self):
        self.logger = self._setup_logging()
        self.common_domains = [
            "example.com", "test.local", "wiki.local", "mail.local", 
            "shop.local", "blog.local", "search.local", "news.local"
        ]
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
            "Mozilla/5.0 (X11; Linux x86_64)"
        ]
        
    def _setup_logging(self):
        logger = logging.getLogger('traffic_gen')
        logger.setLevel(logging.INFO)
        handler = logging.FileHandler('traffic.log')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger

    def generate_http_traffic(self):
        """Generate HTTP/HTTPS requests to simulate web browsing"""
        paths = ["/", "/about", "/contact", "/products", "/services", "/blog"]
        methods = ["GET", "POST", "HEAD"]
        
        while True:
            domain = random.choice(self.common_domains)
            path = random.choice(paths)
            method = random.choice(methods)
            
            try:
                conn = http.client.HTTPConnection(domain, timeout=2)
                headers = {
                    "User-Agent": random.choice(self.user_agents),
                    "Accept": "text/html,application/xhtml+xml",
                    "Accept-Language": "en-US,en;q=0.9"
                }
                conn.request(method, path, headers=headers)
                self.logger.info(f"HTTP {method} request to {domain}{path}")
            except:
                pass
            
            time.sleep(random.uniform(1, 5))

    def generate_dns_traffic(self):
        """Generate DNS queries using socket"""
        while True:
            domain = random.choice(self.common_domains)
            
            try:
                # Using socket for DNS lookups instead of dns.resolver
                socket.gethostbyname(domain)
                self.logger.info(f"DNS query for {domain}")
                
                # Also try to get MX records using nslookup
                try:
                    subprocess.run(['nslookup', '-type=MX', domain], 
                                 capture_output=True, timeout=2)
                    self.logger.info(f"MX record lookup for {domain}")
                except:
                    pass
                    
            except:
                pass
                
            time.sleep(random.uniform(2, 8))

    def generate_ftp_traffic(self):
        """Simulate FTP connections and commands"""
        while True:
            try:
                ftp = FTP('test.local')
                ftp.login('anonymous', 'guest@example.com')
                commands = ['LIST', 'PWD', 'SYST', 'HELP']
                cmd = random.choice(commands)
                ftp.sendcmd(cmd)
                self.logger.info(f"FTP command: {cmd}")
                ftp.quit()
            except:
                pass
                
            time.sleep(random.uniform(10, 20))

    def generate_telnet_traffic(self):
        """Simulate Telnet connections"""
        while True:
            try:
                tn = Telnet('test.local', timeout=2)
                tn.read_until(b"login: ")
                tn.write(b"user\n")
                tn.read_until(b"Password: ")
                tn.write(b"password\n")
                self.logger.info("Telnet connection attempt")
                tn.close()
            except:
                pass
                
            time.sleep(random.uniform(15, 30))

    def run(self):
        """Start all traffic generation threads"""
        threads = [
            threading.Thread(target=self.generate_http_traffic),
            threading.Thread(target=self.generate_dns_traffic),
            threading.Thread(target=self.generate_ftp_traffic),
            threading.Thread(target=self.generate_telnet_traffic)
        ]
        
        for thread in threads:
            thread.daemon = True
            thread.start()
            
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.logger.info("Traffic generation stopped")

if __name__ == "__main__":
    generator = TrafficGenerator()
    generator.run()