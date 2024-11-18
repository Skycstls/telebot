#!/bin/bash
domain=$1

dig +short A $domain > A.txt
dig +short NS $domain > NS.txt
dig +short MX $domain > MX.txt
dig +short TXT $domain > TXT.txt
dig +short SOA $domain > SOA.txt
dig +short SRV $domain > SRV.txt
dig +short CNAME $domain > CNAME.txt
dig +short AAAA $domain > AAAA.txt
dig +short PTR $domain > PTR.txt
dig +short SPF $domain > SPF.txt

#sudo nmap -sV -p- -A $domain -oA nmap_raw.txt

cero $domain > cero_raw.txt

if [ ! -s A.txt ]; then
    rm A.txt
fi
if [ ! -s NS.txt ]; then
    rm NS.txt
fi
if [ ! -s MX.txt ]; then
    rm MX.txt
fi
if [ ! -s TXT.txt ]; then
    rm TXT.txt
fi
if [ ! -s SOA.txt ]; then
    rm SOA.txt
fi
if [ ! -s SRV.txt ]; then
    rm SRV.txt
fi
if [ ! -s CNAME.txt ]; then
    rm CNAME.txt
fi
if [ ! -s AAAA.txt ]; then
    rm AAAA.txt
fi
if [ ! -s PTR.txt ]; then
    rm PTR.txt
fi
if [ ! -s SPF.txt ]; then
    rm SPF.txt
fi
if [ ! -s cero_raw.txt ]; then
    rm cero_raw.txt
fi

#check if exist file then cat to resultados
if [ -f A.txt ]; then
    echo "# A" >> resultados.txt
    cat A.txt >> resultados.txt
    echo "------------------" >> resultados.txt
fi
if [ -f NS.txt ]; then
    echo "# NS" >> resultados.txt
    cat NS.txt >> resultados.txt
    echo "------------------" >> resultados.txt

fi
if [ -f MX.txt ]; then
    echo "# MX" >> resultados.txt
    cat MX.txt >> resultados.txt
    echo "------------------" >> resultados.txt

fi
if [ -f TXT.txt ]; then
    echo "# TXT" >> resultados.txt
    cat TXT.txt >> resultados.txt
    echo "------------------" >> resultados.txt
fi
if [ -f SOA.txt ]; then
    echo "# SOA" >> resultados.txt
    cat SOA.txt >> resultados.txt
    echo "------------------" >> resultados.txt
fi
if [ -f SRV.txt ]; then
    echo "# SRV" >> resultados.txt
    cat SRV.txt >> resultados.txt
    echo "------------------" >> resultados.txt
fi
if [ -f CNAME.txt ]; then
    echo "# CNAME" >> resultados.txt
    cat CNAME.txt >> resultados.txt
    echo "------------------" >> resultados.txt
fi
if [ -f AAAA.txt ]; then
    echo "# AAAA" >> resultados.txt
    cat AAAA.txt >> resultados.txt
    echo "------------------" >> resultados.txt
fi
if [ -f PTR.txt ]; then
    echo "# PTR" >> resultados.txt
    cat PTR.txt >> resultados.txt
    echo "------------------" >> resultados.txt
fi
if [ -f SPF.txt ]; then
    echo "# SPF" >> resultados.txt
    cat SPF.txt >> resultados.txt
    echo "------------------" >> resultados.txt
fi
if [ -f cero_raw.txt ]; then
    echo "# CERO" >> resultados.txt
    cat cero_raw.txt >> resultados.txt
    echo "------------------" >> resultados.txt
fi

rm A.txt
rm NS.txt
rm MX.txt
rm TXT.txt
rm SOA.txt
rm SRV.txt
rm CNAME.txt
rm AAAA.txt
rm PTR.txt
rm SPF.txt
rm cero_raw.txt

cat resultados.txt
rm resultados.txt