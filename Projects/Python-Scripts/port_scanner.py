#!/usr/bin/env python3
"""
Simple Port Scanner for Educational Purposes
Based on Python Fundamentals: Variables, Conditionals, Loops, Functions, and File Operations
"""

import socket
import time

# Function to scan a single port (using Functions concept)
def scan_port(ip_address, port, timeout=1.0):
    """
    Attempt to connect to a specific port on a target IP address.
    Returns True if port is open, False if closed, and None on error.
    """
    try:
        # Create a socket object (Using built-in module)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        
        # Try to connect to the port
        result = sock.connect_ex((ip_address, port))
        sock.close()
        
        # Check if port is open (Using Conditionals concept)
        if result == 0:
            return True
        else:
            return False
            
    except socket.error:
        return None

# Function to resolve hostname to IP
def get_ip_address(hostname):
    """
    Convert a hostname to an IP address using socket module.
    """
    try:
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except socket.gaierror:
        print(f"[ERROR] Could not resolve hostname: {hostname}")
        return None

# Function to get service name for a port
def get_service_name(port):
    """
    Try to get the service name for a given port number.
    """
    try:
        service_name = socket.getservbyport(port)
        return service_name
    except:
        return "unknown"

# Main function (organizing our code)
def main():
    print("=" * 50)
    print("        PYTHON PORT SCANNER")
    print("=" * 50)
    print("Educational tool - Scan responsibly!")
    print()
    
    # Get user input (Using Input/Output concept)
    target_host = input("Enter target hostname or IP: ").strip()
    
    # Validate input
    if not target_host:
        print("[ERROR] Please provide a target host.")
        return
    
    # Resolve hostname to IP
    target_ip = get_ip_address(target_host)
    if target_ip is None:
        return
    
    print(f"Target IP: {target_ip}")
    print()
    
    # Get port range from user
    port_input = input("Enter port or range (e.g., 80 or 20-100): ").strip()
    
    # Process port range (Using Variables & Conditionals concepts)
    if "-" in port_input:
        try:
            start_port, end_port = map(int, port_input.split("-"))
            if start_port > end_port:
                print("[ERROR] Start port must be less than end port.")
                return
        except ValueError:
            print("[ERROR] Invalid port range format. Use 'start-end' (e.g., 20-100).")
            return
    else:
        try:
            start_port = end_port = int(port_input)
        except ValueError:
            print("[ERROR] Please enter a valid port number.")
            return
    
    # Validate port numbers
    if start_port < 1 or end_port > 65535:
        print("[ERROR] Ports must be between 1 and 65535.")
        return
    
    # Ask for timeout
    try:
        timeout = float(input("Enter timeout in seconds (default 1.0): ") or "1.0")
    except ValueError:
        print("[ERROR] Please enter a valid number for timeout.")
        return
    
    print()
    print(f"Scanning {target_host} ({target_ip})")
    print(f"Port range: {start_port}-{end_port}")
    print(f"Timeout: {timeout} seconds")
    print("-" * 50)
    
    # List to store open ports
    open_ports = []
    
    # Start the scan (Using Loops concept)
    start_time = time.time()
    
    print("Scanning ports...")
    for port in range(start_port, end_port + 1):
        result = scan_port(target_ip, port, timeout)
        
        if result is True:
            service = get_service_name(port)
            print(f"Port {port}/tcp is OPEN ({service})")
            open_ports.append(port)
        elif result is None:
            print(f"Port {port}/tcp: Error scanning")
    
    # Calculate execution time
    end_time = time.time()
    scan_time = end_time - start_time
    
    print("-" * 50)
    print(f"Scan completed in {scan_time:.2f} seconds")
    
    # Display results
    if open_ports:
        print("OPEN PORTS FOUND:")
        for port in open_ports:
            service = get_service_name(port)
            print(f"  {port}/tcp - {service}")
        
        # Ask if user wants to save results (Using File Operations concept)
        save = input("\nWould you like to save results to a file? (y/n): ").lower()
        if save == 'y' or save == 'yes':
            filename = f"portscan_{target_host}_{time.strftime('%Y%m%d_%H%M%S')}.txt"
            
            try:
                with open(filename, 'w') as file:
                    file.write(f"Port Scan Results for {target_host} ({target_ip})\n")
                    file.write(f"Scanned on: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                    file.write(f"Scan duration: {scan_time:.2f} seconds\n")
                    file.write("OPEN PORTS:\n")
                    
                    for port in open_ports:
                        service = get_service_name(port)
                        file.write(f"  {port}/tcp - {service}\n")
                
                print(f"Results saved to {filename}")
            except Exception as e:
                print(f"Error saving file: {e}")
    else:
        print("No open ports found in the specified range.")
    
    print("=" * 50)

# Run the program
if __name__ == "__main__":
    main()
