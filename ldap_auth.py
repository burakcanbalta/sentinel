from ldap3 import Server, Connection, ALL, NTLM
import os

LDAP_SERVER = os.getenv("LDAP_SERVER", "ldap://your-ldap.local")
LDAP_USER_DOMAIN = os.getenv("LDAP_DOMAIN", "corp.local")

def ldap_login(username, password):
    try:
        server = Server(LDAP_SERVER, get_info=ALL)
        user_dn = f"{LDAP_USER_DOMAIN}\\{username}"
        conn = Connection(server, user=user_dn, password=password, authentication=NTLM, auto_bind=True)
        if conn.bound:
            return True
    except Exception as e:
        print("LDAP login failed:", e)
    return False
