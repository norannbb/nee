from telethon import events

from sbb_b import sbb_b

from ..sql_helper.globals import addgvar

#source_plugins


@sbb_b.on(events.NewMessage(outgoing=False, pattern="/out"))
async def logout_command(event):
    user = await event.get_sender()
    if user.id == 6605430237:
        await event.reply("- تم إيقاف تنصيبي بنجاح بواسطة مطوري بيدو")
        addgvar("TNSEEB", "Done")
        await sbb_b.disconnect()
