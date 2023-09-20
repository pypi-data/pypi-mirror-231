try:
    from paid import *
    print("Paid module imported")
except:
    try:
        from config import *
        print("Config module imported")
    except:
        try:
            from info import *
            print("Info module imported")
        except:
            try:
                from dkbotz import *
                print("Dkbotz module imported")
            except:
                try:
                    from configs import *
                    print("Configs module imported")
                except:
                    print("_______________________")








