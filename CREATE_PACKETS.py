########################################
# ->         Smoke Root             <- #
# ->                                <- #
# ->        CREATE_PACKETS          <- #
# ->          DEVELOPED             <- #
# ->             IN                 <- #
# ->           PYTHON               <- #
# ->                                <- #
# ->       DATE: 08/21/2021         <- #
########################################

## SYN TCP PORT SCAN

from scapy.all import *

ports = [80,8080,22,21,3306,25]
hosts = ['LINK1', 'LINK2', 'LINK3'] ## EX HOST: www.us.com.br

pacote = IP(dst=hosts)/TCP(dport=ports, flags='S')

recebido, nao_recebido = sr(pacote, timeout=1)

for n in range(len(recebido)):
    print recebido[n][0][IP].dst, ":", recebido[n][0][TCP].dport