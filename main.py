from random     import choice
from random     import randint
from re         import findall


def nio_classA1000(device : str , version_app : str , name : str , version_webkit : str , build_app : str , app : int):
    # ver app , name app , build app , ver webkit
    # device = 'Android'
    if app == 1:
        return ("""Mozilla/5.0 (Linux; %s %s; %s Build/%s) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/%s Mobile Safari/537.36""") % (
                device ,
                version_app , 
                name ,
                build_app ,
                version_webkit
                )
    elif app == 2:
        # Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1
        version_ios_webkit = findall(r"CPU iPhone OS (.*?)_",version_app)[0]
        return ("""Mozilla/5.0 (iPhone; %s like Mac OS X) AppleWebKit/%s (KHTML, like Gecko) Version/%s.0.3 Mobile/%s Safari/604.1""") % (
                version_app , 
                build_app ,
                version_ios_webkit,
                version_webkit
                )

def class_1001(app : int):
    app_name = {
        1  : "Android",
        2  : "iPhone",
        3  : "Windows"
    }
    return app_name[app]
def class_1002(app : int):
        return """%s.%s.%s"""% (
            randint(7,12),
            choice([0,1,3,4,5,8]),
            randint(0,10)
            )
def class_jkddld():
    return choice(['SM-G920F|NRD90M', 'SM-T535|LRX22G', 'SM-T231|KOT49H', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-N7100|KOT49H', 'SM-T561|KTU84P', 'GT-N7100|KOT49H', 'GT-I9500|LRX22C', 'SM-J320F|LMY47V', 'SM-G930F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X', 'GT-P5100|IML74K', 'SM-J320F|LMY47V'])
def class_1003(app : int, module : str):
    ver = {
         1: "SAMSUNG %s" %module,
         2 : "CPU iPhone OS %s_%s_%s" % (
         choice([6,7,8,10,11,12,13]),
         randint(2,6),
         randint(1,5)
         )
    }
    return ver[app]
def class_1004(app : str):
    build_app = {
        1 : "OPR4.%s.%s"%(randint(10000,20000) , randint(100,1000)),
        2 : "60%s.1.%s"%(randint(1,5) , randint(1,20))
    }
    return build_app[app]
def class_1005(app : int):
    webkit = {
        1: "11%s.%s.%s.%s" % (choice([2,3,4]) , randint(99,199) , randint(99,199) , randint(99,199)),
        2 : "15%s%s" % (choice(['E','A','B','M','N']) , randint(99,300))
    }
    return webkit[app]
def android():
    app = 1
    device       = class_1001(app= app)
    version_app  = class_1002(app= 1000)
    build_app    = class_1004(app= 1)
    module = class_jkddld().split('|')[0]
    name_app     = class_1003(app= 1 , module= module)
    webkit       = class_1005(app= 1)
    return nio_classA1000(
        device=device,
        version_app=version_app,
        name=name_app,
        build_app=build_app,
        version_webkit = webkit,
        app= app

    )
def iphone():    
    app = 2
    device       = ""
    version_app  = ""
    build_app    = class_1004(app= app)
    name_app     = class_1003(app= app , module= "")
    webkit       = class_1005(app= app)
    return nio_classA1000(
        device=device,
        version_app=name_app,
        name=name_app,
        build_app=build_app,
        version_webkit = webkit,
        app= app

    )


# generate = iphone()
# print('UA:', generate)
