import os, shutil, socket, time, re, sys, csv
from datetime import datetime

def main():

    try:
        terminal = start_scanner()
        start_time = time.perf_counter()
        results_tcp, results_udp = scan_target()
        end_time = time.perf_counter()
        duration = end_time - start_time

        summary = build_summary(results_tcp, results_udp, duration)

        table_tcp = format_results_table(results_tcp, "TCP:")
        table_udp = format_results_table(results_udp,"UDP:")

        print(indent_block(format_summary(summary),terminal));print("")
        print(indent_block(table_tcp,terminal));print("")
        print(indent_block(table_udp,terminal));print("")


        print(f'saved .csv > {save_csv_report(make_report_filename(results_tcp[0].get("ip",""),"csv"),results_tcp, results_udp)}')
        print(f'saved .txt > {save_txt_report(make_report_filename(results_tcp[0].get("ip",""),"txt"),results_tcp, results_udp, summary)}')
        print("")

    except KeyboardInterrupt:
        clear_terminal()
        sys.exit("")
    except IndexError:
        clear_terminal()
        print("\n\nNo OPEN ports\n\n".center(terminal))


#-----------------------------
#         output
#-----------------------------

def make_report_filename(ip, extension):
    return f'reports/scan_{ip}_{datetime.now().strftime("%Y%m%d_%H%M%S")}.{extension}'

def save_csv_report(path, results_tcp, results_udp):
    fieldnames=["ip", "port", "protocol", "service", "source", "confidence", "evidence","banner","headers"]

    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for result in results_tcp + results_udp:
            writer.writerow({
                "ip": result.get("ip",""),
                "port": result.get("port",""),
                "protocol": result.get("protocol", ""),
                "service": result.get("service", ""),
                "source": result.get("source",""),
                "confidence": result.get("confidence",""),
                "evidence": result.get("evidence",""),
                "banner":result.get("banner",""),
                "headers": result.get("headers","")
            })
        return path

def save_txt_report(path, results_tcp, results_udp, summary):

    lines=[]
    lines.append(format_summary(summary))
    lines.append("")
    lines.append(format_results_table(results_tcp, "TCP:"))
    lines.append("")
    lines.append(format_results_table(results_udp, "UDP:"))
    lines.append("")

    with open(path, "w", newline="", encoding="utf-8") as file:
        file.write("\n".join(lines))
    return path

#-----------------------------
#         after formatter
#-----------------------------

def indent_block(text, terminal):
    spaces = " " * 2
    return "\n".join(spaces + line for line in text.splitlines())

def format_summary(summary):
    lines=[]
    lines.append("\n\nSCAN SUMMARY")
    lines.append("--------------\n")
    lines.append(f'Open TCP ports: {summary["open_tcp_ports"]}')
    lines.append(f'Open UDP ports: {summary["open_udp_ports"]}')
    lines.append(f'Open ports Total: {summary["open_ports_total"]}')
    lines.append("")
    lines.append(f' Duration: {summary["duration"]}')
    lines.append("")
    lines.append("Services:")


    for service, count in summary["services"].items():
        lines.append(f"{service}:{count}")
    return "\n".join(lines)


def build_summary(results_tcp, results_udp, duration):
    results_all = results_tcp + results_udp

    services = {}
    for result in results_all:
        service = result.get("service","unknown")
        if service in services:
            services[service] +=1
        else:
            services[service] =1

    summary = {
        "open_tcp_ports": len(results_tcp),
        "open_udp_ports": len(results_udp),
        "open_ports_total": len(results_all),
        "duration": f"{duration:.2f}s",
        "services": services
    }
    return summary

def format_result_row(results):

  return f'{results["port"]:<5}| {results["service"]:<15}| {results["source"]:<18}| {results["confidence"].upper():<14}| {results["evidence"].upper():<25}'


def format_results_table(results, kind):


    header = f"\n{"PORT":>1} | {"SERVICE":<14} | {"SOURCE":<17} | {"CONFIDENCE":<13} | {"EVIDENCE":<25}"
    border =  "-"* len(header)
    table = [kind,header,border]
    for result in results:
        if result := format_result_row(result):
            table.append(result)
    return "\n".join(table)


def build_scan_result(ip,port,protocol,service,source,confidence,banner,headers,evidence):
    scan_result = {
        "ip": ip,
        "port": port,
        "protocol": protocol,
        "status": "open",
        "service": service,
        "source": source,
        "confidence": confidence,
        "banner": banner,
        "headers": headers,
        "evidence": evidence
    }
    return scan_result

#-----------------------------
#       first formatter
#-----------------------------


def clean_input(text):

     text = re.sub(r"[^a-zA-Z]", "", text)
     return text.upper()

def resolve_host(host):

    try:
        ip = socket.gethostbyname(host.strip())
    except socket.gaierror:
        return None
    else:
        return ip

def check_host(host):
    if validate(host):
        return True
    else:
        return False


#-----------------------------
#         Logik
#-----------------------------

def extract_header_value(headers,name="server"):
    for row in headers.splitlines():
        if row.lower().startswith(name + ":"):
           return row.split(":",1)[1].strip()
    else:
        return None

def grab_http_headers(host, port, timeout=1.0):

     request = f"HEAD / HTTP/1.0\r\nHost: {host}\r\nConnection: close\r\n\r\n"

     try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            if s.connect_ex((host,port)) != 0:
                return ""

            s.sendall(request.encode("ascii"))
            return s.recv(1024).decode("ascii",errors="replace")
     except:
         return ""

def grab_banner(host,port,timeout):

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            if s.connect_ex((host,port)) != 0:
                return ""
            return s.recv(1024).decode("ascii",errors="replace")
    except (socket.timeout, socket.error):
        return ""


        #-----------------------------
        #         scanner
        #-----------------------------

def scan_tcp_port_details(ip, port, timeout):
    headers = grab_http_headers(ip, port, timeout)
    banner = ""

    if headers == "":
        banner = grab_banner(ip ,port, timeout)

    service, source, confidence, evidence = classify_service(port, banner, headers)
    return build_scan_result(ip,port,"TCP",service,source,confidence,banner,headers,evidence)

def scan_udp_port_details(ip, port):

        service, source = guess_service_name(port)
        if service != "unknown":
            confidence = "low"
            evidence = "matched by port"
        else:
            confidence = "low"
            evidence = "udp response"
        return build_scan_result(ip, port, "UDP", service, source, confidence,"","", evidence)

def scan_target():

   ip, start, end, timeout = get_scan_config()
   open_tcp_ports, open_udp_ports = scan_port_range(ip,start,end,timeout)

   results_tcp = []; results_udp = []
   for port in open_tcp_ports:
       results_tcp.append(scan_tcp_port_details(ip, port, timeout))
   for port in open_udp_ports:
       results_udp.append(scan_udp_port_details(ip,port))
   return results_tcp, results_udp

def scan_port_range(host, start_port, end_port, timeout, terminal=None):
     if terminal is None:
        terminal = shutil.get_terminal_size((80,20)).columns
     open_tcp_ports = []; open_udp_ports = []
     COMMON_UDP_PORTS = [53, 67, 68, 123, 161, 500, 5353]
     clear_terminal()
     for port in range(start_port, end_port+1):
        if port % 10 == 0:
            print(f"\r" + f"Scanning port {port}".center(terminal),end="", flush=True)
        if is_tcp_port_open(host,port,timeout):
            open_tcp_ports.append(port)
        if port in COMMON_UDP_PORTS:
            if is_udp_port_open(host,port,timeout):
                open_udp_ports.append(port)
     clear_terminal()
     return open_tcp_ports, open_udp_ports


def is_tcp_port_open(host, port, timeout):

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            return (s.connect_ex((host,port)) == 0)
    except socket.error:
        return False

def is_udp_port_open(host, port, timeout):

    UDP_PROBES = {
    53: b"\xaa\xaa\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x07example\x03com\x00\x00\x01\x00\x01",
    123: b"\x1b" + 47 * b"\0",
    }

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.settimeout(timeout)
            probe = UDP_PROBES.get(port,b"")
            s.sendto(probe, (host, port))

            try:
                s.recvfrom(1024)
                return True
            except socket.timeout:
                return False
    except socket.error:
        return False


    #-----------------------------
    #         services
    #-----------------------------


def classify_service(port, banner, headers):
    if headers != "":
        first_line = headers.splitlines()[0]

        if first_line.lower().startswith("ssh"):
            return ("SSH", "banner", "high", first_line)

        if value := extract_header_value(headers, name="server"):
            return ("HTTP", "http_headers", "high", value)
        else:
            return ("HTTP", "http_headers", "medium", first_line)

    elif banner != "":
        banner_lower = banner.lower()

        if "ssh" in banner_lower:
            return ("SSH", "banner", "high", banner)
        elif "ftp" in banner_lower:
            return ("FTP", "banner", "high", banner)
        else:
            return ("unknown", "banner", "medium", banner)

    service, source = guess_service_name(port)

    if service != "unknown":
        return (service, source, "low", "matched by port")

    return ("unknown", "none", "low", "")


def get_service_from_table(port):

    ports = {
        22 : "SSH",
        80 : "HTTP",
        443 : "HTTPS",
        1883: "MQTT",
        3306 : "MySQL",
        5432 : "PostgreSQL",
        8000 : "HTTP-alt",
        8080 : "HTTP-alt",
        8883 : "MQTT-TLS"
    }

    if port in ports:
        return ports[port]
    else:
        return None

def get_service_from_system(port):
    try:
        return socket.getservbyport(port, "tcp")
    except OSError:
        return None

def guess_service_name(port):
    if service := get_service_from_table(port):
        return (service, "port_table")
    elif service := get_service_from_system(port):
        return (service, "system_db")
    else:
        return ("unknown","none")



#-----------------------------
#         starter
#-----------------------------

def start_scanner():
    terminal = shutil.get_terminal_size((80,20)).columns
    clear_terminal()
    print();print(center_block("""=============================\n"""
                                """||  STARTING PORT SCANNER  ||\n"""
                                """=============================\n\n"""
                                """only for educational purpose\n"""
                                """use it only against allowed targets!\n\n"""
                                """to Start type in [OK]\n\n""", terminal))

    ok = clean_input(input(" " * (terminal // 2 - 4) + ">" + " " * 4))
    if ok == "OK":
        return terminal
    else:
        clear_terminal()
        sys.exit()

def get_port_range(terminal=None):
     if terminal is None:
        terminal = shutil.get_terminal_size((80,20)).columns

     while True:
        try:
            print();print("What's the Start Port?\n".center(terminal))
            start_port = int(input(" " * (terminal // 2 - 6) + ">" + " " * 3))
            if start_port < 1 or start_port > 65535:
                clear_terminal()
                print(center_block("\nInvalid START PORT\n",terminal ))
                continue
            print();print("What's the End Port?\n".center(terminal))
            end_port = int(input(" " * (terminal // 2 - 8) + ">" + " " * 3))
        except ValueError:
            clear_terminal()
            print("\nPorts must be NUMBERS\n".center(terminal))
        else:
             if end_port < 1 or end_port > 65535:
                clear_terminal()
                print(center_block("\nInvalid END PORT\n",terminal ))
                continue
             if start_port > end_port:
                clear_terminal()
                print(center_block("\nSTART PORT must be smaller than END PORT\n", terminal))
                continue

             return start_port, end_port

def get_timeout(terminal=None):
    if terminal is None:
        terminal = shutil.get_terminal_size((80,20)).columns
    while True:
        try:

            print();print("What's the Timeout?\n".center(terminal))
            timeout = float(input(" " * (terminal // 2 - 5) + ">" + " " * 3))
        except ValueError:
            clear_terminal()
            print(center_block("\nTIMEOUT must be a positive number\n",terminal))
            continue
        else:
             if timeout <= 0:
                clear_terminal()
                print(center_block("\nInvalid TIMEOUT\n",terminal ))
                continue
             return timeout

def get_scan_config(terminal=None):
   if terminal is None:
        terminal = shutil.get_terminal_size((80,20)).columns
   clear_terminal()
   while True:
        try:
            print();print("What's the Host?\n".center(terminal))
            host = input(" " * (terminal // 2 - 11) + ">" + " " * 3)
            if not validate(host):
                host = resolve_host(host)
                if not host:
                    clear_terminal()
                    print(center_block("\nInvalid IP\n",terminal ))
                    continue
            clear_terminal()
            start_port, end_port = get_port_range(terminal)
            clear_terminal()
            timeout = get_timeout(terminal)
            if timeout <= 0:
                clear_terminal()
                print(center_block("\nInvalid TIMEOUT\n",terminal ))
                continue
        except ValueError:
            continue
        else:
            return host, start_port, end_port, timeout


#-----------------------------
#       Helper from CS50p
#-----------------------------


def validate(ip):
    if numbers := re.search(r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$",ip):
       for number in numbers.groups():
            if int(number) > 255:
              return False
            elif (len(number) > 1 and number.startswith("0")):
              return False
            else:
              continue
       return True
    else:
       return False

def clear_terminal():
     os.system("cls" if os.name == "nt" else "clear")

def center_block(text,width):
     lines = text.splitlines()
     centered_lines = []
     for line in lines:
        centered_line = line.center(width)
        centered_lines.append(centered_line)

     return"\n".join(centered_lines)


if __name__ == "__main__":
    main()

# AI Usage Disclosure
# Chatgpt was used whilde developing this final project as a support tool for asking
# questions about debugging errors, socket concepts and general python concepts

# The project idea, code decisions, testing on my own Raspberry Pi and final implementation were completed and reviewed by me

