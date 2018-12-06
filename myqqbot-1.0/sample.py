# -*- coding: utf-8 -*-

# 插件加载方法： 
# 先运行 qqbot ，启动成功后，在另一个命令行窗口输入： qq plug qqbot.plugins.sample
import datetime
import os
def onQQMessage(bot, contact, member, content):
    # 四个参数的详细
    # bot     : QQBot 对象，提供 List/SendTo/Stop/Restart 四个接口，详见本文档第五节
    # contact : QContact 对象，消息的发送者，具有 ctype/qq/uin/nick/mark/card/name 属性，这些属性都是 str 对象
    # member  : QContact 对象，仅当本消息为 群或讨论组 消息时有效，代表实际发消息的成员
    # content : str 对象，消息内容
    me = '崔思深可'

    if '@'+me in content and '傻逼' in content:
        bot.SendTo(contact, '晓磊才是傻逼')
    # elif '@'+me in content:
    #     bot.SendTo(contact, member.name+'，艾特我干嘛呢？')
    elif '@崔思深可' in content:
        bot.SendTo(contact, member.name+'，艾特闰土干嘛呢？')
    elif 'test' == content:
        bot.SendTo(contact, os.getcwd())
        fwrite = open('count.txt', 'w', encoding='utf-8')
        fwrite.write(str(0))
        fwrite.close()
    # 当群里有人@你的时候 传入过来的会被转化为[@ME]
    # 所以使用 @ME 来过滤其他人在群里面at你
    elif "help" in content and '@'+me in content:
        now = datetime.datetime.now()
        now = now.strftime("%Y-%m-%d")
        bot.SendTo(contact, '到' + now + "为止,闰土有以下几种命令：\n@我 含help :输出当前闰土所有命令\n"
                                        "time :输出当前时间\n"
                                        "睡觉吧： 这辈子不可能睡觉的\n"
                                        "醒醒啊闰土 ： 瞬间清醒，活力四射\n"
                                        "stop ：关闭闰土\n"
                                        "@我 ： 艾特我干嘛呢？\n"
                                        "@我 含傻逼内容 ： 晓磊才是傻逼")
    elif content == "time":
        now = datetime.datetime.now()
        now = now.strftime("%Y-%m-%d %H:%M:%S")
        bot.SendTo(contact, '你好，我是闰土,现在是北京时间：'+now)
    elif content == '睡觉吧':
        now = datetime.datetime.now()
        now = now.strftime("%H:%M")
        fread = open('count.txt', 'r', encoding='utf8')
        sleepfeeling = int(fread.read())
        fread.close()
        if sleepfeeling<5:
            bot.SendTo(contact, '困意为'+str(sleepfeeling)+'，不睡,现在才'+now)
            fwrite = open('count.txt', 'w', encoding='utf-8')
            fwrite.write(str(sleepfeeling + 1))
            fwrite.close()
        elif sleepfeeling == 5:
            bot.SendTo(contact, '困意为'+str(sleepfeeling)+'，好困啊，睡一会吧')
            fwrite = open('count.txt', 'w', encoding='utf-8')
            fwrite.write(str(sleepfeeling + 1))
            fwrite.close()
        elif sleepfeeling > 5:
            bot.SendTo(contact, '困意为'+str(sleepfeeling)+'，我都已经睡着了，你还要怎样？晚安everybody，明天做睡觉倒计时')
    elif content == '醒醒啊闰土':
        fwrite = open('count.txt', 'w', encoding='utf-8')
        fwrite.write(str(0))
        fwrite.close()
        fread = open('count.txt', 'r', encoding='utf8')
        sleepfeeling = int(fread.read())
        fread.close()
        bot.SendTo(contact, '困意为' + str(sleepfeeling) + '，大家好，我现在感觉倍爽儿')
    elif content == 'stop':
        bot.SendTo(contact, 'QQ机器人已关闭')
        # bot.Stop()