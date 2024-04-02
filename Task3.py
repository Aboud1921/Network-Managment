from pysnmp.hlapi import *
def Get_object(object,commun):
    iterator = getCmd(
        SnmpEngine(),
        CommunityData(commun, mpModel=0),
        UdpTransportTarget(('localhost', 161)),
        ContextData(),
        ObjectType(ObjectIdentity(object))
    )


    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

    if errorIndication:
        print(errorIndication)

    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))

    else:

        for varBind in varBinds:
            print(' = '.join([x.prettyPrint() for x in varBind]))
    return varBinds
def Set_object(object,commun,new_val):
    iterator = setCmd(
        SnmpEngine(),
        CommunityData(commun),
        UdpTransportTarget(('localhost', 161)),
        ContextData(),
        ObjectType(
            ObjectIdentity(object),
            new_val
        )
    )

    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

    if errorIndication:
        print(errorIndication)

    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))

    else:
        
        for varBind in varBinds:
            print(' = '.join([x.prettyPrint() for x in varBind]))
def Get_val(s):
    val = ''
    for i in range(len(s)):
        if s[i] == '=':
            k = len(s) - i
            val = s[i+2:i + k]
            break
    return val



Set_object('.1.3.6.1.2.1.1.4.0','Abdo','Desktop')
g=Get_object('.1.3.6.1.2.1.1.4.0','Abdo')
Output=Get_val(g[0].prettyPrint())
if Output=='Desktop':
    Set_object('.1.3.6.1.2.1.1.4.0','Abdo','Abdelrahman')
    print('done')
else:
    print('Failed')




