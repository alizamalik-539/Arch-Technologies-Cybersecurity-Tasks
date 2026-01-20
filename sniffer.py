from scapy.all import sniff, IP
import datetime

def process_packet(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # This creates the text we want to save
        log_entry = f"[{timestamp}] {src_ip} -> {dst_ip} | Protocol: {protocol}\n"
        
        # 1. Print it so you see it in the terminal
        print(log_entry.strip())
        
        # 2. THIS IS THE PART THAT CREATES THE FILE
        # 'a' means 'append' (add to the end of the file)
        with open("packet_log.txt", "a") as f:
            f.write(log_entry)

print("--- Sniffer Started. Saving to packet_log.txt... ---")
sniff(prn=process_packet, store=0)