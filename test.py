import ldap

ldap_server = "ldap.tek-up.de"  

ldap_ou = "security"  
ldap_group = "security-group"  


    # domaine d'admin
LDAP_ADMIN_DN = "cn=admin,dc=tek-up,dc=de"
LDAP_ADMIN_PWD = "li"

# start connection

try:
    print(ldap_server)
    ldap_client = ldap.initialize(ldap_server)
        # search for specific user
except ldap.LDAPError as e:
           # LOG.debug('(ldap_connect) LDAP Erro : %s : Type %s ' %s (str(e), type(e)))
    print("###############################################" + str(e))
    print(type(e))                          
