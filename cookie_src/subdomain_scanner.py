import socket

def get_subdomains(domain, subdomains):
    active_subdomains = []
    for sub in subdomains:
        subdomain = f"{sub}.{domain}"
        try:
            ip = socket.gethostbyname(subdomain)
            active_subdomains.append((subdomain, ip))
        except socket.gaierror:
            pass
    return active_subdomains
