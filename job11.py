import re

domains_ex = []

with open("domains.xml") as file:
    domains = re.findall(r"\.[a-z]{1,}[<\s]", file.read())
    for domain in domains:
        domain = domain[:-1]
        if domain not in domains_ex:
            domains_ex.append(domain)
number_domains_ex = 0
for element in domains_ex:
    number_domains_ex += 1
print(str(number_domains_ex))
