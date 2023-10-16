#!/usr/bin/python3
# -*- coding: utf-8 -*-

from upsonic import Upsonic, Upsonic_Remote, HASHES

class Upsonic_Auth_Controller:
    def __init__(self, encryption_key, database_name, api_url, password=None) -> None:
        self.encrypted_key = encryption_key
        self.connection = Upsonic_Remote(database_name, api_url, password)
    def add_user(self, name, password):
        self.connection.set(name, HASHES.get_hash(password), encrypted_key=self.encrypted_key)
    def delete_user(self, name):
        self.connection.delete(name)        
    def check(self, name, password):
        return self.connection.get(name, encrypted_key=self.encrypted_key) == HASHES.get_hash(password)

def Upsonic_Auth(encryption_key, database_name):
    return Upsonic_Auth_Controller(encryption_key, database_name, "http://free.cloud.upsonic.co:5000", "onuratakan")

def Upsonic_Auth_Pro(encryption_key, database_name, access_key):
    return Upsonic_Auth_Controller(encryption_key, database_name, "http://free.cloud.upsonic.co:5001", access_key)

def Upsonic_Auth_Dedicated(encryption_key, database_name, password, dedicated_key):
    dedicated_key = dedicated_key.replace("dedicatedkey-", "")
    dedicated_key = dedicated_key.encode()
    resolver = Upsonic("dedicate_resolver")
    resolver.set(dedicated_key.decode(), dedicated_key)
    host = resolver.get(dedicated_key.decode(), encryption_key="dedicatedkey")
    return Upsonic_Auth_Controller(encryption_key, database_name, host, password)