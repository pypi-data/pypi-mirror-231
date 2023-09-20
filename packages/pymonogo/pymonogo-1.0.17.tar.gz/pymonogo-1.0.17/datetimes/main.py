import pyrogram
from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant, InviteHashExpired
import os, threading, asyncio, datetime, io, logging, random, string, time, traceback, aiofiles
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from paid import *
from .premium import *
from pyrogram import Client as bot, filters
from pyrogram.errors import *
from pyrogram.types import Message
from .database import *
from asyncio.exceptions import TimeoutError
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid
)

from pyrogram.types import CallbackQuery, InlineKeyboardMarkup
try:
    from bot import Bot as bot
except ModuleNotFoundError as e:
    print(f"Module not found: {e}")
except ImportError as e:
    print(f"Import error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    



log = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)



broadcast_ids = {}


async def send_msg(user_id, message):
    try:
        await message.forward(chat_id=user_id)
        return 200, None
    except FloodWait as e:
        await asyncio.sleep(e.x)
        return send_msg(user_id, message)
    except InputUserDeactivated:
        return 400, f"{user_id} : deactivated\n"
    except UserIsBlocked:
        return 400, f"{user_id} : blocked the bot\n"
    except PeerIdInvalid:
        return 400, f"{user_id} : user id invalid\n"
    except Exception:
        return 500, f"{user_id} : {traceback.format_exc()}\n"


@bot.on_message(
    filters.command("paid_broadcast")
    & filters.private
    & filters.user(AUTH_USERS)
    & filters.reply
)
async def paidbroadcast_(c, m):
    all_users = await db.get_all_paid_users()
    total_users = 0
    async for paid_user in all_users:
        total_users += 1

    broadcast_msg = m.reply_to_message
    while True:
        broadcast_id = "".join([random.choice(string.ascii_letters) for i in range(3)])
        if not broadcast_ids.get(broadcast_id):
            break
    out = await m.reply_text(text=f"Broadcasting.....")
    start_time = time.time()
    done = 0
    failed = 0
    success = 0
    broadcast_ids[broadcast_id] = dict(
        total=total_users, current=done, failed=failed, success=success
    )
    async with aiofiles.open("broadcast.txt", "w") as broadcast_log_file:
        async for user in all_users:
            sts, msg = await send_msg(user_id=int(user["id"]), message=broadcast_msg)
            if msg is not None:
                await broadcast_log_file.write(msg)
            if sts == 200:
                success += 1
            else:
                failed += 1
            # if sts == 400:
            #    await db.delete_user(user['id'])
            done += 1
            if broadcast_ids.get(broadcast_id) is None:
                break
            else:
                broadcast_ids[broadcast_id].update(
                    dict(current=done, failed=failed, success=success)
                )
    if broadcast_ids.get(broadcast_id):
        broadcast_ids.pop(broadcast_id)
    completed_in = datetime.timedelta(seconds=int(time.time() - start_time))
    await asyncio.sleep(3)
    await out.delete()
    if failed == 0:
        await m.reply_text(
            text=f"broadcast completed in `{completed_in}`\n\nTotal users {total_users}.\nTotal done {done}, {success} success and {failed} failed.",
            quote=True,
        )
    else:
        await m.reply_document(
            document="broadcast.txt",
            caption=f"broadcast completed in `{completed_in}`\n\nTotal users {total_users}.\nTotal done {done}, {success} success and {failed} failed.",
            quote=True,
        )
    os.remove("broadcast.txt")


async def check_user_plan(c, m):
    paid_duration = 0
    paid_on = 0
    paid_usr_count = 0
    will_expire_on_date = 0
    will_expire_days = 0
    try:
        user_ids = int(m.from_user.id)
        all_paid_users = await db.get_all_paid_users()
        async for paid_user in all_paid_users:
            user_id = paid_user["id"]
            if user_ids == user_id:
                paid_duration = paid_user["paid_status"]["paid_duration"]
                paid_on = paid_user["paid_status"]["paid_on"]
                paid_user["paid_status"]["paid_username"]
                paid_user["paid_status"]["paid_reason"]
                paid_usr_count = 1

                current_date = datetime.datetime.now()  # 2022-07-13 04:27:51.090832
                integer_paid_duration = int(paid_duration)
                will_expire = paid_on + datetime.timedelta(days=integer_paid_duration)
                # end_date or paid on same format: 2022-08-12 04:27:39.853000, timedelta: 30 days, 0:00:00
                # check = will_expire < current_date
                # log.info(f"Compare: {check}")

                if will_expire < current_date:
                    await db.remove_paid(user_id)
                    paid_usr_count = 0
                    return (
                        paid_usr_count,
                        paid_on,
                        paid_duration,
                        will_expire_days,
                        will_expire_on_date,
                    )
                will_exp_days = will_expire - current_date  # 29 days, 23:59:48.762168
                # formatted
                will_expire_on_date = will_expire.strftime("%Y-%m-%d")  # 2022-08-12
                will_expire_days = will_exp_days

                return (
                    paid_usr_count,
                    paid_on,
                    paid_duration,
                    will_expire_days,
                    will_expire_on_date,
                )
        if paid_usr_count == 0:
            return (
                paid_usr_count,
                paid_on,
                paid_duration,
                will_expire_days,
                will_expire_on_date,
            )
    except Exception as e:
        log.error(e, exc_info=True)
        paid_usr_count = 0
        return (
            paid_usr_count,
            paid_on,
            paid_duration,
            will_expire_days,
            will_expire_on_date,
        )


@bot.on_message(
    filters.private & filters.command("paid") & filters.user(AUTH_USERS)
)
async def paid_ss(c, m):
    await m.reply_text(
        "➩  /paid_user Add a user in Subscription\n\n➩  /paid_status To know user(s) paid status"
        "\n\n➩  /plan_expired When plan expired\n\n➩  /paid_users List of all paid users",
        quote=True,
    )


@bot.on_message(
    filters.private & filters.command("paid_status") & filters.user(AUTH_USERS)
)
async def paid_statusss(c, m):
    if len(m.command) == 1:
        await m.reply_text(
            "Use this command to add a user in paid bot.\n\nUsage:\n\n`/paid_user user_id`",
            quote=True,
        )
        return

    try:
        user_ids = int(m.command[1])
        all_paid_users = await db.get_all_paid_users()
        text = ""
        paid_usr_count = 0
        async for paid_user in all_paid_users:
            user_id = paid_user["id"]
            if user_ids == user_id:
                paid_usr_count += 1
                paid_duration = paid_user["paid_status"]["paid_duration"]
                paid_on = paid_user["paid_status"]["paid_on"]
                paid_username = paid_user["paid_status"]["paid_username"]
                paid_reason = paid_user["paid_status"]["paid_reason"]
                text += f"✶ **User Id** : `{user_id}`\n\n✶ **User Name** : {paid_username}\n\n➩ **Plan Validity** : `{paid_duration}` Days\n\n➩ **Joined On** : {paid_on} \n\n➩ **Discription** : `{paid_reason}` \n\n"
        if paid_usr_count == 0:
            await m.reply_text(
                "⚠️ Paid User not found in this id, or Plan Expired ",
                quote=True,
            )
            return
        reply_text = f"{text}"
        if len(reply_text) > 4096:
            paid_usrs = io.BytesIO()
            paid_usrs.name = "paid-users.txt"
            paid_usrs.write(reply_text.encode())
            await m.reply_document(paid_usrs, True)
            return
        await m.reply_text(reply_text, True)
    except Exception as e:
        log.error(e, exc_info=True)
        await m.reply_text(
            f"Error occoured!! {e}",
            quote=True,
        )


@bot.on_message(
    filters.private & filters.command("paid_user") & filters.user(AUTH_USERS)
)
async def paiduser(c, m):

    if len(m.command) == 1:
        await m.reply_text(
            "Use this command to add a user in paid bot.\n\nUsage:\n\n`/paid_user user_id user_name duration discription` ",
            quote=True,
        )
        return

    try:
        user_id = int(m.command[1])
        paid_username = m.command[2]
        paid_duration = int(m.command[3])
        paid_reason = " ".join(m.command[4:])
        paid_log_text = f"**User Id:** {user_id}\n**User Name:** {paid_username} \n**Plan Validity:** {paid_duration} Days"  #
        try:
            await c.send_message(
                user_id,
                f"🙂 Your paid subscription started for **{paid_duration}** Days",
            )
            paid_log_text += "\n\nUser notified successfully ✅"
        except Exception as e:
            log.debug(e, exc_info=True)
            paid_log_text += f"\n\nUser notification failed !!!{e}"
        await db.paid_user(user_id, paid_username, paid_duration, paid_reason)
        log.debug(paid_log_text)
        await m.reply_text(paid_log_text, quote=True)
    except Exception as e:
        log.error(e, exc_info=True)
        await m.reply_text(
            f"Error occoured!! {e}",
            quote=True,
        )


@bot.on_message(
    filters.private & filters.command("paid_users") & filters.user(AUTH_USERS)
)
async def _paid_usrs(c, m):
    all_paid_users = await db.get_all_paid_users()
    paid_usr_count = 0
    text = ""
    async for paid_user in all_paid_users:
        user_id = paid_user["id"]
        paid_duration = paid_user["paid_status"]["paid_duration"]
        paid_on = paid_user["paid_status"]["paid_on"]
        paid_username = paid_user["paid_status"]["paid_username"]
        paid_reason = paid_user["paid_status"]["paid_reason"]
        paid_usr_count += 1
        text += f"✶ **User Id** : `{user_id}`\n\n✶ **User Name** : `{paid_username}`\n\n➩ **Plan Validity** : `{paid_duration}` Days\n\n➩ **Joined On** : {paid_on} \n\n➩ **Discription** : `{paid_reason}` \n--------------------------------------------------------------\n\n"
    reply_text = f"Total Paid Users : `{paid_usr_count}`\n\n{text}"
    if len(reply_text) > 4096:
        paid_usrs = io.BytesIO()
        paid_usrs.name = "paid-users.txt"
        paid_usrs.write(reply_text.encode())
        await m.reply_document(paid_usrs, True)
        return
    await m.reply_text(reply_text, True)


@bot.on_message(
    filters.private & filters.command("plan_expired") & filters.user(AUTH_USERS)
)
async def plan_expireds(c, m):
    if len(m.command) == 1:
        await m.reply_text(
            "Use this command to kick plan_expired user.\n\nUsage:\n\n`/plan_expired user_id`\n\n",
            quote=True,
        )
        return

    try:
        user_id = int(m.command[1])
        plan_ex_log_text = f"Plan Validity Expired User {user_id}"

        try:
            await c.send_message(
                user_id,
                "👋 Your plan has Expired.\n\nIf you want to use the bot, You can do so by Paying.",
            )
            plan_ex_log_text += "\n\nUser notified successfully ✅"
        except Exception as e:
            log.debug(e, exc_info=True)
            plan_ex_log_text += f"\n\nUser notification failed !! {e}"
        await db.remove_paid(user_id)
        log.debug(plan_ex_log_text)
        await m.reply_text(plan_ex_log_text, quote=True)
    except Exception as e:
        log.error(e, exc_info=True)
        await m.reply_text(
            f"Error occoured! {e}",
            quote=True,
        )


@bot.on_message(filters.private & filters.command("plan"))
async def help(c, m):

    user_id = m.from_user.id
    if PAID_BOT.upper() == "YES":
        try:
            paid_status = await db.get_paid_status(user_id)
        except:
            await m.reply("⚠️ First Click on /start, Then try again")
            return
        if paid_status["is_paid"]:
            current_date = datetime.datetime.now()
            paid_duration = paid_status["paid_duration"]
            paid_on = paid_status["paid_on"]
            paid_reason = paid_status["paid_reason"]
            integer_paid_duration = int(paid_duration)
            will_expire = paid_on + datetime.timedelta(days=integer_paid_duration)
            if will_expire < current_date:
                try:
                    await db.remove_paid(user_id)
                except Exception as e:
                    logger.info(f"⚠️ Error: {e}")
                try:
                    await bot.send_message(
                        m.chat.id,
                        f"**User Id:** `{m.from_user.id}`\n\n**User Name:** @{m.from_user.username}\n\n**Plan Validity:** `{paid_duration}` Days\n\n**Joined On** : `{paid_on}`\n\n👋 Your Paid Plan Has Expired On {will_expire}\n\nIf You Want To Use The Bot, You Can Do So By Paying.\n\n__**Plan 1**__\n\n`199/M\n\nAll Features Of This Bot`\n\n__**Plan 2**__\n\n`499 For 3 Month\n\nAll Features Of This Bot`\n\n__**Plan 3**__\n\n`999 For 1 Year\n\nAll Features Of This Bot`\n\n||**Need More Plans Contact To Our Developer :- @{OWNER_USERNAME}**||",
                        reply_markup=PAID_BUTTONS
                    )
                except Exception as e:
                    logger.info(f"⚠️ Error: {e}")
                for i in Config.AUTH_USERS:
                    try:
                        await bot.send_message(
                            i,
                            f"🌟 **Plan Expired:** \n\n**User Id:** `{m.from_user.id}`\n\n**User Name:** @{update.from_user.username}\n\n**Plan Validity:** {paid_duration} Days\n\n**Joined On** : {paid_on}\n\n**Discription** : {paid_reason}",
                            reply_markup=PAID_BUTTONS
                        )
                    except Exception:
                        logger.info(f"⚠️ Not found id {i}")
                return

            else:
                pass

        else:
            current_date = datetime.datetime.now()
            await m.reply_text(
                text=f"**Your Plan Deatails**\n\n**User Id:** `{m.from_user.id}`\n\n**User Name:** @{m.from_user.username}\n\nPlan : `Free`\n\n**Plan Validity:** `Lifetime`\n\nDate :- {current_date}\n\n__**Plan 1**__\n\n`199/M\n\nAll Features Of This Bot`\n\n__**Plan 2**__\n\n`499 For 3 Month\n\nAll Features Of This Bot`\n\n__**Plan 3**__\n\n`999 For 1 Year\n\nAll Features Of This Bot`\n\n||**Need More Plans Contact To Our Developer :- @{OWNER_USERNAME}**||",
                disable_web_page_preview=True,
                quote=True,
                reply_markup=PAID_BUTTONS
            )
            return
    paid_id = m.from_user.id
    paid_status = await db.get_paid_status(paid_id)
    if paid_status["is_paid"]:
        current_date = datetime.datetime.now()
        paid_duration = paid_status["paid_duration"]
        paid_on = paid_status["paid_on"]
        paid_reason = paid_status["paid_reason"]
        integer_paid_duration = int(paid_duration)
        will_expire = paid_on + datetime.timedelta(days=integer_paid_duration)
        await m.reply_text(
            text=f"**Your Plan Deatails**\n\n**User Id:** `{m.from_user.id}`\n\n**User Name:** @{m.from_user.username}\n\nPlan Type : `Paid`\n\n**Plan Validity:** `{paid_duration}` Days\n\n**Plan Buy On** : `{paid_on}`\n\n**Plan Discription** : `{paid_reason}`\n\nDate :- `{current_date}`\n\n👋 Your Paid Plan Has Expired On {will_expire}\n\n__**Plan 1**__\n\n`199/M\n\nAll Features Of This Bot`\n\n__**Plan 2**__\n\n`499 For 3 Month\n\nAll Features Of This Bot`\n\n__**Plan 3**__\n\n`999 For 1 Year\n\nAll Features Of This Bot`\n\n||**Need More Plans Contact To Our Developer :- @{OWNER_USERNAME}**||",
            disable_web_page_preview=True,
            reply_markup=PAID_BUTTONS,
            quote=True
        )

