# Cake

Cake is a simple security scanning library.

## Features
- Port scanning
- Subdomain scanning
- IP geolocation lookup
- Banner grabbing
- CMS detection

## Installation
```
pip install .
```

## Usage
```python
import cake

ports = cake.get_ports("example.com")
subdomains = cake.get_subdomains("example.com", ["www", "blog"])
ip_info = cake.get_ipinfo("8.8.8.8")
banner = cake.get_banner("example.com", 80)
cms = cake.get_cms("https://example.com")
```
