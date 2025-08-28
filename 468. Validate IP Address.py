def validIPAddress(self, queryIP: str) -> str:
        ipv4_pattern=r'^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])$'
        ipv6_pattern=r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'
        if re.match(ipv4_pattern, queryIP):
            return "IPv4"
        elif re.match(ipv6_pattern, queryIP):
            return "IPv6"
        else:
            return "Neither"