#!/usr/bin/env python
#-*- coding:utf-8 -*-

import httplib, urllib
import socket, time

params = dict(
    login_email="dnspod account", # replace with your email
    login_password="dnspod password", # replace with your password
    format="json",
    domain_id=342154, # replace with your domain_od, can get it by API Domain.List
    record_id=69302311, # replace with your record_id, can get it by API Record.List
    sub_domain="pi", # replace with your sub_domain
    record_line="默认",
)
ip_file = '/var/log/dnspod.ip'

def get_old_ip():
    try:
        f = open(ip_file, "rw")
        old_ip = f.readline()
        f.close()
        return old_ip
    except Exception, e:
        return None

def save_current_ip(ip):
   f = open(ip_file, 'w')
   f.write(ip)
   f.close()

def ddns(ip):
    params.update(dict(value=ip))
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/json"}
    conn = httplib.HTTPSConnection("dnsapi.cn")
    conn.request("POST", "/Record.Ddns", urllib.urlencode(params), headers)

    response = conn.getresponse()
    print response.status, response.reason
    data = response.read()
    print data
    conn.close()
    return response.status == 200

def get_current_ip():
    sock = socket.create_connection(('ns1.dnspod.net', 6666))
    ip = sock.recv(16)
    sock.close()
    return ip

if __name__ == '__main__':
    try:
        current_ip = get_current_ip()
        old_ip = get_old_ip()
        if current_ip != old_ip :
            if ddns(current_ip):
                save_current_ip(current_ip)
    except Exception, e:
        print e


