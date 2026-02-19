#!/usr/bin/env python3
php_define("8290934275:AAG8nhKC6U6mIcVJgGSPNNkAF60AXDgiets", "https://t.me/education_coders")
#// token qoyes.manba: @education_coders dasturchi: @muzadev tahrichi:@uzder_php  @education_coders kanali orqali tarqatildi!!! manba bilan olmagan kut!!!
admin_ = "8215108926"
#// admin id qoyas manba: @education_coders dasturchi: @muzadev tahrichi:@uzder_php  @education_coders kanali orqali tarqatildi!!! manba bilan olmagan kut!!!
#// manba: @education_coders
#// dasturchi: @muzadev. tahrirchi:@uzder_php. @education_coders kanali orqali tarqatildi!!! manba bilan olmagan kut!!!
def bot(method_=None, datas_=None, *_args_):
    if datas_ is None:
        datas_ = Array()
    # end if
    
    url_ = "https://api.telegram.org/bot" + API_KEY + "/" + method_
    ch_ = curl_init()
    curl_setopt(ch_, CURLOPT_URL, url_)
    curl_setopt(ch_, CURLOPT_RETURNTRANSFER, True)
    curl_setopt(ch_, CURLOPT_POSTFIELDS, datas_)
    res_ = curl_exec(ch_)
    if curl_error(ch_):
        var_dump(curl_error(ch_))
    else:
        return php_json_decode(res_)
    # end if
    
# end def bot
def hisob(*_args_):
    
    
    text_ = "ð TOP10 = Hisoblar\n\n"
    daten_ = Array()
    rev_ = Array()
    fayllar_ = glob("foydalanuvchi/hisob/*.*")
    for file_ in fayllar_:
        if php_mb_stripos(file_, ".txt") != False:
            value_ = php_file_get_contents(file_)
            id_ = php_str_replace(Array("foydalanuvchi/hisob/", ".txt"), Array("", ""), file_)
            daten_[value_] = id_
            rev_[id_] = value_
        # end if
        print(file_)
    # end for
    asort(rev_)
    reversed_ = php_array_reverse(rev_)
    i_ = 0
    while i_ < 10:
        
        order_ = i_ + 1
        id_ = daten_[str(reversed_[i_])]
        text_ += str("<b>") + str(order_) + str("</b>. <a href='tg://user?id=") + str(id_) + str("'>") + str(id_) + str("</a> - ") + "<code>" + reversed_[i_] + "</code>" + " <b>so'm</b>" + "\n"
        i_ += 1
    # end while
    return text_
    
# end def hisob
def dostlar(*_args_):
    
    
    text2_ = "ð TOP10 = Do'stlar\n\n"
    daten2_ = Array()
    rev2_ = Array()
    fayllar2_ = glob("foydalanuvchi/referal/*.*")
    for file2_ in fayllar2_:
        if php_mb_stripos(file2_, ".txt") != False:
            value2_ = php_file_get_contents(file2_)
            id2_ = php_str_replace(Array("foydalanuvchi/referal/", ".txt"), Array("", ""), file2_)
            daten2_[value2_] = id2_
            rev2_[id2_] = value2_
        # end if
        print(file2_)
    # end for
    asort(rev2_)
    reversed2_ = php_array_reverse(rev2_)
    i2_ = 0
    while i2_ < 10:
        
        order2_ = i2_ + 1
        id2_ = daten2_[str(reversed2_[i2_])]
        text2_ += str("<b>") + str(order2_) + str("</b>. <a href='tg://user?id=") + str(id2_) + str("'>") + str(id2_) + str("</a> - ") + "<code>" + reversed2_[i2_] + "</code>" + " <b>ta</b>" + "\n"
        i2_ += 1
    # end while
    return text2_
    
# end def dostlar
def deleteFolder(path_=None, *_args_):
    
    
    if php_is_dir(path_) == True:
        files_ = php_array_diff(scandir(path_), Array(".", ".."))
        for file_ in files_:
            deleteFolder(php_realpath(path_) + "/" + file_)
        # end for
        return rmdir(path_)
    else:
        if php_is_file(path_) == True:
            return unlink(path_)
        # end if
    # end if
    return False
    
# end def deleteFolder
def joinchat(id_=None, *_args_):
    
    
    global mid_
    php_check_if_defined("mid_")
    array_ = Array("inline_keyboard")
    kanallar_ = php_file_get_contents("sozlamalar/kanal/ch.txt")
    ex_ = php_explode("\n", kanallar_)
    i_ = 0
    while i_ <= php_count(ex_) - 1:
        
        first_line_ = ex_[i_]
        first_ex_ = php_explode("@", first_line_)
        url_ = first_ex_[1]
        ism_ = bot("getChat", Array({"chat_id": "@" + url_})).result.title
        ret_ = bot("getChatMember", Array({"chat_id": str("@") + str(url_), "user_id": id_}))
        stat_ = ret_.result.status
        if stat_ == "creator" or stat_ == "administrator" or stat_ == "member":
            array_["inline_keyboard"][str(i_)][0]["text"] = "â " + ism_
            array_["inline_keyboard"][str(i_)][0]["url"] = str("https://t.me/") + str(url_)
        else:
            array_["inline_keyboard"][str(i_)][0]["text"] = "â " + ism_
            array_["inline_keyboard"][str(i_)][0]["url"] = str("https://t.me/") + str(url_)
            uns_ = True
        # end if
        i_ += 1
    # end while
    if uns_ == True:
        bot("sendMessage", Array({"chat_id": id_, "text": "<b>â ï¸ Botdan foydalanish uchun quyidagi kanalimizga azo bo'ling va /start  bosing!</b>", "parse_mode": "html", "reply_to_message_id": mid_, "disable_web_page_preview": True, "reply_markup": php_json_encode(array_)}))
        return False
    else:
        return True
    # end if
    
# end def joinchat
update_ = php_json_decode(php_file_get_contents("php://input"))
message_ = update_.message
cid_ = message_.chat.id
tx_ = message_.text
mid_ = message_.message_id
name_ = message_.from_.first_name
fid_ = message_.from_.id
callback_ = update_.callback_query
data_ = callback_.data
callid_ = callback_.id
ccid_ = callback_.message.chat.id
cmid_ = callback_.message.message_id
from_id_ = update_.message.from_.id
token_ = message_.text
text_ = message_.text
message_id_ = callback_.message.message_id
data_ = update_.callback_query.data
callcid_ = update_.callback_query.message.chat.id
doc_ = update_.message.document
doc_id_ = doc_.file_id
cqid_ = update_.callback_query.id
callfrid_ = update_.callback_query.from_.id
botname_ = bot("getme", Array("FastKonsBot")).result.username
#// #-----------------------------
mkdir("foydalanuvchi")
mkdir(str("foydalanuvchi/sarmoya/") + str(fid_))
mkdir(str("foydalanuvchi/bot/") + str(fid_))
mkdir("foydalanuvchi/sarhisob")
mkdir("foydalanuvchi/sarmoya")
mkdir("foydalanuvchi/referal")
mkdir("foydalanuvchi/hisob")
mkdir("sozlamalar/hamyon")
mkdir("sozlamalar/kanal")
mkdir("sozlamalar/tugma")
mkdir("sozlamalar/xizmat")
mkdir("sozlamalar/xizmatlar")
mkdir("sozlamalar/bot")
mkdir("sozlamalar/pul")
mkdir("statistika")
mkdir(str("nak/") + str(cid_))
mkdir("nak")
mkdir("sozlamalar")
mkdir("otkazma")
mkdir("botlar")
mkdir("step")
mkdir("baza")
mkdir("ban")
#// #-----------------------------
if (not php_file_exists(str("foydalanuvchi/hisob/") + str(fid_) + str(".1.txt"))):
    file_put_contents(str("foydalanuvchi/hisob/") + str(fid_) + str(".1.txt"), "0")
# end if
if (not php_file_exists(str("foydalanuvchi/hisob/") + str(fid_) + str(".1txt"))):
    file_put_contents(str("foydalanuvchi/hisob/") + str(fid_) + str(".1txt"), "0")
# end if
if (not php_file_exists(str("foydalanuvchi/hisob/") + str(fid_) + str(".txt"))):
    file_put_contents(str("foydalanuvchi/hisob/") + str(fid_) + str(".txt"), "0")
# end if
if (not php_file_exists(str("foydalanuvchi/sarhisob/") + str(fid_) + str(".kiritgan"))):
    file_put_contents(str("foydalanuvchi/sarhisob/") + str(fid_) + str(".kiritgan"), "0")
# end if
if (not php_file_exists(str("foydalanuvchi/sarhisob/") + str(fid_) + str(".chiqargan"))):
    file_put_contents(str("foydalanuvchi/sarhisob/") + str(fid_) + str(".chiqargan"), "0")
# end if
if (not php_file_exists(str("foydalanuvchi/referal/") + str(fid_) + str(".txt"))):
    file_put_contents(str("foydalanuvchi/referal/") + str(fid_) + str(".txt"), "0")
# end if
if (not php_file_exists(str("foydalanuvchi/sarmoya/") + str(fid_) + str("/sarson.txt"))):
    file_put_contents(str("foydalanuvchi/sarmoya/") + str(fid_) + str("/sarson.txt"), "0")
# end if
if (not php_file_exists("sozlamalar/pul/referal.txt")):
    file_put_contents("sozlamalar/pul/referal.txt", "100")
# end if
if (not php_file_exists("sozlamalar/pul/valyuta.txt")):
    file_put_contents("sozlamalar/pul/valyuta.txt", "so'm")
# end if
if (not php_file_exists("sozlamalar/tugma/tugma1.txt")):
    file_put_contents("sozlamalar/tugma/tugma1.txt", "ð¤ Botlarni boshqarish")
# end if
if (not php_file_exists("sozlamalar/tugma/tugma2.txt")):
    file_put_contents("sozlamalar/tugma/tugma2.txt", "ð Kabinet")
# end if
if (not php_file_exists("sozlamalar/tugma/tugma3.txt")):
    file_put_contents("sozlamalar/tugma/tugma3.txt", "ðµ Pul ishlash")
# end if
if (not php_file_exists("sozlamalar/tugma/tugma4.txt")):
    file_put_contents("sozlamalar/tugma/tugma4.txt", "âï¸ Murojaat")
# end if
if (not php_file_exists("sozlamalar/tugma/tugma5.txt")):
    file_put_contents("sozlamalar/tugma/tugma5.txt", "@education_codersi")
# end if
if (not php_file_exists("sozlamalar/tugma/tugma6.txt")):
    file_put_contents("sozlamalar/tugma/tugma6.txt", "muzadev")
# end if
if (not php_file_exists("sozlamalar/tugma/tugma7.txt")):
    file_put_contents("sozlamalar/tugma/tugma7.txt", "ð Taklifnoma")
# end if
if (not php_file_exists("sozlamalar/kanal/ch.txt")):
    file_put_contents("sozlamalar/kanal/ch.txt", "@education_coders")
# end if
if (not php_file_exists(str("otkazma/") + str(fid_) + str(".idraqam"))):
    file_put_contents(str("otkazma/") + str(fid_) + str(".idraqam"), "")
# end if
if (not php_file_exists(str("otkazma/") + str(fid_) + str(".pulraqam"))):
    file_put_contents(str("otkazma/") + str(fid_) + str(".pulraqam"), "")
# end if
if (not php_file_exists("statistika/hammabot.txt")):
    file_put_contents("statistika/hammabot.txt", "0")
# end if
if (not php_file_exists("statistika/aktivbot.txt")):
    file_put_contents("statistika/aktivbot.txt", "0")
# end if
if php_file_get_contents("statistika/obunachi.txt"):
    pass
else:
    file_put_contents("statistika/obunachi.txt", "0")
# end if
if (not php_file_exists("baza/all.num")):
    file_put_contents("baza/all.num", "0")
# end if
kiritgan_ = php_file_get_contents(str("foydalanuvchi/hisob/") + str(fid_) + str(".1.txt"))
odam_ = php_file_get_contents(str("foydalanuvchi/referal/") + str(fid_) + str(".txt"))
odamcha_ = php_file_get_contents(str("foydalanuvchi/referal/") + str(fid_) + str(".db"))
asosiy_ = php_file_get_contents(str("foydalanuvchi/hisob/") + str(fid_) + str(".txt"))
sar_ = php_file_get_contents(str("foydalanuvchi/hisob/") + str(fid_) + str(".1txt"))
sarson_ = php_file_get_contents(str("foydalanuvchi/sarmoya/") + str(fid_) + str("/sarson.txt"))
pul_ = php_file_get_contents("sozlamalar/pul/valyuta.txt")
taklifpul_ = php_file_get_contents("sozlamalar/pul/referal.txt")
tugma1_ = php_file_get_contents("sozlamalar/tugma/tugma1.txt")
tugma2_ = php_file_get_contents("sozlamalar/tugma/tugma2.txt")
tugma3_ = php_file_get_contents("sozlamalar/tugma/tugma3.txt")
tugma4_ = php_file_get_contents("sozlamalar/tugma/tugma4.txt")
tugma5_ = php_file_get_contents("sozlamalar/tugma/tugma5.txt")
tugma6_ = php_file_get_contents("sozlamalar/tugma/tugma6.txt")
tugma7_ = php_file_get_contents("sozlamalar/tugma/tugma7.txt")
kanallar_ = php_file_get_contents("sozlamalar/kanal/ch.txt")
#// #-----------------------------------#
kategoriya_ = php_file_get_contents("sozlamalar/bot/kategoriya.txt")
royxat_ = php_file_get_contents(str("sozlamalar/bot/") + str(kategoriya_) + str("/royxat.txt"))
type_ = php_file_get_contents(str("sozlamalar/bot/") + str(kategoriya_) + str("/") + str(royxat_) + str("/turi.txt"))
narx_ = php_file_get_contents(str("sozlamalar/bot/") + str(kategoriya_) + str("/") + str(royxat_) + str("/narx.txt"))
tavsif_ = php_file_get_contents(str("sozlamalar/bot/") + str(kategoriya_) + str("/") + str(royxat_) + str("/tavsif.txt"))
#// #-----------------------------------#
kategoriya2_ = php_file_get_contents("sozlamalar/hamyon/kategoriya.txt")
raqam_ = php_file_get_contents(str("sozlamalar/hamyon/") + str(kategoriya2_) + str("/raqam.txt"))
#// #-----------------------------------#
saved_ = php_file_get_contents("step/odam.txt")
num_ = php_file_get_contents("baza/all.num")
ban_ = php_file_get_contents(str("ban/") + str(fid_) + str(".txt"))
statistika_ = php_file_get_contents("statistika/obunachi.txt")
aktivbot_ = php_file_get_contents("statistika/aktivbot.txt")
hammabot_ = php_file_get_contents("statistika/hammabot.txt")
soat_ = date("H:i", strtotime("2 hour"))
referalsum_ = php_file_get_contents(str("foydalanuvchi/hisob/") + str(fid_) + str(".txt"))
referalid_ = php_file_get_contents(str("foydalanuvchi/referal/") + str(fid_) + str(".referal"))
referalcid_ = php_file_get_contents(str("foydalanuvchi/referal/") + str(ccid_) + str(".referal"))
userstep_ = php_file_get_contents(str("step/") + str(fid_) + str(".txt"))
userstep1_ = php_file_get_contents(str("step/") + str(fid_) + str(".txt1"))
if php_mb_stripos(text_, str("/start ") + str(cid_)):
    bot("SendMessage", Array({"chat_id": cid_, "text": "", "parse_mode": "html"}))
else:
    idref_ = str("foydalanuvchi/referal/") + str(ex_) + str(".db")
    idref2_ = php_file_get_contents(idref_)
    id_ = str(cid_) + str("\n")
    handle_ = fopen(idref_, "a+")
    fwrite(handle_, id_)
    php_fclose(handle_)
    if php_mb_stripos(idref2_, cid_) != False:
        pass
    else:
        pub_ = php_explode(" ", text_)
        ex_ = pub_[1]
        pulim_ = php_file_get_contents(str("foydalanuvchi/hisob/") + str(ex_) + str(".txt"))
        a_ = pulim_ + taklifpul_
        file_put_contents(str("foydalanuvchi/hisob/") + str(ex_) + str(".txt"), str(a_))
        odam_ = php_file_get_contents(str("foydalanuvchi/referal/") + str(ex_) + str(".txt"))
        b_ = odam_ + 1
        file_put_contents(str("foydalanuvchi/referal/") + str(ex_) + str(".txt"), str(b_))
        bot("SendMessage", Array({"chat_id": cid_, "text": "", "parse_mode": "html", "reply_markup": main_menu_}))
        bot("SendMessage", Array({"chat_id": ex_, "text": str("<b>ð³ Sizda yangi <a href='tg://user?id=") + str(cid_) + str("'>taklif</a> mavjud!</b>\n\n<i>Hisobingizga ") + str(taklifpul_) + str(" ") + str(pul_) + str(" qo'shildi!</i>"), "parse_mode": "html"}))
    # end if
# end if
if tx_:
    if ban_ == "ban":
        sys.exit(0)
    # end if
# end if
if data_:
    ban_ = php_file_get_contents(str("ban/") + str(ccid_) + str(".txt"))
    if ban_ == "ban":
        sys.exit(0)
    # end if
# end if
main_menu_ = php_json_encode(Array({"resize_keyboard": True, "keyboard": Array(Array(Array({"text": str(tugma1_)}), Array({"text": "ð¦ Buyurtma berish"})), Array(Array({"text": str(tugma2_)}), Array({"text": str(tugma3_)})), Array(Array({"text": "ð Buyurtma kuzatish"}), Array({"text": str(tugma4_)})))}))
#// manba: @education_coders
#// dasturchi: @muzadev. tahrirchi:@uzder_php. @education_coders kanali orqali tarqatildi!!! manba bilan olmagan kut!!!
main_menuad_ = php_json_encode(Array({"resize_keyboard": True, "keyboard": Array(Array(Array({"text": str(tugma1_)})), Array(Array({"text": str(tugma2_)}), Array({"text": str(tugma3_)})), Array(Array({"text": str(tugma4_)})), Array(Array({"text": str(tugma2_)}), Array({"text": str(tugma3_)})), Array(Array({"text": "ð Boshqaruv"})))}))
asosiy_soz_ = php_json_encode(Array({"resize_keyboard": True, "keyboard": Array(Array(Array({"text": "*â£ Birlamchi sozlamalar"})), Array(Array({"text": "ð¢ Kanallar"}), Array({"text": "ð¤ Bot holati"})), Array(Array({"text": "ð Api sozlamalari"})), Array(Array({"text": "ð¤ Botlar"}), Array({"text": "ðï¸ Xizmatlar"})), Array(Array({"text": "ð Boshqaruv"})))}))
if tx_ == "âï¸ Asosiy sozlamalar":
    if cid_ == admin_:
        bot("sendMessage", Array({"chat_id": admin_, "text": "<b>ð Boshqaruv paneliga xush kelibsiz!</b>", "parse_mode": "html", "reply_markup": asosiy_soz_}))
    else:
        bot("sendMessage", Array({"chat_id": cid_, "text": "<b>ð¥ Asosiy menyudasiz</b>", "parse_mode": "html"}))
    # end if
# end if
if text_ == "ð Orqaga" and joinchat(cid_) == True:
    bot("sendMessage", Array({"chat_id": cid_, "text": "Menu tanlang", "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "ð¦ Nakrutka BoÊ»lim", "callback_data": "nak_menu"})), Array(Array({"text": "ð¤ Maker BoÊ»lim", "callback_data": "mak_menu"})))}))}))
# end if
#// manba: @education_coders
#// dasturchi: @muzadev. tahrirchi:@uzder_php. @education_coders kanali orqali tarqatildi!!! manba bilan olmagan kut!!!
#// manba bilan olmagan kut!!!
admin1_menu_ = php_json_encode(Array({"resize_keyboard": True, "keyboard": Array(Array(Array({"text": "âï¸ Asosiy sozlamalar"})), Array(Array({"text": "ð Tugmalar"}), Array({"text": "ð³ Hamyonlar"})), Array(Array({"text": "ð Foydalanuvchini boshqarish"})), Array(Array({"text": "ð¨ Xabarnoma"}), Array({"text": "ð Statistika"})), Array(Array({"text": "ð Orqaga"})))}))
if data_ == "nak_menu":
    bot("deleteMessage", Array({"chat_id": ccid_, "message_id": cmid_}))
    bot("sendMessage", Array({"chat_id": ccid_, "text": "<b>ð Nakrutka boÊ»limiga xush kelibsiz!</b>", "parse_mode": "html", "reply_markup": nak_menu_}))
    unlink("step/odam.txt")
# end if
if data_ == "mak_menu":
    bot("deleteMessage", Array({"chat_id": ccid_, "message_id": cmid_}))
    bot("sendMessage", Array({"chat_id": ccid_, "text": "<b>ð Maker boÊ»limiga xush kelibsiz!</b>", "parse_mode": "html", "reply_markup": main_menu_}))
    unlink("step/odam.txt")
# end if
if data_ == "boshqaruv" and ccid_ == admin_:
    bot("deleteMessage", Array({"chat_id": admin_, "message_id": cmid_}))
    bot("sendMessage", Array({"chat_id": admin_, "text": "<b>ð Boshqaruv paneliga xush kelibsiz!</b>", "parse_mode": "html", "reply_markup": admin1_menu_}))
    unlink("step/odam.txt")
# end if
orqaga1_ = php_json_encode(Array({"resize_keyboard": True, "keyboard": Array(Array(Array({"text": "ð Boshqaruv"})))}))
if tx_ == "ð Boshqaruv" and cid_ == admin_:
    bot("sendMessage", Array({"chat_id": admin_, "text": "<b>ð Boshqaruv paneliga xush kelibsiz!</b>", "parse_mode": "html", "reply_markup": admin1_menu_}))
    unlink(str("step/") + str(cid_) + str(".txt"))
    unlink("miqdor.txt")
    unlink("fbsh.txt")
# end if
orqamak_ = php_json_encode(Array({"resize_keyboard": True, "keyboard": Array(Array(Array({"text": "ð Orqaga"})))}))
if tx_ == "ð Orqaga":
    bot("sendMessage", Array({"chat_id": cid_, "text": "<b>ð Orqaga qaytingiz</b>", "parse_mode": "html", "reply_markup": main_menu_}))
    unlink(str("step/") + str(cid_) + str(".txt"))
    unlink("miqdor.txt")
    unlink("fbsh.txt")
# end if
orqanak_ = php_json_encode(Array({"resize_keyboard": True, "keyboard": Array(Array(Array({"text": "â¬ï¸ Orqaga"})))}))
if tx_ == "â¬ï¸ Orqaga":
    bot("sendMessage", Array({"chat_id": cid_, "text": "<b>ð Orqaga qaytingiz</b>", "parse_mode": "html", "reply_markup": nak_menu_}))
    unlink(str("step/") + str(cid_) + str(".txt"))
    unlink("miqdor.txt")
    unlink("fbsh.txt")
# end if
oddiy_xabar_ = php_file_get_contents("oddiy.txt")
if data_ == "oddiy_xabar" and ccid_ == admin_:
    lichka_ = php_file_get_contents("statistika/obunachi.txt")
    lich_ = php_substr_count(lichka_, "\n")
    bot("deleteMessage", Array({"chat_id": admin_, "message_id": cmid_}))
    bot("sendMessage", Array({"chat_id": admin_, "text": str("<b>") + str(lich_) + str(" ta foydalanuvchiga yuboriladigan xabar matnini yuboring:</b>"), "parse_mode": "html", "reply_markup": php_json_encode(Array({"resize_keyboard": True, "keyboard": Array(Array(Array({"text": "ð Boshqaruv"})))}))}))
    file_put_contents("oddiy.txt", "oddiy")
# end if
if oddiy_xabar_ == "oddiy" and cid_ == admin_:
    if tx_ == "ð Boshqaruv":
        unlink("oddiy.txt")
    else:
        lichka_ = php_file_get_contents("statistika/obunachi.txt")
        lich_ = php_substr_count(lichka_, "\n")
        bot("sendmessage", Array({"chat_id": admin_, "text": str("<b>") + str(lich_) + str(" ta foydalanuvchiga xabar yuborish boshlandi!</b>"), "parse_mode": "html", "reply_markup": admin1_menu_}))
        lich_ = php_file_get_contents("statistika/obunachi.txt")
        lichka_ = php_explode("\n", lich_)
        for lichkalar_ in lichka_:
            usr_ = bot("sendMessage", Array({"chat_id": lichkalar_, "text": text_, "parse_mode": "HTML"}))
            unlink("oddiy.txt")
        # end for
    # end if
# end if
if usr_:
    lichka_ = php_file_get_contents("statistika/obunachi.txt")
    lich_ = php_substr_count(lichka_, "\n")
    bot("sendmessage", Array({"chat_id": admin_, "text": str("<b>") + str(lich_) + str(" ta foydalanuvchiga muvaffaqiyatli yuborildi</b>"), "parse_mode": "html", "reply_markup": admin1_menu_}))
    unlink("oddiy.txt")
# end if
forward_xabar_ = php_file_get_contents("forward.txt")
if data_ == "forward_xabar" and ccid_ == admin_:
    lichka_ = php_file_get_contents("statistika/obunachi.txt")
    lich_ = php_substr_count(lichka_, "\n")
    bot("deleteMessage", Array({"chat_id": admin_, "message_id": cmid_}))
    bot("sendMessage", Array({"chat_id": admin_, "text": str("<b>") + str(lich_) + str(" ta foydalanuvchiga yuboriladigan xabarni forward shaklida yuboring:</b>"), "parse_mode": "html", "reply_markup": php_json_encode(Array({"resize_keyboard": True, "keyboard": Array(Array(Array({"text": "ð Boshqaruv"})))}))}))
    file_put_contents("forward.txt", "forward")
# end if
if forward_xabar_ == "forward" and cid_ == admin_:
    if tx_ == "ð Boshqaruv":
        unlink("forward.txt")
    else:
        lichka_ = php_file_get_contents("statistika/obunachi.txt")
        lich_ = php_substr_count(lichka_, "\n")
        bot("sendmessage", Array({"chat_id": admin_, "text": str("<b>") + str(lich_) + str(" ta foydalanuvchiga xabar yuborish boshlandi!</b>"), "parse_mode": "html", "reply_markup": admin1_menu_}))
        lich_ = php_file_get_contents("statistika/obunachi.txt")
        lichka_ = php_explode("\n", lich_)
        for lichkalar_ in lichka_:
            fors_ = bot("forwardMessage", Array({"from_chat_id": cid_, "chat_id": lichkalar_, "message_id": mid_}))
            unlink("forward.txt")
        # end for
    # end if
# end if
if fors_:
    lichka_ = php_file_get_contents("statistika/obunachi.txt")
    lich_ = php_substr_count(lichka_, "\n")
    bot("sendmessage", Array({"chat_id": admin_, "text": str("<b>") + str(lich_) + str(" ta foydalanuvchiga muvaffaqiyatli yuborildi</b>"), "parse_mode": "html", "reply_markup": admin1_menu_}))
    unlink("forward.txt")
# end if
if tx_ == "ð¨ Xabarnoma" and cid_ == admin_:
    bot("sendMessage", Array({"chat_id": admin_, "text": "<b>ð¨ Yuboriladigan xabar turini tanlang:</b>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "Oddiy xabar", "callback_data": "oddiy_xabar"})), Array(Array({"text": "Forward xabar", "callback_data": "forward_xabar"})))}))}))
# end if
if tx_ == "ð¤ Botlar" and cid_ == admin_:
    bot("sendMessage", Array({"chat_id": cid_, "text": "ð¤ <b>Botlarni sozlash bo'limidasiz:</b>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "ð Kategoriyalar", "callback_data": "kategoriya"})), Array(Array({"text": "ð¤ Botlarni sozlash", "callback_data": "BotSet"})))}))}))
# end if
if data_ == "bbosh":
    bot("deleteMessage", Array({"chat_id": ccid_, "message_id": cmid_}))
    bot("sendMessage", Array({"chat_id": ccid_, "text": "ð¤ <b>Botlarni sozlash bo'limidasiz:</b>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "ð Kategoriyalar", "callback_data": "kategoriya"})), Array(Array({"text": "ð¤ Botlarni sozlash", "callback_data": "BotSet"})))}))}))
# end if
if data_ == "kategoriya":
    bot("editMessageText", Array({"chat_id": ccid_, "message_id": cmid_, "text": "ð <b>Quyidagilardan birini tanlang:</b>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "â Kategoriya qo'shish", "callback_data": "AdKat"})), Array(Array({"text": "ð Kategoriyalar ro'yxati", "callback_data": "listKat"})), Array(Array({"text": "ð Orqaga", "callback_data": "bbosh"})))}))}))
# end if
if data_ == "BotSet":
    bot("editMessageText", Array({"chat_id": ccid_, "message_id": cmid_, "text": "ð¤ <b>Quyidagilardan birini tanlang:</b>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "â Bot qo'shish", "callback_data": "AdBot"})), Array(Array({"text": "ð Botlar ro'yxati", "callback_data": "listBot"})), Array(Array({"text": "âï¸ Orqaga", "callback_data": "bbosh"})))}))}))
# end if
if data_ == "listKat":
    more_ = php_explode("\n", kategoriya_)
    soni_ = php_substr_count(kategoriya_, "\n")
    keys_ = Array()
    for_ = 1
    while for_ <= soni_:
        
        title_ = php_str_replace("\n", "", more_[for_])
        keys_[-1] = Array({"text": str(title_) + str(" - sozlash"), "callback_data": str("setKat-") + str(title_)})
        keysboard2_ = array_chunk(keys_, 1)
        keysboard2_[-1] = Array(Array({"text": "âï¸ Orqaga", "callback_data": "bbosh"}))
        key_ = php_json_encode(Array({"inline_keyboard": keysboard2_}))
        for_ += 1
    # end while
    if kategoriya_ != None:
        bot("editMessageText", Array({"chat_id": ccid_, "message_id": cmid_, "text": "<b>ð Kategoriyalar ro'yxati:</b>", "parse_mode": "html", "reply_markup": key_}))
    else:
        bot("answerCallbackQuery", Array({"callback_query_id": callid_, "text": "ð Kategoriyalar mavjud emas!", "show_alert": True}))
    # end if
# end if
if php_mb_stripos(data_, "setKat-") != False:
    ex_ = php_explode("-", data_)
    kat_ = ex_[1]
    bot("editMessageText", Array({"chat_id": ccid_, "message_id": cmid_, "text": str("ð <b>Kategoriya nomi:</b> ") + str(kat_), "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "ð O'chirish", "callback_data": str("delKat-") + str(kat_)})), Array(Array({"text": "âï¸ Orqaga", "callback_data": "listKat"})))}))}))
# end if
if php_mb_stripos(data_, "delKat-") != False:
    ex_ = php_explode("-", data_)
    kat_ = ex_[1]
    k_ = php_str_replace("\n" + kat_ + "", "", kategoriya_)
    file_put_contents("sozlamalar/bot/kategoriya.txt", k_)
    bot("editMessageText", Array({"chat_id": ccid_, "message_id": cmid_, "text": "<b>O'chirish yakunlandi!</b>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "âï¸ Orqaga", "callback_data": "kategoriya"})))}))}))
    deleteFolder(str("sozlamalar/bot/") + str(kat_))
# end if
if data_ == "listBot":
    kategoriya_ = php_file_get_contents("sozlamalar/bot/kategoriya.txt")
    more_ = php_explode("\n", kategoriya_)
    soni_ = php_substr_count(kategoriya_, "\n")
    keys_ = Array()
    for_ = 1
    while for_ <= soni_:
        
        title_ = php_str_replace("\n", "", more_[for_])
        keys_[-1] = Array({"text": str(title_) + str(" â©"), "callback_data": str("setBot-") + str(title_)})
        keysboard2_ = array_chunk(keys_, 1)
        keysboard2_[-1] = Array(Array({"text": "âï¸ Orqaga", "callback_data": "bbosh"}))
        key_ = php_json_encode(Array({"inline_keyboard": keysboard2_}))
        for_ += 1
    # end while
    if kategoriya_ != None:
        bot("editMessageText", Array({"chat_id": ccid_, "message_id": cmid_, "text": "<b>ð Kategoriyalardan birini tanlang:</b>", "parse_mode": "html", "reply_markup": key_}))
    else:
        bot("answerCallbackQuery", Array({"callback_query_id": callid_, "text": "ð Kategoriyalar mavjud emas!", "show_alert": True}))
    # end if
# end if
if php_mb_stripos(data_, "setBot-") != False:
    ex_ = php_explode("-", data_)
    kat_ = ex_[1]
    royxat_ = php_file_get_contents(str("sozlamalar/bot/") + str(kat_) + str("/royxat.txt"))
    kategoriya_ = php_file_get_contents("sozlamalar/bot/kategoriya.txt")
    more_ = php_explode("\n", royxat_)
    soni_ = php_substr_count(royxat_, "\n")
    keys_ = Array()
    for_ = 1
    while for_ <= soni_:
        
        title_ = php_str_replace("\n", "", more_[for_])
        keys_[-1] = Array({"text": str("â ") + str(title_), "callback_data": str("bset-") + str(title_) + str("-") + str(kat_)})
        keysboard2_ = array_chunk(keys_, 2)
        keysboard2_[-1] = Array(Array({"text": "âï¸ Orqaga", "callback_data": "bbosh"}))
        key_ = php_json_encode(Array({"inline_keyboard": keysboard2_}))
        for_ += 1
    # end while
    if royxat_ != None:
        bot("editMessageText", Array({"chat_id": ccid_, "message_id": cmid_, "text": "ð <b>Botlar ro'yxati:</b>", "parse_mode": "html", "reply_markup": key_}))
    else:
        bot("answerCallbackQuery", Array({"callback_query_id": callid_, "text": "ð Botlar mavjud emas!", "show_alert": True}))
    # end if
# end if
if php_mb_stripos(data_, "bset-") != False:
    ex_ = php_explode("-", data_)
    roy_ = ex_[1]
    kat_ = ex_[2]
    narx_ = php_file_get_contents(str("sozlamalar/bot/") + str(kat_) + str("/") + str(roy_) + str("/narx.txt"))
    tavsif_ = php_file_get_contents(str("sozlamalar/bot/") + str(kat_) + str("/") + str(roy_) + str("/tavsif.txt"))
    type_ = php_file_get_contents(str("sozlamalar/bot/") + str(kat_) + str("/") + str(roy_) + str("/turi.txt"))
    bot("editMessageText", Array({"chat_id": ccid_, "message_id": cmid_, "text": str("<b>ð¤ ") + str(type_) + str("""</b>\n\n<b>ð¬ Bot tili:</b> O'zbekcha\n<b>ðµ Narxi:</b> """) + str(narx_) + str(" ") + str(pul_) + str("\n<b>ð Kunlik to'lov:</b> 200 ") + str(pul_) + str("\n\nð <b>Qo'shimcha ma'lumot:</b> <i>") + str(tavsif_) + str("</i>"), "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "ð O'chirish", "callback_data": str("delBot-") + str(kat_) + str("-") + str(roy_) + str("-") + str(type_)})), Array(Array({"text": "âï¸ Orqaga", "callback_data": "listBot"})))}))}))
# end if
if php_mb_stripos(data_, "delBot-") != False:
    ex_ = php_explode("-", data_)
    kat_ = ex_[1]
    roy_ = ex_[2]
    type_ = ex_[3]
    royxat_ = php_file_get_contents(str("sozlamalar/bot/") + str(kat_) + str("/royxat.txt"))
    k_ = php_str_replace("\n" + roy_ + "", "", royxat_)
    file_put_contents(str("sozlamalar/bot/") + str(kat_) + str("/royxat.txt"), k_)
    bot("editMessageText", Array({"chat_id": ccid_, "message_id": cmid_, "text": "<b>O'chirish yakunlandi!</b>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "âï¸ Orqaga", "callback_data": "listBot"})))}))}))
    deleteFolder(str("sozlamalar/bot/") + str(kat_) + str("/") + str(roy_))
    unlink(str("sozlamalar/bot/") + str(type_) + str(".php"))
# end if
if data_ == "AdKat":
    bot("sendMessage", Array({"chat_id": ccid_, "text": "<b>ð Yangi kategoriya nomini yuboring:</b>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"resize_keyboard": True, "keyboard": Array(Array(Array({"text": "ð Boshqaruv"})))}))}))
    file_put_contents(str("step/") + str(ccid_) + str(".txt"), "AdKat")
    sys.exit(0)
# end if
if userstep_ == "AdKat":
    if tx_ == "ð Boshqaruv":
        unlink(str("step/") + str(cid_) + str(".txt"))
    else:
        if cid_ == admin_:
            if (php_isset(lambda : text_)):
                kategoriya_ = php_file_get_contents("sozlamalar/bot/kategoriya.txt")
                file_put_contents("sozlamalar/bot/kategoriya.txt", str(kategoriya_) + str("\n") + str(text_))
                mkdir(str("sozlamalar/bot/") + str(text_))
                bot("SendMessage", Array({"chat_id": cid_, "text": str(text_) + str(" <b>nomli kategoriya qo'shildi</b>"), "parse_mode": "html", "reply_markup": admin1_menu_}))
            # end if
            unlink(str("step/") + str(cid_) + str(".txt"))
        # end if
    # end if
# end if
if data_ == "AdBot":
    kategoriya_ = php_file_get_contents("sozlamalar/bot/kategoriya.txt")
    more_ = php_explode("\n", kategoriya_)
    soni_ = php_substr_count(kategoriya_, "\n")
    keys_ = Array()
    for_ = 1
    while for_ <= soni_:
        
        title_ = php_str_replace("\n", "", more_[for_])
        keys_[-1] = Array({"text": str(title_), "callback_data": str("addb-") + str(title_)})
        keysboard2_ = array_chunk(keys_, 1)
        keysboard2_[-1] = Array(Array({"text": "âï¸ Orqaga", "callback_data": "bbosh"}))
        AdBot_ = php_json_encode(Array({"inline_keyboard": keysboard2_}))
        for_ += 1
    # end while
    if kategoriya_ != None:
        bot("editMessageText", Array({"chat_id": ccid_, "message_id": cmid_, "text": "<b>ð Qaysi kategoriyaga qo'shamiz?</b>", "parse_mode": "html", "reply_markup": AdBot_}))
    else:
        bot("answerCallbackQuery", Array({"callback_query_id": callid_, "text": "ð Kategoriyalar mavjud emas!", "show_alert": True}))
    # end if
# end if
if php_mb_stripos(data_, "addb-") != False:
    ex_ = php_explode("-", data_)
    kat_ = ex_[1]
    bot("deleteMessage", Array({"chat_id": ccid_, "message_id": cmid_}))
    bot("sendMessage", Array({"chat_id": ccid_, "text": """<b>â Kategoriya tanlandi</b>
    ð Bot turini yuboring: 
    <i>Stikersiz yuboring!</i>""", "parse_mode": "html", "reply_markup": php_json_encode(Array({"resize_keyboard": True, "keyboard": Array(Array(Array({"text": "ð Boshqaruv"})))}))}))
    file_put_contents(str("step/") + str(ccid_) + str(".txt"), str("turi-") + str(kat_))
    sys.exit(0)
# end if
if php_mb_stripos(userstep_, "turi-") != False:
    ex_ = php_explode("-", userstep_)
    kat_ = ex_[1]
    if tx_ == "ð Boshqaruv":
        unlink(str("step/") + str(cid_) + str(".txt"))
    else:
        if (php_isset(lambda : text_)):
            royxat_ = php_file_get_contents(str("sozlamalar/bot/") + str(kat_) + str("/royxat.txt"))
            file_put_contents(str("sozlamalar/bot/") + str(kat_) + str("/royxat.txt"), str(royxat_) + str("\n") + str(text_))
            mkdir(str("sozlamalar/bot/") + str(kat_) + str("/") + str(text_))
            file_put_contents(str("sozlamalar/bot/") + str(kat_) + str("/") + str(text_) + str("/turi.txt"), text_)
            bot("SendMessage", Array({"chat_id": cid_, "text": str(text_) + str(" <b>nomi qabul qilindi.</b>\n\nð Bot uchun narx yuboring:"), "parse_mode": "html"}))
            file_put_contents(str("step/") + str(cid_) + str(".txt"), str("narxi-") + str(kat_) + str("-") + str(text_) + str("-") + str(text_))
        else:
            bot("SendMessage", Array({"chat_id": cid_, "text": "<b>â ï¸ Faqat harflardan foydalaning!</b>", "parse_mode": "html"}))
        # end if
    # end if
# end if
if php_mb_stripos(userstep_, "narxi-") != False:
    ex_ = php_explode("-", userstep_)
    kat_ = ex_[1]
    roy_ = ex_[2]
    type_ = ex_[3]
    if tx_ == "ð Boshqaruv":
        unlink(str("step/") + str(cid_) + str(".txt"))
        unlink(str("sozlamalar/bot/") + str(kat_) + str("/") + str(roy_))
        royxat_ = php_file_get_contents(str("sozlamalar/bot/") + str(kat_) + str("/royxat.txt"))
        k_ = php_str_replace("\n" + roy_ + "", "", royxat_)
        file_put_contents(str("sozlamalar/bot/") + str(kat_) + str("/royxat.txt"), k_)
    else:
        if php_is_numeric(text_) == True:
            file_put_contents(str("sozlamalar/bot/") + str(kat_) + str("/") + str(roy_) + str("/narx.txt"), text_)
            bot("SendMessage", Array({"chat_id": cid_, "text": str("<b>") + str(text_) + str(" </b>") + str(pul_) + str(" narxi qabul qilindi\n\nð Bot haqida malumot yuboring:"), "parse_mode": "html"}))
            file_put_contents(str("step/") + str(cid_) + str(".txt"), str("tavsif-") + str(kat_) + str("-") + str(roy_) + str("-") + str(type_))
        else:
            bot("SendMessage", Array({"chat_id": cid_, "text": "<b>â ï¸ Faqat raqamlardan foydalaning!</b>", "parse_mode": "html"}))
        # end if
    # end if
# end if
if php_mb_stripos(userstep_, "tavsif-") != False:
    ex_ = php_explode("-", userstep_)
    kat_ = ex_[1]
    roy_ = ex_[2]
    type_ = ex_[3]
    if tx_ == "ð Boshqaruv":
        unlink(str("step/") + str(cid_) + str(".txt"))
        unlink(str("sozlamalar/bot/") + str(kat_) + str("/") + str(roy_))
        royxat_ = php_file_get_contents(str("sozlamalar/bot/") + str(kat_) + str("/royxat.txt"))
        k_ = php_str_replace("\n" + roy_ + "", "", royxat_)
        file_put_contents(str("sozlamalar/bot/") + str(kat_) + str("/royxat.txt"), k_)
    else:
        if (php_isset(lambda : text_)):
            file_put_contents(str("sozlamalar/bot/") + str(kat_) + str("/") + str(roy_) + str("/tavsif.txt"), text_)
            bot("SendMessage", Array({"chat_id": cid_, "text": str("<b>Qabul qilindi</b>\n\nð Bot kodini yuboring: ") + str(type_) + str(".php bo'lishi kerak!"), "parse_mode": "html"}))
            file_put_contents(str("step/") + str(cid_) + str(".txt"), str("script-") + str(kat_) + str("-") + str(roy_) + str("-") + str(type_))
        else:
            bot("SendMessage", Array({"chat_id": cid_, "text": "<b>â ï¸ Faqat harflardan foydalaning!</b>", "parse_mode": "html"}))
        # end if
    # end if
# end if
if php_mb_stripos(userstep_, "script-") != False:
    ex_ = php_explode("-", userstep_)
    kat_ = ex_[1]
    roy_ = ex_[2]
    type_ = ex_[3]
    if tx_ == "ð Boshqaruv":
        unlink(str("step/") + str(cid_) + str(".txt"))
        unlink(str("sozlamalar/bot/") + str(kat_) + str("/") + str(roy_))
        royxat_ = php_file_get_contents(str("sozlamalar/bot/") + str(kat_) + str("/royxat.txt"))
        k_ = php_str_replace("\n" + roy_ + "", "", royxat_)
        file_put_contents(str("sozlamalar/bot/") + str(kat_) + str("/royxat.txt"), k_)
    else:
        if (php_isset(lambda : doc_)):
            url_ = php_json_decode(php_file_get_contents("https://api.telegram.org/bot" + API_KEY + "/getFile?file_id=" + doc_id_), True)
            path_ = url_["result"]["file_path"]
            file_ = "https://api.telegram.org/file/bot" + API_KEY + "/" + path_
            ok_ = file_put_contents(str("botlar/") + str(type_) + str(".php"), php_file_get_contents(file_))
            bot("SendMessage", Array({"chat_id": cid_, "text": "<b>â Yangi bot qo'shildi</b>", "parse_mode": "html", "reply_markup": admin1_menu_}))
            unlink(str("step/") + str(cid_) + str(".txt"))
        else:
            bot("SendMessage", Array({"chat_id": cid_, "text": str("<b>Qabul qilindi</b>\n\nð Bot kodini yuboring: ") + str(type_) + str(".php bo'lishi kerak!"), "parse_mode": "html"}))
        # end if
    # end if
# end if
taklif_ = php_file_get_contents("taklif.txt")
if data_ == "taklif_narxi" and ccid_ == admin_:
    bot("sendMessage", Array({"chat_id": admin_, "message_id": cmid_}))
    bot("sendMessage", Array({"chat_id": admin_, "text": "<b>ð Yangi qiymatni yuboring:</b>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"resize_keyboard": True, "keyboard": Array(Array(Array({"text": "ð Boshqaruv"})))}))}))
    file_put_contents("taklif.txt", "taklif")
# end if
if taklif_ == "taklif" and cid_ == admin_:
    if tx_ == "ð Boshqaruv":
        unlink("taklif.txt")
    else:
        file_put_contents("sozlamalar/pul/referal.txt", str(tx_))
        bot("sendMessage", Array({"chat_id": admin_, "text": "<b>Muvaffaqiyatli o'zgartirildi!</b>", "parse_mode": "html", "reply_markup": admin1_menu_}))
        unlink("taklif.txt")
    # end if
# end if
valyuta_ = php_file_get_contents("valyuta.txt")
if data_ == "valyuta_nomi" and ccid_ == admin_:
    bot("sendMessage", Array({"chat_id": admin_, "message_id": cmid_}))
    bot("sendMessage", Array({"chat_id": admin_, "text": "<b>ð Yangi qiymatni yuboring:</b>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"resize_keyboard": True, "keyboard": Array(Array(Array({"text": "ð Boshqaruv"})))}))}))
    file_put_contents("valyuta.txt", "valyuta")
# end if
if valyuta_ == "valyuta" and cid_ == admin_:
    if tx_ == "ð Boshqaruv":
        unlink("valyuta.txt")
    else:
        file_put_contents("sozlamalar/pul/valyuta.txt", str(tx_))
        bot("sendMessage", Array({"chat_id": admin_, "text": "<b>Muvaffaqiyatli o'zgartirildi!</b>", "parse_mode": "html", "reply_markup": admin1_menu_}))
        unlink("valyuta.txt")
    # end if
# end if
fbsh_ = php_file_get_contents("fbsh.txt")
if tx_ == "ð Foydalanuvchini boshqarish" and cid_ == admin_:
    bot("sendMessage", Array({"chat_id": admin_, "text": "<b>Kerakli foydalanuvchining ID raqamini yuboring:</b>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"resize_keyboard": True, "keyboard": Array(Array(Array({"text": "ð Boshqaruv"})))}))}))
    file_put_contents("fbsh.txt", "idraqam")
# end if
if fbsh_ == "idraqam" and cid_ == admin_:
    if tx_ == "ð Boshqaruv":
        unlink("fbsh.txt")
    else:
        if php_file_exists(str("ban/") + str(tx_) + str(".txt")):
            if php_file_exists(str("foydalanuvchi/hisob/") + str(tx_) + str(".txt")):
                file_put_contents("step/odam.txt", tx_)
                asos_ = php_file_get_contents(str("foydalanuvchi/hisob/") + str(tx_) + str(".txt"))
                tpul_ = php_file_get_contents(str("foydalanuvchi/hisob/") + str(tx_) + str(".1txt"))
                kirit_ = php_file_get_contents(str("foydalanuvchi/hisob/") + str(tx_) + str(".1.txt"))
                odam_ = php_file_get_contents(str("foydalanuvchi/referal/") + str(tx_) + str(".txt"))
                bot("sendMessage", Array({"chat_id": admin_, "text": str("<b>â Foydalanuvchi topildi:</b> <a href='tg://user?id=") + str(tx_) + str("'>") + str(tx_) + str("</a>\n\n<b>Asosiy balans:</b> ") + str(asos_) + str(" ") + str(pul_) + str("\n<b>Sarmoya balans:</b> ") + str(tpul_) + str(" ") + str(pul_) + str("\n<b>Takliflari:</b> ") + str(odam_) + str(" ta\n\n<b>Kiritgan pullari:</b> ") + str(kirit_) + str(" ") + str(pul_), "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "ð Bandan olish", "callback_data": "unban"})), Array(Array({"text": "â Pul qo'shish", "callback_data": "val_qoshish"}), Array({"text": "â Pul ayirish", "callback_data": "val_ayirish"})), Array(Array({"text": "ð Sarmoya qo'shish", "callback_data": "tolov_qoshish"}), Array({"text": "ð Sarmoya ayirish", "callback_data": "tolov_ayirish"})))}))}))
                unlink("fbsh.txt")
            else:
                bot("SendMessage", Array({"chat_id": admin_, "text": "<b>Ushbu foydalanuvchi botdan foydalanmaydi!</b>\n\n<i>Qayta yuboring:</i>", "parse_mode": "html"}))
            # end if
        else:
            if php_file_exists(str("foydalanuvchi/hisob/") + str(tx_) + str(".txt")):
                file_put_contents("step/odam.txt", tx_)
                asos_ = php_file_get_contents(str("foydalanuvchi/hisob/") + str(tx_) + str(".txt"))
                tpul_ = php_file_get_contents(str("foydalanuvchi/hisob/") + str(tx_) + str(".1txt"))
                kirit_ = php_file_get_contents(str("foydalanuvchi/hisob/") + str(tx_) + str(".1.txt"))
                odam_ = php_file_get_contents(str("foydalanuvchi/referal/") + str(tx_) + str(".txt"))
                bot("sendMessage", Array({"chat_id": admin_, "text": str("<b>â Foydalanuvchi topildi:</b> <a href='tg://user?id=") + str(tx_) + str("'>") + str(tx_) + str("</a>\n\n<b>Asosiy balans:</b> ") + str(asos_) + str(" ") + str(pul_) + str("\n<b>Sarmoya balans:</b> ") + str(tpul_) + str(" ") + str(pul_) + str("\n<b>Takliflari:</b> ") + str(odam_) + str(" ta\n\n<b>Kiritgan pullari:</b> ") + str(kirit_) + str(" ") + str(pul_), "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "ð Banlash", "callback_data": "ban"})), Array(Array({"text": "â Pul qo'shish", "callback_data": "val_qoshish"}), Array({"text": "â Pul ayirish", "callback_data": "val_ayirish"})), Array(Array({"text": "ð Sarmoya qo'shish", "callback_data": "tolov_qoshish"}), Array({"text": "ð Sarmoya ayirish", "callback_data": "tolov_ayirish"})))}))}))
                unlink("fbsh.txt")
            else:
                bot("SendMessage", Array({"chat_id": admin_, "text": "<b>Ushbu foydalanuvchi botdan foydalanmaydi!</b>\n\n<i>Qayta yuboring:</i>", "parse_mode": "html"}))
            # end if
        # end if
    # end if
# end if
if data_ == "ban":
    file_put_contents(str("ban/") + str(saved_) + str(".txt"), "ban")
    bot("deleteMessage", Array({"chat_id": ccid_, "message_id": cmid_}))
    bot("sendMessage", Array({"chat_id": ccid_, "text": str("<a href='tg://user?id=") + str(saved_) + str("'>") + str(saved_) + str("</a> <b>banlandi</b>"), "parse_mode": "html", "reply_markup": admin1_menu_}))
    bot("sendMessage", Array({"chat_id": saved_, "text": "<b>Admin tomonidan bloklandingiz!</b>", "parse_mode": "html"}))
    unlink("step/odam.txt")
# end if
if data_ == "unban":
    unlink(str("ban/") + str(saved_) + str(".txt"))
    bot("deleteMessage", Array({"chat_id": ccid_, "message_id": cmid_}))
    bot("sendMessage", Array({"chat_id": ccid_, "text": str("<a href='tg://user?id=") + str(saved_) + str("'>") + str(saved_) + str("</a> <b>banlandan olindi</b>"), "parse_mode": "html", "reply_markup": admin1_menu_}))
    bot("sendMessage", Array({"chat_id": saved_, "text": "<b>Admin tomonidan blokdan olindingiz!</b>", "parse_mode": "html"}))
    unlink("step/odam.txt")
# end if
valqosh_ = php_file_get_contents("valqosh.txt")
if data_ == "val_qoshish" and ccid_ == admin_:
    file_put_contents("valqosh.txt", "valqosh")
    bot("deleteMessage", Array({"chat_id": admin_, "message_id": cmid_}))
    bot("sendMessage", Array({"chat_id": admin_, "parse_mode": "html", "text": str("<a href='tg://user?id=") + str(saved_) + str("'>") + str(saved_) + str("</a> <b>ning hisobiga qancha pul qo'shmoqchisiz?</b>"), "reply_markup": php_json_encode(Array({"resize_keyboard": True, "keyboard": Array(Array(Array({"text": "ð Boshqaruv"})))}))}))
# end if
if valqosh_ == "valqosh" and cid_ == admin_:
    if tx_ == "ð Boshqaruv":
        unlink("valqosh.txt")
        unlink("step/odam.txt")
    else:
        bot("sendMessage", Array({"chat_id": saved_, "text": str("<b>Adminlar tomonidan hisobingiz ") + str(tx_) + str(" ") + str(pul_) + str(" to'ldirildi</b>"), "parse_mode": "html"}))
        bot("sendMessage", Array({"chat_id": admin_, "text": str("<b>Foydalanuvchi hisobiga ") + str(tx_) + str(" ") + str(pul_) + str(" qo'shildi</b>"), "parse_mode": "html", "reply_markup": admin1_menu_}))
        currency_ = php_file_get_contents(str("foydalanuvchi/hisob/") + str(saved_) + str(".1.txt"))
        get_ = php_file_get_contents(str("foydalanuvchi/hisob/") + str(saved_) + str(".txt"))
        get_ += tx_
        currency_ += tx_
        file_put_contents(str("foydalanuvchi/hisob/") + str(saved_) + str(".1.txt"), currency_)
        file_put_contents(str("foydalanuvchi/hisob/") + str(saved_) + str(".txt"), get_)
        unlink("valqosh.txt")
        unlink("step/odam.txt")
    # end if
# end if
valayir_ = php_file_get_contents("valayir.txt")
if data_ == "val_ayirish" and ccid_ == admin_:
    file_put_contents("valayir.txt", "valayir")
    bot("deleteMessage", Array({"chat_id": admin_, "message_id": cmid_}))
    bot("sendMessage", Array({"chat_id": admin_, "parse_mode": "html", "text": str("<a href='tg://user?id=") + str(saved_) + str("'>") + str(saved_) + str("</a> <b>ning hisobidan qancha pul ayirmoqchisiz?</b>"), "reply_markup": php_json_encode(Array({"resize_keyboard": True, "keyboard": Array(Array(Array({"text": "ð Boshqaruv"})))}))}))
# end if
if valayir_ == "valayir" and cid_ == admin_:
    if tx_ == "ð Boshqaruv":
        unlink("valayir.txt")
        unlink("step/odam.txt")
    else:
        bot("sendMessage", Array({"chat_id": saved_, "text": str("<b>Adminlar tomonidan hisobingizdan ") + str(tx_) + str(" ") + str(pul_) + str(" olib tashlandi</b>"), "parse_mode": "html"}))
        bot("sendMessage", Array({"chat_id": admin_, "text": str("<b>Foydalanuvchi hisobidan ") + str(tx_) + str(" ") + str(pul_) + str(" olib tashlandi</b>"), "parse_mode": "html", "reply_markup": admin1_menu_}))
        currency_ = php_file_get_contents(str("foydalanuvchi/hisob/") + str(saved_) + str(".1.txt"))
        get_ = php_file_get_contents(str("foydalanuvchi/hisob/") + str(saved_) + str(".txt"))
        get_ -= tx_
        currency_ -= tx_
        file_put_contents(str("foydalanuvchi/hisob/") + str(saved_) + str(".1.txt"), currency_)
        file_put_contents(str("foydalanuvchi/hisob/") + str(saved_) + str(".txt"), get_)
        unlink("valayir.txt")
        unlink("step/odam.txt")
    # end if
# end if
tolqosh_ = php_file_get_contents("tvalqosh.txt")
if data_ == "tolov_qoshish" and ccid_ == admin_:
    file_put_contents("tvalqosh.txt", "tvalqosh")
    bot("deleteMessage", Array({"chat_id": admin_, "message_id": cmid_}))
    bot("sendMessage", Array({"chat_id": admin_, "parse_mode": "html", "text": str("<a href='tg://user?id=") + str(saved_) + str("'>") + str(saved_) + str("</a> <b>ning sarmoya hisobiga qancha pul qo'shmoqchisiz?</b>"), "reply_markup": php_json_encode(Array({"resize_keyboard": True, "keyboard": Array(Array(Array({"text": "ð Boshqaruv"})))}))}))
# end if
if tolqosh_ == "tvalqosh" and cid_ == admin_:
    if tx_ == "ð Boshqaruv":
        unlink("tvalqosh.txt")
        unlink("step/odam.txt")
    else:
        bot("sendMessage", Array({"chat_id": saved_, "text": str("<b>Adminlar tomonidan sarmoya hisobingiz ") + str(tx_) + str(" ") + str(pul_) + str(" to'ldirildi</b>"), "parse_mode": "html"}))
        bot("sendMessage", Array({"chat_id": admin_, "text": str("<b>Foydalanuvchi sarmoya hisobiga ") + str(tx_) + str(" ") + str(pul_) + str(" qo'shildi!</b>"), "parse_mode": "html", "reply_markup": admin1_menu_}))
        currency_ = php_file_get_contents(str("foydalanuvchi/hisob/") + str(saved_) + str(".1.txt"))
        currency_ += tx_
        file_put_contents(str("foydalanuvchi/hisob/") + str(saved_) + str(".1.txt"), currency_)
        buyurtmab_ = php_file_get_contents(str("foydalanuvchi/hisob/") + str(saved_) + str(".1txt"))
        buyurtmab_ += tx_
        file_put_contents(str("foydalanuvchi/hisob/") + str(saved_) + str(".1txt"), buyurtmab_)
        unlink("tvalqosh.txt")
        unlink("step/odam.txt")
    # end if
# end if
tolayir_ = php_file_get_contents("tvalayir.txt")
if data_ == "tolov_ayirish" and ccid_ == admin_:
    file_put_contents("tvalayir.txt", "tvalayir")
    bot("deleteMessage", Array({"chat_id": admin_, "message_id": cmid_}))
    bot("sendMessage", Array({"chat_id": admin_, "parse_mode": "html", "text": str("<a href='tg://user?id=") + str(saved_) + str("'>") + str(saved_) + str("</a> <b>ning sarmoya hisobidan qancha pul ayirmoqchisiz?</b>"), "reply_markup": php_json_encode(Array({"resize_keyboard": True, "keyboard": Array(Array(Array({"text": "ð Boshqaruv"})))}))}))
# end if
if tolayir_ == "tvalayir" and cid_ == admin_:
    if tx_ == "ð Boshqaruv":
        unlink("tvalayir.txt")
        unlink("step/odam.txt")
    else:
        bot("sendMessage", Array({"chat_id": saved_, "text": str("<b>Adminlar tomonidan sarmoya hisobingizdan ") + str(tx_) + str(" ") + str(pul_) + str(" olib tashlandi</b>"), "parse_mode": "html"}))
        bot("sendMessage", Array({"chat_id": admin_, "text": str("<b>Foydalanuvchi sarmoya hisobidan ") + str(tx_) + str(" ") + str(pul_) + str(" olib tashlandi!</b>"), "parse_mode": "html", "reply_markup": admin1_menu_}))
        currency_ = php_file_get_contents(str("foydalanuvchi/hisob/") + str(saved_) + str(".1.txt"))
        currency_ -= tx_
        file_put_contents(str("foydalanuvchi/hisob/") + str(saved_) + str(".1.txt"), currency_)
        buyurtmab_ = php_file_get_contents(str("foydalanuvchi/hisob/") + str(saved_) + str(".1txt"))
        buyurtmab_ -= tx_
        file_put_contents(str("foydalanuvchi/hisob/") + str(saved_) + str(".1txt"), buyurtmab_)
        unlink("tvalayir.txt")
        unlink("step/odam.txt")
    # end if
# end if
if tx_ == "ð³ Hamyonlar" and cid_ == admin_:
    kategoriya_ = php_file_get_contents("sozlamalar/hamyon/kategoriya.txt")
    more_ = php_explode("\n", kategoriya_)
    soni_ = php_substr_count(kategoriya_, "\n")
    keys_ = Array()
    for_ = 1
    while for_ <= soni_:
        
        title_ = php_str_replace("\n", "", more_[for_])
        keys_[-1] = Array({"text": str(title_) + str("- ni o'chirish"), "callback_data": str("delete-") + str(title_)})
        keysboard2_ = array_chunk(keys_, 1)
        keysboard2_[-1] = Array(Array({"text": "â Yangi to'lov tizimi qo'shish", "callback_data": "yangi_tolov"}))
        keysboard2_[-1] = Array(Array({"text": "ð Taklif narxi", "callback_data": "taklif_narxi"}), Array({"text": "ð¶ Valyuta nomi", "callback_data": "valyuta_nomi"}))
        key_ = php_json_encode(Array({"inline_keyboard": keysboard2_}))
        for_ += 1
    # end while
    if kategoriya_ != None:
        bot("sendMessage", Array({"chat_id": admin_, "text": "<b>Quyidagilardan birini tanlang:</b>", "parse_mode": "html", "reply_markup": key_}))
    else:
        bot("sendMessage", Array({"chat_id": admin_, "text": "<b>Quyidagilardan birini tanlang:</b>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "â Yangi to'lov tizimi qo'shish", "callback_data": "yangi_tolov"})), Array(Array({"text": "ð Taklif narxi", "callback_data": "taklif_narxi"}), Array({"text": "ð¶ Valyuta nomi", "callback_data": "valyuta_nomi"})))}))}))
    # end if
# end if
if php_mb_stripos(data_, "delete-") != False:
    ex_ = php_explode("-", data_)
    kat_ = ex_[1]
    royxat_ = php_file_get_contents("sozlamalar/hamyon/kategoriya.txt")
    k_ = php_str_replace("\n" + kat_ + "", "", royxat_)
    file_put_contents("sozlamalar/hamyon/kategoriya.txt", k_)
    deleteFolder(str("sozlamalar/hamyon/") + str(kat_))
    bot("deleteMessage", Array({"chat_id": ccid_, "message_id": cmid_}))
    bot("SendMessage", Array({"chat_id": ccid_, "text": "<b>To'lov tizimi o'chirildi!</b>", "parse_mode": "html"}))
# end if
if data_ == "yangi_tolov":
    bot("deleteMessage", Array({"chat_id": ccid_, "message_id": cmid_}))
    bot("SendMessage", Array({"chat_id": ccid_, "text": "<b>Yangi to'lov tizimi nomini yuboring:\n\nMasalan:</b> Click", "parse_mode": "html", "reply_markup": php_json_encode(Array({"resize_keyboard": True, "keyboard": Array(Array(Array({"text": "ð Boshqaruv"})))}))}))
    file_put_contents(str("step/") + str(ccid_) + str(".txt"), "tolov")
# end if
if userstep_ == "tolov":
    if tx_ == "ð Boshqaruv":
        unlink(str("step/") + str(cid_) + str(".txt"))
    else:
        if (php_isset(lambda : text_)):
            kategoriya2_ = php_file_get_contents("sozlamalar/hamyon/kategoriya.txt")
            file_put_contents("sozlamalar/hamyon/kategoriya.txt", str(kategoriya2_) + str("\n") + str(text_))
            mkdir(str("sozlamalar/hamyon/") + str(text_))
            bot("SendMessage", Array({"chat_id": cid_, "text": "<b>Ushbu to'lov tizimidagi hamyoningiz raqamini yuboring:</b>", "parse_mode": "html"}))
            file_put_contents(str("step/") + str(cid_) + str(".txt"), str("raqam-") + str(text_))
        else:
            bot("SendMessage", Array({"chat_id": cid_, "text": "<b>Yangi to'lov tizimi nomini yuboring:\n\nMasalan:</b> Click", "parse_mode": "html"}))
        # end if
    # end if
# end if
if php_mb_stripos(userstep_, "raqam-") != False:
    ex_ = php_explode("-", userstep_)
    kat_ = ex_[1]
    if tx_ == "ð Boshqaruv":
        unlink(str("step/") + str(cid_) + str(".txt"))
        unlink(str("sozlamalar/hamyon/") + str(kat_))
    else:
        if php_is_numeric(text_):
            file_put_contents(str("sozlamalar/hamyon/") + str(kat_) + str("/raqam.txt"), text_)
            bot("SendMessage", Array({"chat_id": cid_, "text": "<b>Yangi to'lov tizimi qo'shildi!</b>", "parse_mode": "html", "reply_markup": admin1_menu_}))
            unlink(str("step/") + str(cid_) + str(".txt"))
        else:
            bot("SendMessage", Array({"chat_id": cid_, "text": "<b>Ushbu to'lov tizimidagi hamyoningiz raqamini yuboring:</b>", "parse_mode": "html"}))
        # end if
    # end if
# end if
if tx_ == "ð Tugmalar" and cid_ == admin_:
    bot("sendMessage", Array({"chat_id": admin_, "text": "<b>ð Tugma sozlash bo'limidasiz tanlang:</b>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "ð¥ Asosiy menyudagi tugmalar", "callback_data": "asosiy_tugma"})), Array(Array({"text": "ðµ Pul ishlash bo'limi tugmalari", "callback_data": "pulishlash_tugma"})), Array(Array({"text": "â ï¸ O'z holiga qaytarish", "callback_data": "reset_tugma"})))}))}))
# end if
if data_ == "tugma_sozlash" and ccid_ == admin_:
    bot("deleteMessage", Array({"chat_id": admin_, "message_id": cmid_}))
    bot("sendMessage", Array({"chat_id": admin_, "text": "<b>ð Tugma sozlash bo'limidasiz tanlang:</b>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "ð¥ Asosiy menyudagi tugmalar", "callback_data": "asosiy_tugma"})), Array(Array({"text": "ðµ Pul ishlash bo'limi tugmalari", "callback_data": "pulishlash_tugma"})), Array(Array({"text": "â ï¸ O'z holiga qaytarish", "callback_data": "reset_tugma"})))}))}))
# end if
if data_ == "asosiy_tugma" and ccid_ == admin_:
    bot("editMessageText", Array({"chat_id": admin_, "message_id": cmid_, "text": "<b>Quyidagilardan birini tanlang:</b>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": str(tugma1_), "callback_data": "tg1"})), Array(Array({"text": str(tugma2_), "callback_data": "tg2"}), Array({"text": str(tugma3_), "callback_data": "tg3"})), Array(Array({"text": str(tugma4_), "callback_data": "tg4"})), Array(Array({"text": "âï¸ Orqaga", "callback_data": "tugma_sozlash"})))}))}))
# end if
tugma_ = php_file_get_contents("tugma.txt")
if data_ == "tg1" and ccid_ == admin_:
    bot("sendMessage", Array({"chat_id": admin_, "text": "<b>Tugma uchun yangi nom yuboring:</b>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"resize_keyboard": True, "keyboard": Array(Array(Array({"text": "ð Boshqaruv"})))}))}))
    file_put_contents("tugma.txt", "tg1")
# end if
if tugma_ == "tg1" and cid_ == admin_:
    if tx_ == "ð Boshqaruv":
        unlink("tugma.txt")
    else:
        file_put_contents("sozlamalar/tugma/tugma1.txt", str(tx_))
        bot("sendMessage", Array({"chat_id": admin_, "text": str("<b>Qabul qilindi!</b>\n\n<i>Tugma nomi</i> <b>") + str(tx_) + str("</b> <i>ga o'zgartirildi</i>"), "parse_mode": "html", "reply_markup": admin1_menu_}))
        unlink("tugma.txt")
    # end if
# end if
tugma_ = php_file_get_contents("tugma.txt")
if data_ == "tg2" and ccid_ == admin_:
    bot("sendMessage", Array({"chat_id": admin_, "text": "<b>Tugma uchun yangi nom yuboring:</b>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"resize_keyboard": True, "keyboard": Array(Array(Array({"text": "ð Boshqaruv"})))}))}))
    file_put_contents("tugma.txt", "tg2")
# end if
if tugma_ == "tg2" and cid_ == admin_:
    if tx_ == "ð Boshqaruv":
        unlink("tugma.txt")
    else:
        file_put_contents("sozlamalar/tugma/tugma2.txt", str(tx_))
        bot("sendMessage", Array({"chat_id": admin_, "text": str("<b>Qabul qilindi!</b>\n\n<i>Tugma nomi</i> <b>") + str(tx_) + str("</b> <i>ga o'zgartirildi</i>"), "parse_mode": "html", "reply_markup": admin1_menu_}))
        unlink("tugma.txt")
    # end if
# end if
tugma_ = php_file_get_contents("tugma.txt")
if data_ == "tg3" and ccid_ == admin_:
    bot("sendMessage", Array({"chat_id": admin_, "text": "<b>Tugma uchun yangi nom yuboring:</b>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"resize_keyboard": True, "keyboard": Array(Array(Array({"text": "ð Boshqaruv"})))}))}))
    file_put_contents("tugma.txt", "tg3")
# end if
if tugma_ == "tg3" and cid_ == admin_:
    if tx_ == "ð Boshqaruv":
        unlink("tugma.txt")
    else:
        file_put_contents("sozlamalar/tugma/tugma3.txt", str(tx_))
        bot("sendMessage", Array({"chat_id": admin_, "text": str("<b>Qabul qilindi!</b>\n\n<i>Tugma nomi</i> <b>") + str(tx_) + str("</b> <i>ga o'zgartirildi</i>"), "parse_mode": "html", "reply_markup": admin1_menu_}))
        unlink("tugma.txt")
    # end if
# end if
tugma_ = php_file_get_contents("tugma.txt")
if data_ == "tg4" and ccid_ == admin_:
    bot("sendMessage", Array({"chat_id": admin_, "text": "<b>Tugma uchun yangi nom yuboring:</b>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"resize_keyboard": True, "keyboard": Array(Array(Array({"text": "ð Boshqaruv"})))}))}))
    file_put_contents("tugma.txt", "tg4")
# end if
if tugma_ == "tg4" and cid_ == admin_:
    if tx_ == "ð Boshqaruv":
        unlink("tugma.txt")
    else:
        file_put_contents("sozlamalar/tugma/tugma4.txt", str(tx_))
        bot("sendMessage", Array({"chat_id": admin_, "text": str("<b>Qabul qilindi!</b>\n\n<i>Tugma nomi</i> <b>") + str(tx_) + str("</b> <i>ga o'zgartirildi</i>"), "parse_mode": "html", "reply_markup": admin1_menu_}))
        unlink("tugma.txt")
    # end if
# end if
if data_ == "pulishlash_tugma" and ccid_ == admin_:
    bot("editMessageText", Array({"chat_id": admin_, "message_id": cmid_, "text": "<b>Quyidagilardan birini tanlang:</b>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": str(tugma7_), "callback_data": "pultg2"})), Array(Array({"text": "âï¸ Orqaga", "callback_data": "tugma_sozlash"})))}))}))
# end if
tugma_ = php_file_get_contents("tugma.txt")
if data_ == "pultg1" and ccid_ == admin_:
    bot("sendMessage", Array({"chat_id": admin_, "text": "<b>Tugma uchun yangi nom yuboring:</b>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"resize_keyboard": True, "keyboard": Array(Array(Array({"text": "ð Boshqaruv"})))}))}))
    file_put_contents("tugma.txt", "pultg1")
# end if
if tugma_ == "pultg1" and cid_ == admin_:
    if tx_ == "ð Boshqaruv":
        unlink("tugma.txt")
    else:
        file_put_contents("sozlamalar/tugma/tugma6.txt", str(tx_))
        bot("sendMessage", Array({"chat_id": admin_, "text": str("<b>Qabul qilindi!</b>\n\n<i>Tugma nomi</i> <b>") + str(tx_) + str("</b> <i>ga o'zgartirildi</i>"), "parse_mode": "html", "reply_markup": admin1_menu_}))
        unlink("tugma.txt")
    # end if
# end if
tugma_ = php_file_get_contents("tugma.txt")
if data_ == "pultg2" and ccid_ == admin_:
    bot("sendMessage", Array({"chat_id": admin_, "text": "<b>Tugma uchun yangi nom yuboring:</b>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"resize_keyboard": True, "keyboard": Array(Array(Array({"text": "ð Boshqaruv"})))}))}))
    file_put_contents("tugma.txt", "pultg2")
# end if
if tugma_ == "pultg2" and cid_ == admin_:
    if tx_ == "ð Boshqaruv":
        unlink("tugma.txt")
    else:
        file_put_contents("sozlamalar/tugma/tugma7.txt", str(tx_))
        bot("sendMessage", Array({"chat_id": admin_, "text": str("<b>Qabul qilindi!</b>\n\n<i>Tugma nomi</i> <b>") + str(tx_) + str("</b> <i>ga o'zgartirildi</i>"), "parse_mode": "html", "reply_markup": admin1_menu_}))
        unlink("tugma.txt")
    # end if
# end if
if data_ == "reset_tugma" and ccid_ == admin_:
    bot("editMessageText", Array({"chat_id": admin_, "message_id": cmid_, "text": "<b>Tugma nomlari o'chirilmoqda...</b>", "parse_mode": "html"}))
    sleep(2)
    bot("deleteMessage", Array({"chat_id": admin_, "message_id": cmid_}))
    bot("sendMessage", Array({"chat_id": admin_, "text": "<b>Tugma nomlari o'chirilib, o'z holiga qaytarildi!</b>", "parse_mode": "html"}))
    unlink("sozlamalar/tugma/tugma1.txt")
    unlink("sozlamalar/tugma/tugma2.txt")
    unlink("sozlamalar/tugma/tugma3.txt")
    unlink("sozlamalar/tugma/tugma4.txt")
    unlink("sozlamalar/tugma/tugma5.txt")
    unlink("sozlamalar/tugma/tugma6.txt")
    unlink("sozlamalar/tugma/tugma7.txt")
# end if
admin6_menu_ = php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "ð Majburiy obuna", "callback_data": "majburiy_obuna"})))}))
if data_ == "kanalsoz" and ccid_ == admin_:
    bot("deleteMessage", Array({"chat_id": admin_, "message_id": cmid_}))
    bot("sendMessage", Array({"chat_id": admin_, "text": "<b>Quyidagilardan birini tanlang:</b>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "ð Majburiy obuna", "callback_data": "majburiy_obuna"})))}))}))
    unlink(str("step/") + str(ccid_) + str(".txt"))
# end if
if tx_ == "ð Statistika" and cid_ == admin_:
    lichka_ = php_file_get_contents("statistika/obunachi.txt")
    lich_ = php_substr_count(lichka_, "\n")
    load_ = sys_getloadavg()
    bot("sendMessage", Array({"chat_id": admin_, "text": str("<b>ð¡ O'rtacha yuklanish:</b> <code>") + str(load_[0]) + str("</code>\n\nð <b>Aktiv botlar: ") + str(aktivbot_) + str(" ta</b>\nð <b>Yaratilgan botlar: ") + str(hammabot_) + str(" ta</b>\nð¥ <b>Foydalanuvchilar: ") + str(lich_) + str(" ta</b>"), "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "ð Yangilash", "callback_data": "stats"})), Array(Array({"text": "ð Hisoblar", "callback_data": "hisob"}), Array({"text": "ð Do'stlar", "callback_data": "dostlar"})))}))}))
# end if
if data_ == "hisob" and ccid_ == admin_:
    bot("deleteMessage", Array({"chat_id": admin_, "message_id": cmid_}))
    hisoblar_ = hisob()
    bot("sendMessage", Array({"chat_id": admin_, "text": str(hisoblar_), "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "âï¸ Orqaga", "callback_data": "stats"})))}))}))
# end if
if data_ == "dostlar" and ccid_ == admin_:
    bot("deleteMessage", Array({"chat_id": admin_, "message_id": cmid_}))
    dostlar_ = dostlar()
    bot("sendMessage", Array({"chat_id": admin_, "text": str(dostlar_), "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "âï¸ Orqaga", "callback_data": "stats"})))}))}))
# end if
if data_ == "stats" and ccid_ == admin_:
    lichka_ = php_file_get_contents("statistika/obunachi.txt")
    lich_ = php_substr_count(lichka_, "\n")
    load_ = sys_getloadavg()
    bot("deleteMessage", Array({"chat_id": admin_, "message_id": cmid_}))
    bot("sendMessage", Array({"chat_id": admin_, "text": str("<b>ð¡ O'rtacha yuklanish:</b> <code>") + str(load_[0]) + str("</code>\n\nð <b>Aktiv botlar: ") + str(aktivbot_) + str(" ta</b>\nð <b>Yaratilgan botlar: ") + str(hammabot_) + str(" ta</b>\nð¥ <b>Foydalanuvchilar: ") + str(lich_) + str(" ta</b>"), "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "ð Yangilash", "callback_data": "stats"})), Array(Array({"text": "ð Hisoblar", "callback_data": "hisob"}), Array({"text": "ð Do'stlar", "callback_data": "dostlar"})))}))}))
# end if
if tx_ == "ð¢ Kanallar" and cid_ == admin_:
    bot("sendMessage", Array({"chat_id": admin_, "text": "<b>Quyidagilardan birini tanlang:</b>", "parse_mode": "html", "reply_markup": admin6_menu_}))
# end if
if data_ == "majburiy_obuna" and ccid_ == admin_:
    bot("editMessageText", Array({"chat_id": admin_, "message_id": cmid_, "text": "<b>Majburiy obunalarni sozlash bo'limidasiz:</b>\n\n<i>Avval <b>asosiy kanal</b>ni ulab keyin kanal qo'shing!</i>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "ð Ro'yxatni ko'rish", "callback_data": "majburiy_obuna3"})), Array(Array({"text": "ð¢ Asosiy kanal", "callback_data": "majburiy_obuna4"}), Array({"text": "â Kanal qo'shish", "callback_data": "majburiy_obuna1"})), Array(Array({"text": "ð O'chirish", "callback_data": "majburiy_obuna2"}), Array({"text": "âï¸ Orqaga", "callback_data": "kanalsoz"})))}))}))
    unlink(str("step/") + str(cid_) + str(".txt"))
# end if
majburiy_ = php_file_get_contents("maj.txt")
if data_ == "majburiy_obuna1" and ccid_ == admin_:
    bot("sendMessage", Array({"chat_id": admin_, "text": "<b>ð¢ Kerakli kanalni manzilini yuboring:</b>\n\nNamuna: <code>@MAKERNEWX</code>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"resize_keyboard": True, "keyboard": Array(Array(Array({"text": "ð Boshqaruv"})))}))}))
    file_put_contents("maj.txt", "majburiy1")
# end if
if majburiy_ == "majburiy1" and cid_ == admin_:
    if tx_ == "ð Boshqaruv":
        unlink("maj.txt")
    else:
        if (php_isset(lambda : message_)):
            kanal_ = php_file_get_contents("sozlamalar/kanal/ch.txt")
            if php_mb_stripos(kanal_, tx_) == False:
                file_put_contents("sozlamalar/kanal/ch.txt", str(kanal_) + str("\n") + str(tx_))
                bot("sendMessage", Array({"chat_id": admin_, "text": str("<b>") + str(tx_) + str(" qabul qilindi!</b>\n\nâ ï¸ @") + str(botname_) + str(" ni kanalingizga admin qiling!"), "parse_mode": "html", "reply_markup": admin1_menu_}))
            # end if
        # end if
        unlink("maj.txt")
    # end if
# end if
majburiy_ = php_file_get_contents("maj.txt")
if data_ == "majburiy_obuna4" and ccid_ == admin_:
    bot("sendMessage", Array({"chat_id": admin_, "text": "<b>ð¢ Kerakli kanalni manzilini yuboring:</b>\n\nNamuna: <code>@MAKERNEWX</code>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"resize_keyboard": True, "keyboard": Array(Array(Array({"text": "ð Boshqaruv"})))}))}))
    file_put_contents("maj.txt", "majburiy4")
# end if
if majburiy_ == "majburiy4" and cid_ == admin_:
    if tx_ == "ð Boshqaruv":
        unlink("maj.txt")
    else:
        deleteFolder("sozlamalar/kanal/ch.txt")
        bot("sendMessage", Array({"chat_id": admin_, "text": str("<b>") + str(tx_) + str(" qabul qilindi!</b>\n\nâ ï¸ @") + str(botname_) + str(" ni kanalingizga admin qiling!"), "parse_mode": "html", "reply_markup": admin1_menu_}))
        file_put_contents("sozlamalar/kanal/ch.txt", str(text_))
        unlink("maj.txt")
    # end if
# end if
majburiyoc_ = php_file_get_contents("majoch.txt")
if data_ == "majburiy_obuna2" and ccid_ == admin_:
    bot("sendMessage", Array({"chat_id": admin_, "text": "<b>ð O'chiriladigan kanal manzilini yuboring:</b>\n\nNamuna: <code>@MAKERNEWX</code>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"resize_keyboard": True, "keyboard": Array(Array(Array({"text": "ð Boshqaruv"})))}))}))
    file_put_contents("majoch.txt", "majoch")
# end if
if majburiyoc_ == "majoch" and cid_ == admin_:
    if tx_ == "ð Boshqaruv":
        unlink("majoch.txt")
    else:
        bot("sendMessage", Array({"chat_id": admin_, "text": str("<b>ð ") + str(tx_) + str(" ni o'chirish yakunlandi</b>"), "parse_mode": "html", "reply_markup": admin1_menu_}))
        kanal_ = php_file_get_contents("sozlamalar/kanal/ch.txt")
        if php_mb_stripos(kanal_, tx_) != False:
            ochir_ = php_str_replace("\n" + tx_ + "", "", kanal_)
            file_put_contents("sozlamalar/kanal/ch.txt", ochir_)
            unlink("majoch.txt")
        # end if
    # end if
# end if
if data_ == "majburiy_obuna3" and ccid_ == admin_:
    if kanallar_ == None:
        bot("editMessageText", Array({"chat_id": admin_, "message_id": cmid_, "text": "<b>Kanallar ulanmagan!</b>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "âï¸ Orqaga", "callback_data": "majburiy_obuna"})))}))}))
    else:
        opshi_ = php_substr_count(kanallar_, "\n")
        bot("editMessageText", Array({"chat_id": admin_, "message_id": cmid_, "text": str("""<b>Ulangan kanallar ro'yxati â¤µï¸</b>\nââââââââ\n\n<b>Asosiy kanal:</b> <i>""") + str(kanallar_) + str("</i>\n"), "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "âï¸ Orqaga", "callback_data": "majburiy_obuna"})))}))}))
    # end if
# end if
if tx_ == "/panel":
    if cid_ == admin_:
        bot("sendMessage", Array({"chat_id": admin_, "text": "<b>ð Boshqaruv paneliga xush kelibsiz!</b>", "parse_mode": "html", "reply_markup": admin1_menu_}))
    else:
        bot("sendMessage", Array({"chat_id": cid_, "text": "<b>ð¥ Asosiy menyudasiz</b>", "parse_mode": "html"}))
    # end if
# end if
if (php_isset(lambda : message_)):
    get_ = php_file_get_contents("statistika/obunachi.txt")
    if php_mb_stripos(get_, fid_) == False:
        file_put_contents("statistika/obunachi.txt", str(get_) + str("\n") + str(fid_))
        bot("sendMessage", Array({"chat_id": admin_, "text": str("<b>ð¤ Yangi aÊ¼zo\nâï¸ Lichka:</b> <a href='tg://user?id=") + str(fid_) + str("'>") + str(name_) + str("</a>"), "parse_mode": "html"}))
    # end if
# end if
if text_ == "/start":
    if cid_ != admin_:
        bot("sendmessage", Array({"chat_id": cid_, "text": "<b>ð¥ Asosiy menyudasiz</b>", "parse_mode": "html", "reply_markup": main_menu_}))
    else:
        bot("SendMessage", Array({"chat_id": admin_, "text": "<b>ð¥ Asosiy menyudasiz</b>", "parse_mode": "html", "reply_markup": main_menuad_}))
    # end if
# end if
if tx_ == str(tugma1_) and joinchat(fid_) == "true":
    bot("sendMessage", Array({"chat_id": cid_, "text": "<b>ð¤ Botlarni boshqarish bo'limiga xush kelibsiz!</b>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"resize_keyboard": True, "keyboard": Array(Array(Array({"text": "â Yangi bot ochish"})), Array(Array({"text": "âï¸ Botni sozlash"}), Array({"text": "ðµ To'lov qilish"})), Array(Array({"text": "ð Buyurtmalar"}), Array({"text": "ð Orqaga"})))}))}))
# end if
if tx_ == "ð Buyurtmalar" and joinchat(fid_) == "true":
    bot("sendMessage", Array({"chat_id": cid_, "text": "<b>ð Quyidagilardan birini tanlang:</b>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "â Yangi buyurtma", url: str("tg://user?id=") + str(admin_)})), Array(Array({"text": "ð Mening buyurtmam", "callback_data": "buyurtma_royxat"})))}))}))
# end if
if data_ == "buyurtmalar" and joinchat(ccid_) == "true":
    bot("deleteMessage", Array({"chat_id": ccid_, "message_id": cmid_}))
    bot("sendMessage", Array({"chat_id": ccid_, "text": "<b>ð Quyidagilardan birini tanlang:</b>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "â Yangi buyurtma", url: str("tg://user?id=") + str(admin_)})), Array(Array({"text": "ð Mening buyurtmam", "callback_data": "buyurtma_royxat"})))}))}))
# end if
if data_ == "buyurtma_royxat" and joinchat(ccid_) == "true":
    bot("editMessageText", Array({"chat_id": ccid_, "message_id": cmid_, "text": "â± <b>Yuklanmoqda...</b>", "parse_mode": "html"}))
    bot("editMessageText", Array({"chat_id": ccid_, "message_id": cmid_ + 1, "text": "â± <b>Yuklanmoqda...</b>", "parse_mode": "html"}))
    bot("editmessagetext", Array({"chat_id": ccid_, "message_id": cmid_, "text": "<b>ð Buyurtma mavjud emas!</b>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "âï¸ Orqaga", "callback_data": "buyurtmalar"})))}))}))
# end if
board2_ = php_file_get_contents(str("foydalanuvchi/bot/") + str(cid_) + str("/bots.txt"))
more2_ = php_explode("\n", board2_)
soni2_ = php_substr_count(board2_, "\n")
key2_ = Array()
for2_ = 1
while for2_ <= soni2_:
    
    title2_ = php_str_replace("\n", "", more2_[for2_])
    key2_[-1] = Array({"text": str("ðµ ") + str(title2_), "callback_data": str("botpay_") + str(title2_)})
    key2board2_ = array_chunk(key2_, 1)
    keyboard2_ = php_json_encode(Array({"inline_keyboard": key2board2_}))
    for2_ += 1
# end while
if tx_ == "ðµ To'lov qilish" and joinchat(fid_) == "true":
    botsss_ = php_file_get_contents(str("foydalanuvchi/bot/") + str(cid_) + str("/bots.txt"))
    if botsss_:
        bot("sendMessage", Array({"chat_id": cid_, "text": "<b>ð Quyidagilardan birini tanlang:</b>", "parse_mode": "html", "reply_markup": keyboard2_}))
    else:
        bot("sendMessage", Array({"chat_id": cid_, "text": "<b>ð Sizda hech qanday bot yo'q</b>", "parse_mode": "html"}))
    # end if
# end if
if php_mb_stripos(data_, "orqa_") != False:
    ex_ = php_explode("orqa_", data_)[1]
    bot("editmessagetext", Array({"chat_id": ccid_, "message_id": cmid_, "text": "<b>ð Quyidagilardan birini tanlang:</b>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": str("ðµ ") + str(ex_), "callback_data": str("botpay_") + str(ex_)})))}))}))
# end if
if php_mb_stripos(data_, "botpay_") != False:
    ex_ = php_explode("botpay_", data_)[1]
    turi_ = php_file_get_contents(str("foydalanuvchi/bot/") + str(ccid_) + str("/turi.txt"))
    if turi_ == "ObunachiBot":
        bot("editmessagetext", Array({"chat_id": ccid_, "message_id": cmid_, "text": str("<b>ð Necha kunlik to'lovni amalga oshirmoqchisiz?</b>\n\n<i>1 kunlik to'lov - 200 ") + str(pul_) + str("\n3 kunlik to'lov - 600 ") + str(pul_) + str("\n7 kunlik to'lov - 1400 ") + str(pul_) + str("\n15 kunlik to'lov - 3000 ") + str(pul_) + str("\n30 kunlik to'lov - 6000 ") + str(pul_) + str("</i>"), "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "ð To'lov holati", "callback_data": "holati"})), Array(Array({"text": "1", "callback_data": str("dataPay=1=200=") + str(ex_)}), Array({"text": "3", "callback_data": str("dataPay=3=600=") + str(ex_)}), Array({"text": "7", "callback_data": str("dataPay=7=1400=") + str(ex_)}), Array({"text": "15", "callback_data": str("dataPay=15=3000=") + str(ex_)}), Array({"text": "30", "callback_data": str("dataPay=30=6000=") + str(ex_)})), Array(Array({"text": "âï¸ Orqaga", "callback_data": str("botpay_") + str(ex_)})))}))}))
    # end if
    if turi_ == "ViPObunachiBot":
        bot("editmessagetext", Array({"chat_id": ccid_, "message_id": cmid_, "text": str("<b>ð Necha kunlik to'lovni amalga oshirmoqchisiz?</b>\n\n<i>1 kunlik to'lov - 200 ") + str(pul_) + str("\n3 kunlik to'lov - 600 ") + str(pul_) + str("\n7 kunlik to'lov - 1400 ") + str(pul_) + str("\n15 kunlik to'lov - 3000 ") + str(pul_) + str("\n30 kunlik to'lov - 6000 ") + str(pul_) + str("</i>"), "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "ð To'lov holati", "callback_data": "holati"})), Array(Array({"text": "1", "callback_data": str("dataPay=1=200=") + str(ex_)}), Array({"text": "3", "callback_data": str("dataPay=3=600=") + str(ex_)}), Array({"text": "7", "callback_data": str("dataPay=7=1400=") + str(ex_)}), Array({"text": "15", "callback_data": str("dataPay=15=3000=") + str(ex_)}), Array({"text": "30", "callback_data": str("dataPay=30=6000=") + str(ex_)})), Array(Array({"text": "âï¸ Orqaga", "callback_data": str("orqa_") + str(ex_)})))}))}))
    # end if
# end if
if php_mb_stripos(data_, "dataPay=") != False:
    kun_ = php_explode("=", data_)[1]
    narx_ = php_explode("=", data_)[2]
    ex_ = php_explode("=", data_)[3]
    p_ = php_file_get_contents(str("foydalanuvchi/hisob/") + str(ccid_) + str(".txt"))
    if p_ >= narx_:
        bot("editMessageText", Array({"chat_id": ccid_, "message_id": cmid_, "text": str("<b>â Botingiz uchun ") + str(kun_) + str(" kunlik to'lov to'landi!</b>\n\n<i>Hisobingizdan ") + str(narx_) + str(" ") + str(pul_) + str(" olib tashlandi</i>"), "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "âï¸ Orqaga", "callback_data": str("botpay_") + str(ex_)})))}))}))
        file_put_contents(str("foydalanuvchi/hisob/") + str(ccid_) + str(".txt"), p_ - narx_)
        php_date_default_timezone_set("Asia/Tashkent")
        t_ = date("d")
        files_ = php_json_decode(php_file_get_contents(str("foydalanuvchi/bot/") + str(ccid_) + str("/kunlik.tolov")))
        d_["kun"] = files_.kun + kun_
        d_["sana"] = t_
        d_["puli"] = files_.puli + narx_
        file_put_contents(str("foydalanuvchi/bot/") + str(ccid_) + str("/kunlik.tolov"), php_json_encode(d_))
    else:
        bot("answerCallbackQuery", Array({"callback_query_id": callid_, "text": "ð Kechirasiz, hisobingizda yetarli mablag' mavjud emas!", "show_alert": True}))
    # end if
# end if
if data_ == "holati":
    txolat_ = php_json_decode(php_file_get_contents(str("foydalanuvchi/bot/") + str(ccid_) + str("/kunlik.tolov")))
    bot("answerCallbackQuery", Array({"callback_query_id": callid_, "text": "â³ Qolgan kunlar: " + txolat_.kun + " kun", "show_alert": True}))
# end if
php_date_default_timezone_set("Asia/Tashkent")
t_ = date("d")
glob_ = glob("foydalanuvchi/bot/*/turi.txt")
for globa_ in glob_:
    ids_ = php_str_replace(Array("foydalanuvchi/bot/", "/turi.txt"), Array("", ""), globa_)
    f_ = php_file_get_contents(str("foydalanuvchi/bot/") + str(ids_) + str("/turi.txt"))
    files_ = php_json_decode(php_file_get_contents(str("foydalanuvchi/bot/") + str(ids_) + str("/kunlik.tolov")))
    print(files_.kun)
    if f_ == "ObunachiBot":
        if files_.sana != t_:
            d_["puli"] = files_.puli - 200
            d_["sana"] = t_
            d_["kun"] = files_.kun - 1
            file_put_contents(str("foydalanuvchi/bot/") + str(ids_) + str("/kunlik.tolov"), php_json_encode(d_))
        # end if
        if files_.kun == 0 or files_.kun <= 0:
            bot("sendMessage", Array({"chat_id": ids_, "text": "<b>Sizning botingiz uyqu rejimga o'tkazildi</b>", "parse_mode": "html"}))
            file_put_contents(str("https://api.telegram.org/bot") + str(t_) + str("/deletewebhook?url=https://") + PHP_SERVER["SERVER_NAME"] + str("/Nakmak/foydalanuvchi/bot/") + str(ids_) + str("/") + str(f_) + str(".php"))
            if files_.puli >= 200:
                php_date_default_timezone_set("Asia/Tashkent")
                t_ = date("d")
                d_["sana"] = t_
                f_ = files_.puli - 200
                d_["puli"] = f_
                d_["kun"] = files_.kun - 1
                file_put_contents(str("foydalanuvchi/bot/") + str(ids_) + str("/kunlik.tolov"), php_json_encode(d_))
            else:
                file_put_contents(str("https://api.telegram.org/bot") + str(t_) + str("/deletewebhook?url=https://") + PHP_SERVER["SERVER_NAME"] + str("/Nakmak/foydalanuvchi/bot/") + str(ids_) + str("/") + str(f_) + str(".php"))
            # end if
        # end if
    # end if
    if f_ == "ViPObunachiBot":
        if files_.sana != t_:
            d_["puli"] = files_.puli - 200
            d_["sana"] = t_
            d_["kun"] = files_.kun - 1
            file_put_contents(str("foydalanuvchi/bot/") + str(ids_) + str("/kunlik.tolov"), php_json_encode(d_))
        # end if
        if files_.kun == 0 or files_.kun <= 0:
            bot("sendMessage", Array({"chat_id": ids_, "text": "<b>Sizning botingiz uyqu rejimga o'tkazildi</b>", "parse_mode": "html"}))
            file_put_contents(str("https://api.telegram.org/bot") + str(t_) + str("/deletewebhook?url=https://") + PHP_SERVER["SERVER_NAME"] + str("/Nakmak/foydalanuvchi/bot/") + str(ids_) + str("/") + str(f_) + str(".php"))
            if files_.puli >= 200:
                php_date_default_timezone_set("Asia/Tashkent")
                t_ = date("d")
                d_["sana"] = t_
                f_ = files_.puli - 200
                d_["puli"] = f_
                d_["kun"] = files_.kun - 1
                file_put_contents(str("foydalanuvchi/bot/") + str(ids_) + str("/kunlik.tolov"), php_json_encode(d_))
            else:
                file_put_contents(str("https://api.telegram.org/bot") + str(t_) + str("/deletewebhook?url=https://") + PHP_SERVER["SERVER_NAME"] + str("/Nakmak/foydalanuvchi/bot/") + str(ids_) + str("/") + str(f_) + str(".php"))
            # end if
        # end if
    # end if
# end for
board_ = php_file_get_contents(str("foydalanuvchi/bot/") + str(cid_) + str("/bots.txt"))
more_ = php_explode("\n", board_)
soni_ = php_substr_count(board_, "\n")
key_ = Array()
for_ = 1
while for_ <= soni_:
    
    title_ = php_str_replace("\n", "", more_[for_])
    key_[-1] = Array({"text": str("ï¸ð¤ ") + str(title_), "callback_data": str("set_") + str(title_)})
    keyboard2_ = array_chunk(key_, 2)
    keyboard_ = php_json_encode(Array({"inline_keyboard": keyboard2_}))
    for_ += 1
# end while
if tx_ == "âï¸ Botni sozlash" and joinchat(fid_) == "true":
    botsss_ = php_file_get_contents(str("foydalanuvchi/bot/") + str(cid_) + str("/bots.txt"))
    if botsss_:
        bot("sendMessage", Array({"chat_id": cid_, "text": "<b>ð Quyidagilardan birini tanlang:</b>", "parse_mode": "html", "reply_markup": keyboard_}))
    else:
        bot("sendMessage", Array({"chat_id": cid_, "text": "<b>ð Sizda hech qanday bot yo'q</b>", "parse_mode": "html"}))
    # end if
# end if
backboard_ = php_file_get_contents(str("foydalanuvchi/bot/") + str(ccid_) + str("/bots.txt"))
backmore_ = php_explode("\n", backboard_)
backsoni_ = php_substr_count(backboard_, "\n")
backkey_ = Array()
backfor_ = 1
while backfor_ <= backsoni_:
    
    title_ = php_str_replace("\n", "", backmore_[backfor_])
    backkey_[-1] = Array({"text": str("ï¸ð¤ ") + str(title_), "callback_data": str("set_") + str(title_)})
    backkeyboard2_ = array_chunk(backkey_, 2)
    backkeyboard_ = php_json_encode(Array({"inline_keyboard": backkeyboard2_}))
    backfor_ += 1
# end while
if php_mb_stripos(data_, "back_") != False:
    ex_ = php_explode("back_", data_)[1]
    botsss_ = php_file_get_contents(str("foydalanuvchi/bot/") + str(ccid_) + str("/bots.txt"))
    if botsss_:
        bot("deleteMessage", Array({"chat_id": ccid_, "message_id": cmid_}))
        bot("sendMessage", Array({"chat_id": ccid_, "text": "<b>ð Quyidagilardan birini tanlang:</b>", "parse_mode": "html", "reply_markup": backkeyboard_}))
    else:
        bot("deleteMessage", Array({"chat_id": ccid_, "message_id": cmid_}))
        bot("sendMessage", Array({"chat_id": ccid_, "text": "<b>ð Sizda hech qanday bot yo'q</b>", "parse_mode": "html"}))
    # end if
# end if
if php_mb_stripos(data_, "set_") != False:
    ex_ = php_explode("set_", data_)[1]
    token_ = php_file_get_contents(str("foydalanuvchi/bot/") + str(ccid_) + str("/token.txt"))
    turi_ = php_file_get_contents(str("foydalanuvchi/bot/") + str(ccid_) + str("/turi.txt"))
    kunida_ = php_file_get_contents(str("foydalanuvchi/bot/") + str(ccid_) + str("/kunida.txt"))
    soatida_ = php_file_get_contents(str("foydalanuvchi/bot/") + str(ccid_) + str("/soat.txt"))
    bot("editmessagetext", Array({"chat_id": ccid_, "message_id": cmid_, "text": str("<b>â @") + str(ex_) + str(" tanlandi!</b> \n \n<b><i>ð Bot tokeni:</i></b> <code>") + str(token_) + str("</code> \n<b><i>ð Bot ochilgan vaqt:</i></b> ") + str(kunida_) + str(" | ") + str(soatida_) + str(" \n<b><i>ð Bot turi:</i></b> <i>") + str(turi_) + str("</i> \n \n<b><i> ð½ Quyidagi tugmalar yordamida botingizni sozlashingiz mumkin:</i></b>"), "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "ð Tokenni almashtirish", "callback_data": str("token_") + str(ex_)})), Array(Array({"text": "ð Yangilash", "callback_data": str("up_") + str(ex_)}), Array({"text": "ð O'chirish", "callback_data": str("del_") + str(ex_)})), Array(Array({"text": "âï¸ Orqaga", "callback_data": str("back_") + str(ex_)})))}))}))
# end if
if php_mb_stripos(data_, "kesh_") != False:
    ex_ = php_explode("kesh_", data_)[1]
    bot("editMessageText", Array({"chat_id": ccid_, "message_id": cmid_, "text": "â± <b>Tozalanmoqda...</b>", "parse_mode": "html"}))
    bot("editMessageText", Array({"chat_id": ccid_, "message_id": cmid_ + 1, "text": "â± <b>Tozalanmoqda...</b>", "parse_mode": "html"}))
    bot("editMessageText", Array({"chat_id": ccid_, "message_id": cmid_ + 2, "text": "â± <b>Tozalanmoqda...</b>", "parse_mode": "html"}))
    bot("editMessageText", Array({"chat_id": ccid_, "message_id": cmid_ + 3, "text": "â± <b>Tozalanmoqda...</b>", "parse_mode": "html"}))
    bot("editmessagetext", Array({"chat_id": ccid_, "message_id": cmid_, "text": "<b>ð¡ Kesh fayllar muvaffaqiyatli tozalandi</b>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "âï¸ Orqaga", "callback_data": str("plus_") + str(ex_)})))}))}))
# end if
if php_mb_stripos(data_, "del_") != False:
    ex_ = php_explode("del_", data_)[1]
    bot("editmessagetext", Array({"chat_id": ccid_, "message_id": cmid_, "text": str("<b>â ï¸ @") + str(ex_) + str(" ni o'chirib yuborishga ishonchingiz komilmi?</b>"), "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "ð O'chirish", "callback_data": str("dels_") + str(ex_)})), Array(Array({"text": "âï¸ Orqaga", "callback_data": str("set_") + str(ex_)})))}))}))
# end if
if php_mb_stripos(data_, "dels_") != False:
    ex_ = php_explode("dels_", data_)[1]
    turi_ = php_file_get_contents(str("foydalanuvchi/bot/") + str(ccid_) + str("/") + str(ex_) + str("/turi.txt"))
    bot("deleteMessage", Array({"chat_id": ccid_, "message_id": cmid_}))
    bot("sendMessage", Array({"chat_id": ccid_, "text": str("<b>ð @") + str(ex_) + str(" ni o'chirish yakunlandi</b>"), "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "âï¸ Orqaga", "callback_data": str("back_") + str(ex_)})))}))}))
    aktivbot_ = php_file_get_contents("statistika/aktivbot.txt")
    aktivbot_ -= 1
    file_put_contents("statistika/aktivbot.txt", aktivbot_)
    deleteFolder(str("foydalanuvchi/bot/") + str(ccid_))
    bots2_ = php_file_get_contents(str("foydalanuvchi/bot/") + str(ccid_) + str("/bots.txt"))
    unlink(str("foydalanuvchi/bot/") + str(ccid_) + str("/turi.txt"))
    unlink(str("foydalanuvchi/bot/") + str(ccid_) + str("/user.json"))
    if php_mb_stripos(bots2_, ex_) != False:
        ex1_ = php_str_replace("\n" + ex_ + "", "", bots2_)
        file_put_contents(str("foydalanuvchi/bot/") + str(ccid_) + str("/bots.txt"), ex1_)
    # end if
# end if
if php_mb_stripos(data_, "up_") != False:
    ex_ = php_explode("up_", data_)[1]
    turi_ = php_file_get_contents(str("foydalanuvchi/bot/") + str(ccid_) + str("/turi.txt"))
    tokeni_ = php_file_get_contents(str("foydalanuvchi/bot/") + str(ccid_) + str("/token.txt"))
    kod_ = php_file_get_contents(str("botlar/") + str(turi_) + str(".php"))
    kod_ = php_str_replace("API_TOKEN", str(tokeni_), kod_)
    kod_ = php_str_replace("ADMIN_ID", str(ccid_), kod_)
    file_put_contents(str("foydalanuvchi/bot/") + str(ccid_) + str("/") + str(turi_) + str(".php"), str(kod_))
    file_put_contents(str("foydalanuvchi/bot/") + str(ccid_) + str("/botholat.txt"), "activ")
    get_ = php_json_decode(php_file_get_contents(str("https://api.telegram.org/bot") + str(tokeni_) + str("/setwebhook?url=https://") + PHP_SERVER["SERVER_NAME"] + str("/Nakmak/foydalanuvchi/bot/") + str(ccid_) + str("/") + str(turi_) + str(".php"))).result
    if get_:
        bot("editMessageText", Array({"chat_id": ccid_, "message_id": cmid_, "text": "â± <b>Yangilanmoqda...</b>", "parse_mode": "html"}))
        bot("editMessageText", Array({"chat_id": ccid_, "message_id": cmid_ + 1, "text": "â± <b>Yangilanmoqda...</b>", "parse_mode": "html"}))
        bot("editMessageText", Array({"chat_id": ccid_, "message_id": cmid_ + 2, "text": "â± <b>Yangilanmoqda...</b>", "parse_mode": "html"}))
        bot("editMessageText", Array({"chat_id": ccid_, "message_id": cmid_ + 3, "text": "â± <b>Yangilanmoqda...</b>", "parse_mode": "html"}))
        bot("editmessagetext", Array({"chat_id": ccid_, "message_id": cmid_, "text": "<b>ð Botingiz muvaffaqiyatli yangilandi</b>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "â¡ï¸ Botga o'tish", "url": str("https://t.me/") + str(ex_)})), Array(Array({"text": "âï¸ Orqaga", "callback_data": str("set_") + str(ex_)})))}))}))
    # end if
# end if
if text_ == "â Yangi bot ochish" and joinchat(cid_) == True:
    kategoriya_ = php_file_get_contents("sozlamalar/bot/kategoriya.txt")
    more_ = php_explode("\n", kategoriya_)
    soni_ = php_substr_count(kategoriya_, "\n")
    key_ = Array()
    for_ = 1
    while for_ <= soni_:
        
        title_ = php_str_replace("\n", "", more_[for_])
        key_[-1] = Array({"text": str(title_), "callback_data": str("bolim-") + str(title_)})
        keyboard2_ = array_chunk(key_, 2)
        bolim_ = php_json_encode(Array({"inline_keyboard": keyboard2_}))
        for_ += 1
    # end while
    if kategoriya_ == None:
        bot("SendMessage", Array({"chat_id": cid_, "text": "<b>â ï¸ Kategoriyalar mavjud emas!</b>", "parse_mode": "html"}))
        sys.exit(0)
    else:
        bot("SendMessage", Array({"chat_id": cid_, "text": "ð <b>Quyidagi boâlimlardan birini tanlang:</b>", "parse_mode": "html", "reply_markup": bolim_}))
        sys.exit(0)
    # end if
# end if
if data_ == "orqaga" and joinchat(ccid_) == "true":
    more_ = php_explode("\n", kategoriya_)
    soni_ = php_substr_count(kategoriya_, "\n")
    key_ = Array()
    for_ = 1
    while for_ <= soni_:
        
        title_ = php_str_replace("\n", "", more_[for_])
        key_[-1] = Array({"text": str(title_), "callback_data": str("bolim-") + str(title_)})
        keyboard2_ = array_chunk(key_, 2)
        bolim_ = php_json_encode(Array({"inline_keyboard": keyboard2_}))
        for_ += 1
    # end while
    bot("deleteMessage", Array({"chat_id": ccid_, "message_id": cmid_}))
    bot("sendMessage", Array({"chat_id": ccid_, "text": "ð <b>Quyidagi boâlimlardan birini tanlang:</b>", "parse_mode": "html", "reply_markup": bolim_}))
    sys.exit(0)
# end if
if php_mb_stripos(data_, "bolim-") != False:
    ex_ = php_explode("-", data_)
    kat_ = ex_[1]
    royxat_ = php_file_get_contents(str("sozlamalar/bot/") + str(kat_) + str("/royxat.txt"))
    kategoriya_ = php_file_get_contents("sozlamalar/bot/kategoriya.txt")
    more_ = php_explode("\n", royxat_)
    soni_ = php_substr_count(royxat_, "\n")
    keys_ = Array()
    for_ = 1
    while for_ <= soni_:
        
        title_ = php_str_replace("\n", "", more_[for_])
        keys_[-1] = Array({"text": str("ð¤ ") + str(title_), "callback_data": str("botyarat-") + str(title_) + str("-") + str(kat_)})
        keysboard2_ = array_chunk(keys_, 1)
        keysboard2_[-1] = Array(Array({"text": "âï¸ Orqaga", "callback_data": "orqaga"}))
        key_ = php_json_encode(Array({"inline_keyboard": keysboard2_}))
        for_ += 1
    # end while
    if royxat_ != None:
        bot("editMessageText", Array({"chat_id": ccid_, "message_id": cmid_, "text": "ð¤ <b>Quyidagi botlardan birini tanlang:</b>", "parse_mode": "html", "reply_markup": key_}))
    else:
        bot("answerCallbackQuery", Array({"callback_query_id": callid_, "text": "ð« Botlar mavjud emas!", "show_alert": True}))
    # end if
# end if
if php_mb_stripos(data_, "botyarat-") != False:
    bots_ = php_file_get_contents(str("foydalanuvchi/bot/") + str(cid_) + str("/bots.txt"))
    ex_ = php_explode("-", data_)
    royxat_ = ex_[1]
    kategoriya_ = ex_[2]
    type_ = php_file_get_contents(str("sozlamalar/bot/") + str(kategoriya_) + str("/") + str(royxat_) + str("/turi.txt"))
    narx_ = php_file_get_contents(str("sozlamalar/bot/") + str(kategoriya_) + str("/") + str(royxat_) + str("/narx.txt"))
    tavsif_ = php_file_get_contents(str("sozlamalar/bot/") + str(kategoriya_) + str("/") + str(royxat_) + str("/tavsif.txt"))
    if bots_:
        bot("editMessageText", Array({"chat_id": ccid_, "message_id": cmid_, "text": str("<b>ð¤ ") + str(type_) + str("""</b>\n\n<b>ð¬ Bot tili:</b> O'zbekcha\n<b>ðµ Bot narxi:</b> """) + str(narx_) + str(" ") + str(pul_) + str("\n<b>ð Kunlik to'lov:</b> 200 ") + str(pul_) + str("\n\nð <b>Qo'shimcha ma'lumot:</b> <i>") + str(tavsif_) + str("</i>\n\nð Bonus sifatida 10 kunlik to'lov bepul taqdim etiladi!"), "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "â Yaratish", "callback_data": "botbor"})), Array(Array({"text": "âï¸ Orqaga", "callback_data": str("bolim-") + str(kategoriya_)})))}))}))
    else:
        bot("editMessageText", Array({"chat_id": ccid_, "message_id": cmid_, "text": str("<b>ð¤ ") + str(type_) + str("""</b>\n\n<b>ð¬ Bot tili:</b> O'zbekcha\n<b>ðµ Bot narxi:</b> """) + str(narx_) + str(" ") + str(pul_) + str("\n<b>ð Kunlik to'lov:</b> 200 ") + str(pul_) + str("\n\nð <b>Qo'shimcha ma'lumot:</b> <i>") + str(tavsif_) + str("</i>\n\nð Bonus sifatida 10 kunlik to'lov bepul taqdim etiladi!"), "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "â Yaratish", "callback_data": str("bots-") + str(type_) + str("-") + str(narx_) + str("-") + str(royxat_) + str("-") + str(kategoriya_)})), Array(Array({"text": "âï¸ Orqaga", "callback_data": str("bolim-") + str(kategoriya_)})))}))}))
    # end if
# end if
if data_ == "botbor":
    bot("answerCallbackQuery", Array({"callback_query_id": callid_, "text": "â ï¸ Sizda aktiv bot mavjud!", "show_alert": True}))
# end if
if php_mb_stripos(data_, "bots-") != False:
    ex_ = php_explode("-", data_)
    turi_ = ex_[1]
    narx_ = ex_[2]
    royxat_ = ex_[3]
    kategoriya_ = ex_[4]
    get_ = php_file_get_contents(str("foydalanuvchi/hisob/") + str(ccid_) + str(".txt"))
    if get_ < narx_:
        bot("answerCallbackQuery", Array({"callback_query_id": callid_, "text": "â ï¸ Hisobingizda mablag' yetarli emas", "show_alert": True}))
    else:
        bot("deleteMessage", Array({"chat_id": ccid_, "message_id": cmid_}))
        bot("sendMessage", Array({"chat_id": ccid_, "text": "<b>ð Botingizni tokenini yuboring:</b>\n\n<i>Token haqida ma'lumotga ega bo'lmasangiz qo'llanma bilan tanishib chiqing:</i>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"resize_keyboard": True, "keyboard": Array(Array(Array({"text": "ð Orqaga"})))}))}))
        file_put_contents(str("step/") + str(ccid_) + str(".txt"), str("bots&token-") + str(turi_) + str("-") + str(narx_) + str("-") + str(royxat_) + str("-") + str(kategoriya_))
    # end if
# end if
if php_mb_stripos(userstep_, "bots&token-") != False:
    ex_ = php_explode("-", userstep_)
    turi_ = ex_[1]
    narx_ = ex_[2]
    nomi_ = ex_[3]
    kategoriya_ = ex_[4]
    if php_mb_stripos(tx_, ":") != False:
        getid_ = bot("SendMessage", Array({"chat_id": cid_, "text": "<b>â Siz yuborgan bot tokeni qabul qilindi!</b>", "parse_mode": "html"})).result.message_id
        botuser_ = php_json_decode(php_file_get_contents(str("https://api.telegram.org/bot") + str(tx_) + str("/getme"))).result.username
        kod_ = php_file_get_contents(str("botlar/") + str(turi_) + str(".php"))
        kod_ = php_str_replace("API_TOKEN", str(tx_), kod_)
        kod_ = php_str_replace("ADMIN_ID", str(fid_), kod_)
        mkdir(str("foydalanuvchi/bot/") + str(cid_))
        file_put_contents(str("foydalanuvchi/bot/") + str(cid_) + str("/") + str(turi_) + str(".php"), kod_)
        get_ = php_json_decode(php_file_get_contents(str("https://api.telegram.org/bot") + str(tx_) + str("/setwebhook?url=https://") + PHP_SERVER["SERVER_NAME"] + str("/Nakmak/foydalanuvchi/bot/") + str(cid_) + str("/") + str(turi_) + str(".php"))).result
        if get_:
            botuser_ = php_json_decode(php_file_get_contents(str("https://api.telegram.org/bot") + str(tx_) + str("/getme"))).result.username
            nomi_ = php_json_decode(php_file_get_contents(str("https://api.telegram.org/bot") + str(tx_) + str("/getme"))).result.first_name
            id_ = php_json_decode(php_file_get_contents(str("https://api.telegram.org/bot") + str(tx_) + str("/getme"))).result.id
            mkdir(str("foydalanuvchi/bot/") + str(cid_))
            soat_ = date("H:i", strtotime("2 hour"))
            kun_ = date("d.m.y", strtotime("2 hour"))
            file_put_contents(str("foydalanuvchi/bot/") + str(cid_) + str("/soat.txt"), str(soat_))
            file_put_contents(str("foydalanuvchi/bot/") + str(cid_) + str("/kunida.txt"), str(kun_))
            file_put_contents(str("foydalanuvchi/bot/") + str(cid_) + str("/token.txt"), str(tx_))
            file_put_contents(str("foydalanuvchi/bot/") + str(cid_) + str("/botholat.txt"), "activ")
            file_put_contents(str("foydalanuvchi/bot/") + str(cid_) + str("/turi.txt"), str(turi_))
            file_put_contents(str("foydalanuvchi/bot/") + str(cid_) + str("/bots.txt"))
            if (php_isset(lambda : message_)):
                bots_ = php_file_get_contents(str("foydalanuvchi/bot/") + str(cid_) + str("/bots.txt"))
                if php_mb_stripos(bots_, botuser_) == False:
                    file_put_contents(str("foydalanuvchi/bot/") + str(cid_) + str("/bots.txt"), str(bots_) + str("\n") + str(botuser_))
                    bot("sendMessage", Array({"chat_id": admin_, "text": str("<b>â Yangi bot yaratildi!</b>\n\nð§¾ <b>Bot turi</b>: ") + str(turi_) + str("\nð <b>Bot useri</b>: @") + str(botuser_), "parse_mode": "html"}))
                    sleep(0.5)
                    bot("deleteMessage", Array({"chat_id": cid_, "message_id": mid_}))
                    sleep(1)
                    bot("editMessageText", Array({"chat_id": cid_, "message_id": getid_, "text": "<b>â¹ï¸ Botingiz tayyor. Quyidagi tugma orqali botingizga o'tishingiz mumkin.</b>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "â¡ï¸ Botga o'tish", "url": str("https://t.me/") + str(botuser_)})), Array(Array({"text": "âï¸ Orqaga", "callback_data": "orqagauz"})))}))}))
                    pul_ = php_file_get_contents(str("foydalanuvchi/hisob/") + str(cid_) + str(".txt"))
                    f_ = pul_ / 200
                    php_date_default_timezone_set("Asia/Tashkent")
                    t_ = date("d")
                    d_["sana"] = t_
                    d_["kun"] = 10
                    d_["puli"] = 2000
                    file_put_contents(str("foydalanuvchi/bot/") + str(cid_) + str("/kunlik.tolov"), php_json_encode(d_))
                    gett_ = php_file_get_contents(str("foydalanuvchi/hisob/") + str(cid_) + str(".txt"))
                    gett_ -= narx_
                    file_put_contents(str("foydalanuvchi/hisob/") + str(cid_) + str(".txt"), gett_)
                    aktivbot_ = php_file_get_contents("statistika/aktivbot.txt")
                    aktivbot_ += 1
                    file_put_contents("statistika/aktivbot.txt", aktivbot_)
                    hammabot_ = php_file_get_contents("statistika/hammabot.txt")
                    hammabot_ += 1
                    file_put_contents("statistika/hammabot.txt", hammabot_)
                # end if
            # end if
        # end if
        unlink(str("step/") + str(cid_) + str(".txt"))
    else:
        bot("sendMessage", Array({"chat_id": cid_, "message_id": getid_, "text": "<b>âï¸ Kechirasiz token qabul qilinmadi!</b>", "parse_mode": "html"}))
        unlink(str("step/") + str(cid_) + str(".txt"))
    # end if
    unlink(str("step/") + str(ccid_) + str(".txt"))
# end if
if tx_ == str(tugma2_) and joinchat(fid_) == "true":
    odam_ = php_file_get_contents(str("foydalanuvchi/referal/") + str(cid_) + str(".txt"))
    bot("sendMessage", Array({"chat_id": cid_, "text": str("<b>ð ID raqamingiz:</b> <code>") + str(cid_) + str("</code>\n\n<b>ðµ Asosiy balans:</b> ") + str(asosiy_) + str(" ") + str(pul_) + str("\n<b>ð¦ Qo'shimcha balans:</b> ") + str(sar_) + str(" ") + str(pul_) + str("\n<b>ð Takliflaringiz:</b> ") + str(odam_) + str(" ta\n\n<b>ð³ Botga kiritgan pullaringiz:</b> ") + str(kiritgan_) + str(" ") + str(pul_), "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "ð O'tkazmalar", "callback_data": "puliz"})), Array(Array({"text": "ð³ Hisobni to'ldirish", "callback_data": "oplata"})))}))}))
# end if
if data_ == "orqaga12" and joinchat(ccid_) == "true":
    hisob_ = php_file_get_contents(str("foydalanuvchi/hisob/") + str(ccid_) + str(".txt"))
    kiritgan_ = php_file_get_contents(str("foydalanuvchi/hisob/") + str(ccid_) + str(".1.txt"))
    sar_ = php_file_get_contents(str("foydalanuvchi/hisob/") + str(ccid_) + str(".1txt"))
    odam_ = php_file_get_contents(str("foydalanuvchi/referal/") + str(ccid_) + str(".txt"))
    bot("deleteMessage", Array({"chat_id": ccid_, "message_id": cmid_}))
    bot("SendMessage", Array({"chat_id": ccid_, "text": str("<b>ð ID raqamingiz:</b> <code>") + str(ccid_) + str("</code>\n\n<b>ðµ Asosiy balans:</b> ") + str(hisob_) + str(" ") + str(pul_) + str("\n<b>ð¦ Qo'shimcha balans:</b> ") + str(sar_) + str(" ") + str(pul_) + str("\n<b>ð Takliflaringiz:</b> ") + str(odam_) + str(" ta\n\n<b>ð³ Botga kiritgan pullaringiz:</b> ") + str(kiritgan_) + str(" ") + str(pul_), "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "ð O'tkazmalar", "callback_data": "puliz"})), Array(Array({"text": "ð³ Hisobni to'ldirish", "callback_data": "oplata"})))}))}))
# end if
if data_ == "puliz" and joinchat(ccid_) == "true":
    bot("deleteMessage", Array({"chat_id": ccid_, "message_id": cmid_}))
    bot("SendMessage", Array({"chat_id": ccid_, "text": "<b>Kerakli foydalanuvchi ID raqamini yuboring:</b>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"resize_keyboard": True, "keyboard": Array(Array(Array({"text": "ð Orqaga"})))}))}))
    file_put_contents(str("step/") + str(ccid_) + str(".txt"), "perevodid")
# end if
if userstep_ == "perevodid" and tx_ != "ð Orqaga" and joinchat(fid_) == "true":
    file_put_contents(str("otkazma/") + str(fid_) + str(".idraqam"), str(tx_))
    unlink(str("step/") + str(cid_) + str(".txt"))
    getid_ = bot("sendMessage", Array({"chat_id": cid_, "text": str("<b>Qancha mablag'ingizni o'tkazmoqchisiz?\n\nHisobingiz:</b> ") + str(asosiy_) + str(" ") + str(pul_), "parse_mode": "html", "reply_markup": php_json_encode(Array({"resize_keyboard": True, "keyboard": Array(Array(Array({"text": "ð Orqaga"})))}))}))
    file_put_contents(str("step/") + str(cid_) + str(".txt"), "perevodid1")
# end if
if userstep_ == "perevodid1" and tx_ != "ð Orqaga" and joinchat(fid_) == "true":
    file_put_contents(str("otkazma/") + str(cid_) + str(".pulraqam"), str(tx_))
    raqamid_ = php_file_get_contents(str("otkazma/") + str(cid_) + str(".idraqam"))
    raqapul_ = php_file_get_contents(str("otkazma/") + str(cid_) + str(".pulraqam"))
    olmos1_ = php_file_get_contents(str("foydalanuvchi/hisob/") + str(raqamid_) + str(".txt"))
    olmos2_ = php_file_get_contents(str("foydalanuvchi/hisob/") + str(cid_) + str(".txt"))
    csful_ = raqapul_ / 1 * 1
    if olmos2_ >= csful_ and tx_ >= 0:
        olmoslar1_ = olmos1_ + raqapul_
        olmoslar2_ = olmos2_ - csful_
        file_put_contents(str("foydalanuvchi/hisob/") + str(raqamid_) + str(".txt"), str(olmoslar1_))
        file_put_contents(str("foydalanuvchi/hisob/") + str(cid_) + str(".txt"), str(olmoslar2_))
        bot("sendMessage", Array({"chat_id": raqamid_, "text": str("<b>Hisobingizga</b> <a href='tg://user?id=") + str(cid_) + str("'>") + str(cid_) + str("</a><b> tomonidan ") + str(tx_) + str(" ") + str(pul_) + str(" o'tkazdi.</b>"), "parse_mode": "html"}))
        bot("sendMessage", Array({"chat_id": cid_, "text": "<b>â O'tkazma muvaffaqiyatli amalga oshirildi!</b>", "parse_mode": "html"}))
        unlink(str("step/") + str(cid_) + str(".txt"))
    else:
        bot("sendMessage", Array({"chat_id": cid_, "text": "<b>â ï¸ Hisobingizda mablag' yetarli emas!</b>", "parse_mode": "html"}))
    # end if
# end if
if data_ == "oplata" and joinchat(ccid_) == True:
    kategoriya_ = php_file_get_contents("sozlamalar/hamyon/kategoriya.txt")
    more_ = php_explode("\n", kategoriya_)
    soni_ = php_substr_count(kategoriya_, "\n")
    key_ = Array()
    for_ = 1
    while for_ <= soni_:
        
        title_ = php_str_replace("\n", "", more_[for_])
        key_[-1] = Array({"text": str(title_), "callback_data": str("karta-") + str(title_)})
        keyboard2_ = array_chunk(key_, 1)
        keyboard2_[-1] = Array(Array({"text": "âï¸ Orqaga", "callback_data": "orqaga12"}))
        bolim_ = php_json_encode(Array({"inline_keyboard": keyboard2_}))
        for_ += 1
    # end while
    if kategoriya_ == None:
        bot("answerCallbackQuery", Array({"callback_query_id": callid_, "text": "â ï¸ To'lov tizimlari qo'shilmagan!", "show_alert": True}))
    else:
        bot("editMessageText", Array({"chat_id": ccid_, "message_id": cmid_, "text": "<b>ð³ Quyidagi to'lov tizimlaridan birini tanlang:</b>", "parse_mode": "html", "reply_markup": bolim_}))
        sys.exit(0)
    # end if
# end if
if php_mb_stripos(data_, "karta-") != False:
    ex_ = php_explode("-", data_)
    kategoriya_ = ex_[1]
    raqam_ = php_file_get_contents(str("sozlamalar/hamyon/") + str(kategoriya_) + str("/raqam.txt"))
    bot("editMessageText", Array({"chat_id": ccid_, "message_id": cmid_, "text": str("<b>ð² Toâlov turi:</b> <u>") + str(kategoriya_) + str("</u>\n\nð³ Karta: <code>") + str(raqam_) + str("</code>\nð Izoh: #ID") + str(ccid_) + str("""\n\nAlmashuvingiz muvaffaqiyatli bajarilishi uchun quyidagi harakatlarni amalga oshiring: \n1) Istalgan pul miqdorini tepadagi Hamyonga tashlang\n2) Â«â To'lov qildimÂ» tugmasini bosing; \n4) Qancha pul miqdoni yuborganingizni kiritin;\n3) ToÊ»lov haqidagi suratni botga yuboring;\n3) Operator tomonidan almashuv tasdiqlanishini kuting!"""), "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "â To'lov qildim", "callback_data": "tolov"})), Array(Array({"text": "âï¸ Orqaga", "callback_data": "oplata"})))}))}))
# end if
if data_ == "tolov" and joinchat(ccid_) == "true":
    bot("DeleteMessage", Array({"chat_id": ccid_, "message_id": cmid_}))
    bot("SendMessage", Array({"chat_id": ccid_, "text": "<b>To'lov miqdorini kiriting:</b>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"resize_keyboard": True, "keyboard": Array(Array(Array({"text": "ð Orqaga"})))}))}))
    file_put_contents(str("step/") + str(ccid_) + str(".txt"), "oplata")
# end if
if userstep_ == "oplata" and joinchat(ccid_) == "true":
    if tx_ == "ð Orqaga":
        unlink(str("step/") + str(cid_) + str(".txt"))
    else:
        file_put_contents(str("step/hisob.") + str(cid_), text_)
        bot("SendMessage", Array({"chat_id": cid_, "text": "<b>To'lovingizni chek yoki skreenshotini shu yerga yuboring:</b>", "parse_mode": "html"}))
        file_put_contents(str("step/") + str(cid_) + str(".txt"), "rasm")
    # end if
# end if
if userstep_ == "rasm":
    if cid_ == admin_:
        if tx_ == "ð Orqaga":
            unlink(str("step/") + str(fid_) + str(".txt"))
        else:
            photo_ = message_.photo
            file_ = photo_[php_count(photo_) - 1].file_id
            bot("sendMessage", Array({"chat_id": admin_, "text": "*Hisobni to'ldirganingiz haqida ma'lumot asosiy adminga yuborildi. Agar to'lovni amalga oshirganingiz haqida ma'lumot mavjud bo'lsa, hisobingiz to'ldiriladi.*", "parse_mode": "MarkDown", "reply_markup": main_menuad_}))
            hisob_ = php_file_get_contents(str("step/hisob.") + str(fid_))
            unlink(str("step/") + str(fid_) + str(".txt"))
            bot("sendPhoto", Array({"chat_id": admin_, "photo": file_, "caption": str("ð <b>Foydalanuvchidan check:\n\nð®ââï¸ Foydalanuvchi:</b> <a href='https://tg://user?id=") + str(cid_) + str("'>") + str(name_) + str("</a>\nð <b>ID raqami:</b> ") + str(fid_) + str("\nðµ <b>To'lov miqdori:</b> ") + str(hisob_) + str(" ") + str(pul_), "disable_web_page_preview": True, "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "â Hisobini to'ldirish", "callback_data": str("on=") + str(fid_)})), Array(Array({"text": "â Bekor qilish", "callback_data": str("off=") + str(fid_)})))}))}))
        # end if
    else:
        if tx_ == "ð Orqaga":
            unlink(str("step/") + str(fid_) + str(".txt"))
        else:
            photo_ = message_.photo
            file_ = photo_[php_count(photo_) - 1].file_id
            bot("sendMessage", Array({"chat_id": cid_, "text": "*Hisobni to'ldirganingiz haqida ma'lumot asosiy adminga yuborildi. Agar to'lovni amalga oshirganingiz haqida ma'lumot mavjud bo'lsa, hisobingiz to'ldiriladi.*", "parse_mode": "MarkDown", "reply_markup": main_menu_}))
            hisob_ = php_file_get_contents(str("step/hisob.") + str(fid_))
            unlink(str("step/") + str(fid_) + str(".txt"))
            bot("sendPhoto", Array({"chat_id": admin_, "photo": file_, "caption": str("ð <b>Foydalanuvchidan check:\n\nð®ââï¸ Foydalanuvchi:</b> <a href='https://tg://user?id=") + str(cid_) + str("'>") + str(name_) + str("</a>\nð <b>ID raqami:</b> ") + str(fid_) + str("\nðµ <b>To'lov miqdori:</b> ") + str(hisob_) + str(" ") + str(pul_), "disable_web_page_preview": True, "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "â Hisobini to'ldirish", "callback_data": str("on=") + str(fid_)})), Array(Array({"text": "â Bekor qilish", "callback_data": str("off=") + str(fid_)})))}))}))
        # end if
    # end if
# end if
if php_mb_stripos(data_, "on=") != False:
    odam_ = php_explode("=", data_)[1]
    bot("deleteMessage", Array({"chat_id": ccid_, "message_id": cmid_}))
    hisob_ = php_file_get_contents(str("step/hisob.") + str(odam_))
    bot("SendMessage", Array({"chat_id": odam_, "text": str("<b>Hisobingiz ") + str(hisob_) + str(" ") + str(pul_) + str(" ga to'ldirildi</b>"), "parse_mode": "html"}))
    currency_ = php_file_get_contents(str("foydalanuvchi/hisob/") + str(odam_) + str(".1.txt"))
    get_ = php_file_get_contents(str("foydalanuvchi/hisob/") + str(odam_) + str(".txt"))
    get_ += hisob_
    currency_ += hisob_
    file_put_contents(str("foydalanuvchi/hisob/") + str(odam_) + str(".txt"), get_)
    file_put_contents(str("foydalanuvchi/hisob/") + str(odam_) + str(".1.txt"), currency_)
    bot("SendMessage", Array({"chat_id": admin_, "text": str("<b>Foydalanuvchi hisobi ") + str(hisob_) + str(" ") + str(pul_) + str(" ga to'ldirildi</b>"), "parse_mode": "html"}))
    unlink(str("step/hisob.") + str(odam_))
# end if
if php_mb_stripos(data_, "off=") != False:
    odam_ = php_explode("=", data_)[1]
    bot("deleteMessage", Array({"chat_id": ccid_, "message_id": cmid_}))
    hisob_ = php_file_get_contents(str("step/hisob.") + str(odam_))
    bot("SendMessage", Array({"chat_id": odam_, "text": str("<b>Hisobingizni ") + str(hisob_) + str(" ") + str(pul_) + str(" ga to'ldirish bekor qilindi</b>"), "parse_mode": "html"}))
    bot("SendMessage", Array({"chat_id": admin_, "text": "<b>Foydalanuvchi cheki bekor qilindi</b>", "parse_mode": "html"}))
    unlink(str("step/hisob.") + str(odam_))
# end if
if tx_ == str(tugma3_) and joinchat(fid_) == "true":
    bot("sendMessage", Array({"chat_id": cid_, "text": "<b>ð Quyidagilardan birini tanlang:</b>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": str(tugma7_), "callback_data": "taklifnoma"})))}))}))
# end if
if data_ == "orqaga3" and joinchat(ccid_) == "true":
    bot("deleteMessage", Array({"chat_id": ccid_, "message_id": cmid_}))
    bot("SendMessage", Array({"chat_id": ccid_, "text": "<b>ð Quyidagilardan birini tanlang:</b>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": str(tugma7_), "callback_data": "taklifnoma"})))}))}))
# end if
if data_ == "taklifnoma" and joinchat(ccid_) == "true":
    odam_ = php_file_get_contents(str("foydalanuvchi/referal/") + str(ccid_) + str(".txt"))
    bot("deleteMessage", Array({"chat_id": ccid_, "message_id": cmid_}))
    bot("sendMessage", Array({"chat_id": ccid_, "text": str("<b>ð Sizning taklif havolangiz:</b>\n\n<code>https://t.me/") + str(botname_) + str("?start=") + str(ccid_) + str("</code>\n\n<b>1 ta taklif uchun ") + str(taklifpul_) + str(" so'm beriladi\n\nSizning takliflaringiz: ") + str(odam_) + str(" ta</b>"), "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "ð¥ Do'stlarga yuborish", "url": str("https://t.me/share/url?url=https://t.me/") + str(botname_) + str("?start=") + str(ccid_)})), Array(Array({"text": "ð Orqaga", "callback_data": "orqaga3"})))}))}))
# end if
if text_ == str(tugma4_) and joinchat(cid_) == True:
    bot("sendMessage", Array({"chat_id": cid_, "text": "<b>ð Murojaat matnini yuboring:</b>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"resize_keyboard": True, "keyboard": Array(Array(Array({"text": "ð Orqaga"})))}))}))
    file_put_contents(str("step/") + str(cid_) + str(".txt"), "murojat")
# end if
if data_ == "boglanish" and joinchat(ccid_) == True:
    bot("deleteMessage", Array({"chat_id": ccid_, "message_id": cmid_}))
    bot("sendMessage", Array({"chat_id": ccid_, "text": "<b>ð Murojaat matnini yuboring:</b>\nSiz ham o'z biznesingizni boshlang bizning bot bilan @zero_builder_bot", "parse_mode": "html", "reply_markup": php_json_encode(Array({"resize_keyboard": True, "keyboard": Array(Array(Array({"text": "ð Orqaga"})))}))}))
    file_put_contents(str("step/") + str(ccid_) + str(".txt"), "murojat")
# end if
if userstep_ == "murojat":
    if text_ == "ð Orqaga":
        unlink(str("step/") + str(cid_) + str(".txt"))
    else:
        file_put_contents(str("step/") + str(cid_) + str(".murojat"), str(cid_))
        murojat_ = php_file_get_contents(str("step/") + str(cid_) + str(".murojat"))
        bot("sendMessage", Array({"chat_id": admin_, "text": str("<b>ð¨ Yangi murojat keldi:</b> ") + str(murojat_) + str("\n\n<b>ð Murojat matni:</b> ") + str(text_) + str("\n\n<b>â° Kelgan vaqti:</b> ") + str(soat_), "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "ð Javob yozish", "callback_data": str("yozish=") + str(murojat_)})))}))}))
        unlink(str("step/") + str(murojat_) + str(".txt"))
        if cid_ == admin_:
            bot("sendMessage", Array({"chat_id": admin_, "text": "<b>â Murojaatingiz yuborildi.</b>\n\n<i>Tez orada javob qaytaramiz!</i>", "parse_mode": "html", "reply_markup": main_menuad_}))
        else:
            bot("sendMessage", Array({"chat_id": murojat_, "text": "<b>â Murojaatingiz yuborildi.</b>\n\n<i>Tez orada javob qaytaramiz!</i>", "parse_mode": "html", "reply_markup": main_menu_}))
        # end if
    # end if
# end if
if php_mb_stripos(data_, "yozish=") != False:
    odam_ = php_explode("=", data_)[1]
    bot("deleteMessage", Array({"chat_id": ccid_, "message_id": cmid_}))
    bot("sendMessage", Array({"chat_id": ccid_, "text": "<b>Javob matnini yuboring:</b>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"resize_keyboard": True, "keyboard": Array(Array(Array({"text": "ð Orqaga"})))}))}))
    file_put_contents(str("step/") + str(ccid_) + str(".txt"), "javob")
    file_put_contents(str("step/") + str(ccid_) + str(".javob"), str(odam_))
# end if
if userstep_ == "javob":
    if tx_ == "ð Orqaga":
        unlink(str("step/") + str(admin_) + str(".step"))
        unlink(str("step/") + str(admin_) + str(".javob"))
    else:
        murojat_ = php_file_get_contents(str("step/") + str(cid_) + str(".javob"))
        bot("sendMessage", Array({"chat_id": murojat_, "text": str("<b>âï¸ Administrator:</b>\n\n<i>") + str(text_) + str("</i>"), "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "Javob yozish", "callback_data": "boglanish"})))}))}))
        bot("sendMessage", Array({"chat_id": admin_, "text": "<b>Javob yuborildi</b>", "parse_mode": "html", "reply_markup": main_menuad_}))
        unlink(str("step/") + str(murojat_) + str(".murojat"))
        unlink(str("step/") + str(admin_) + str(".step"))
        unlink(str("step/") + str(admin_) + str(".javob"))
    # end if
# end if
#// if($tx == "📩 Reklama Xizmati" and $cid == $admin){
if text_ == "ð ï¸ Sozlamalar" and joinchat(cid_) == True:
    bot("sendMessage", Array({"chat_id": cid_, "text": "<b>Menulardan birini tanlang</b>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "ð¦ Nakrutka BoÊ»lim", "callback_data": "nak_menu"})), Array(Array({"text": "ð¤ Maker BoÊ»lim", "callback_data": "mak_menu"})))}))}))
# end if
link_by_ = php_file_get_contents(str("nak/") + str(ccid_) + str("/havola.txt"))
son_by_ = php_file_get_contents(str("nak/") + str(ccid_) + str("/nechta.txt"))
if text_ == "ð¦ Buyurtma berish" and joinchat(cid_) == True:
    kategoriya_ = php_file_get_contents("sozlamalar/xizmat/kategoriya.txt")
    more_ = php_explode("\n", kategoriya_)
    soni_ = php_substr_count(kategoriya_, "\n")
    key_ = Array()
    for_ = 1
    while for_ <= soni_:
        
        title_ = php_str_replace("\n", "", more_[for_])
        titlle_ = php_str_replace("\n", "", more_[for_])
        key_[-1] = Array({"text": str(title_), "callback_data": str("nakkat-") + str(title_)})
        keyboard2_ = array_chunk(key_, 2)
        nakkat_ = php_json_encode(Array({"inline_keyboard": keyboard2_}))
        for_ += 1
    # end while
    if kategoriya_ == None:
        bot("SendMessage", Array({"chat_id": cid_, "text": "<b>â ï¸ Kategoriyalar mavjud emas!</b>", "parse_mode": "html"}))
        sys.exit(0)
    else:
        bot("SendMessage", Array({"chat_id": cid_, "text": "<b>ð± Quyidagi ijtimoiy tarmoqlardan birini tanlang:</b>", "parse_mode": "html", "reply_markup": nakkat_}))
        sys.exit(0)
    # end if
# end if
kategoriya_ = php_file_get_contents("sozlamalar/xizmat/kategoriya.txt")
if data_ == "bass" and joinchat(ccid_) == "true":
    more_ = php_explode("\n", kategoriya_)
    soni_ = php_substr_count(kategoriya_, "\n")
    key_ = Array()
    for_ = 1
    while for_ <= soni_:
        
        title_ = php_str_replace("\n", "", more_[for_])
        key_[-1] = Array({"text": str(title_), "callback_data": str("nakkat-") + str(title_)})
        keyboard2_ = array_chunk(key_, 2)
        nakkat_ = php_json_encode(Array({"inline_keyboard": keyboard2_}))
        for_ += 1
    # end while
    bot("deleteMessage", Array({"chat_id": ccid_, "message_id": cmid_}))
    bot("sendMessage", Array({"chat_id": ccid_, "text": "<b>ð± Quyidagi ijtimoiy tarmoqlardan birini tanlang:</b>", "parse_mode": "html", "reply_markup": nakkat_}))
    sys.exit(0)
# end if
if php_mb_stripos(data_, "nakkat-") != False:
    ex_ = php_explode("-", data_)
    kat_ = ex_[1]
    xizmat_ = php_file_get_contents(str("sozlamalar/xizmat/") + str(kat_) + str("/xizmat.txt"))
    kategoriya_ = php_file_get_contents("sozlamalar/xizmat/kategoriya.txt")
    more_ = php_explode("\n", xizmat_)
    soni_ = php_substr_count(xizmat_, "\n")
    keys_ = Array()
    for_ = 1
    while for_ <= soni_:
        
        title_ = php_str_replace("\n", "", more_[for_])
        keys_[-1] = Array({"text": str(title_), "callback_data": str("ichkinak-") + str(title_) + str("-") + str(kat_)})
        keysboard2_ = array_chunk(keys_, 1)
        keysboard2_[-1] = Array(Array({"text": "âï¸ Orqaga", "callback_data": "bass"}))
        ichkinak_ = php_json_encode(Array({"inline_keyboard": keysboard2_}))
        for_ += 1
    # end while
    if xizmat_ != None:
        bot("editMessageText", Array({"chat_id": ccid_, "message_id": cmid_, "text": "<b>â¬ï¸ Quyidagilardan birini tanlang:</b>", "parse_mode": "html", "reply_markup": ichkinak_}))
    else:
        bot("answerCallbackQuery", Array({"callback_query_id": callid_, "text": "ð Xizmatlar mavjud emas!", "show_alert": True}))
    # end if
# end if
if php_mb_stripos(data_, "ichkinak-") != False:
    ex_ = php_explode("-", data_)
    xiz_ = ex_[1]
    kat_ = ex_[2]
    xizmat_ = php_file_get_contents(str("sozlamalar/xizmatlar/") + str(kat_) + str("/") + str(xiz_) + str(".txt"))
    kategoriya_ = php_file_get_contents("sozlamalar/xizmat/kategoriya.txt")
    more_ = php_explode("\n", xizmat_)
    soni_ = php_substr_count(xizmat_, "\n")
    keys_ = Array()
    for_ = 1
    while for_ <= soni_:
        
        title_ = php_str_replace("\n", "", more_[for_])
        keys_[-1] = Array({"text": str(title_), "callback_data": str("buyurtma_berish-") + str(title_) + str("-") + str(kat_)})
        keysboard2_ = array_chunk(keys_, 1)
        keysboard2_[-1] = Array(Array({"text": "âï¸ Orqaga", "callback_data": "bass"}))
        xizmatlarim_ = php_json_encode(Array({"inline_keyboard": keysboard2_}))
        for_ += 1
    # end while
    if xizmat_ != None:
        bot("editMessageText", Array({"chat_id": ccid_, "message_id": cmid_, "text": "<b>â¬ï¸ Quyidagilardan birini tanlang:</b>", "parse_mode": "html", "reply_markup": xizmatlarim_}))
    else:
        bot("answerCallbackQuery", Array({"callback_query_id": callid_, "text": "ð Xizmatlar mavjud emas!", "show_alert": True}))
    # end if
# end if
if php_mb_stripos(data_, "buyurtma_berish-") != False:
    ex_ = php_explode("-", data_)
    royxat_ = ex_[1]
    kategoriya_ = ex_[2]
    id_ = php_file_get_contents(str("sozlamalar/xizmatlar/") + str(kategoriya_) + str("/") + str(royxat_) + str("/id.txt"))
    narxi_ = php_file_get_contents(str("sozlamalar/xizmatlar/") + str(kategoriya_) + str("/") + str(royxat_) + str("/narxi.txt"))
    tavsif_ = php_file_get_contents(str("sozlamalar/xizmatlar/") + str(kategoriya_) + str("/") + str(royxat_) + str("/tavsiya.txt"))
    min_ = php_file_get_contents(str("sozlamalar/xizmatlar/") + str(kategoriya_) + str("/") + str(royxat_) + str("/min.txt"))
    max_ = php_file_get_contents(str("sozlamalar/xizmatlar/") + str(kategoriya_) + str("/") + str(royxat_) + str("/max.txt"))
    bot("editMessageText", Array({"chat_id": ccid_, "message_id": cmid_, "text": str("<b>ð Xizmat nomi: ") + str(royxat_) + str("\n\nð Xizmat ID'si: ") + str(id_) + str("\nð° Narxi (1000x): ") + str(narxi_) + str(" ") + str(pul_) + str("\nð Malumot:</b> ") + str(tavsif_) + str("\n\nâ¬ Minimal buyurtma - ") + str(min_) + str(" ta\nâ« Maksimal buyurtma - ") + str(max_) + str(" ta"), "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "â Buyurtma berish", "callback_data": str("tanla-") + str(royxat_) + str("-") + str(narxi_) + str("-") + str(min_) + str("-") + str(max_) + str("-") + str(kategoriya_) + str("-") + str(id_)})), Array(Array({"text": "âï¸ Orqaga", "callback_data": "bass"})))}))}))
# end if
mkdir("nak")
mkdir(str("nak/") + str(cid_))
step_ = php_file_get_contents(str("step/") + str(cid_) + str(".step"))
api_kalit_ = php_file_get_contents("sozlamalar/api_kalit.txt")
api_sayt_ = php_file_get_contents("sozlamalar/api_sayt.txt")
holat_ = php_file_get_contents("sozlamalar/holat.txt")
if php_mb_stripos(data_, "tanla-") != False:
    ex_ = php_explode("-", data_)
    turi_ = ex_[1]
    narx_ = ex_[2]
    min_ = ex_[3]
    max_ = ex_[4]
    orid_ = ex_[6]
    ba_ = ex_[8]
    kategoriya_ = ex_[5]
    bot("deleteMessage", Array({"chat_id": ccid_, "message_id": ccid_}))
    bot("SendMessage", Array({"chat_id": ccid_, "text": "*ð Kerakli havolani kiriting (https://):*", "parse_mode": "markdown", "reply_markup": back_}))
    file_put_contents(str("step/") + str(ccid_) + str(".step"), str("botsin-") + str(turi_) + str("-") + str(narx_) + str("-") + str(min_) + str("-") + str(max_) + str("-") + str(kategoriya_) + str("-") + str(orid_) + str("-") + str(ba_))
# end if
if php_mb_stripos(step_, "botsin-") != False:
    ex_ = php_explode("-", step_)
    turi_ = ex_[1]
    narx_ = ex_[2]
    min_ = ex_[3]
    max_ = ex_[4]
    kategoriya_ = ex_[5]
    orid_ = ex_[6]
    ba_ = ex_[7]
    if (php_isset(lambda : text_)):
        file_put_contents(str("nak/") + str(cid_) + str("/havola.txt"), text_)
        bot("SendMessage", Array({"chat_id": cid_, "text": "*â¬ï¸ Kerakli buyurtma miqdorini kiriting:*", "parse_mode": "markdown"}))
        file_put_contents(str("step/") + str(cid_) + str(".step"), str("vjfin-") + str(turi_) + str("-") + str(narx_) + str("-") + str(min_) + str("-") + str(max_) + str("-") + str(orid_) + str("-") + str(ba_))
        sys.exit(0)
    # end if
# end if
if php_mb_stripos(step_, "vjfin-") != False:
    ex_ = php_explode("-", step_)
    tur_ = ex_[1]
    narx_ = ex_[2]
    min_ = ex_[3]
    max_ = ex_[4]
    orid_ = ex_[5]
    ba_ = ex_[6]
    if php_is_numeric(text_) and text_ > 0:
        if text_ >= min_ and text_ <= max_:
            file_put_contents(str("nak/") + str(cid_) + str("/nechta.txt"), text_)
            link_by_ = php_file_get_contents(str("nak/") + str(cid_) + str("/havola.txt"))
            soni_by_ = php_file_get_contents(str("nak/") + str(cid_) + str("/nechta.txt"))
            rak_ = text_ / 1000 * narx_
            bot("sendMessage", Array({"chat_id": cid_, "text": str("<b>â¡ï¸ Ma'lumotlarni o'qib chiqing:\n\nðµ Buyurtma narxi: ") + str(rak_) + str(" ") + str(pul_) + str("\nð Buyurtma manzili:</b> <code> ") + str(link_by_) + str(" </code>\nð¢ Buyurtma miqdori: <code> ") + str(soni_by_) + str(" </code> ta\n\n<b>â ï¸ Ma'lumotlar to'g'ri bo'lsa (â Yuborish) tugmasiga bosing va sizning xisobingizdan ") + str(rak_) + str(" ") + str(pul_) + str(" miqdorda pul yechib olinadi va buyurtma yuboriladi buyurtmani bekor qilish imkoni bo'lmaydi.</b>"), "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "â Yuborish", "callback_data": str("tasdiqnakin-") + str(tur_) + str("-") + str(rak_) + str("-") + str(orid_) + str("-") + str(ba_) + str("-") + str(link_) + str("-") + str(text_)})), Array(Array({"text": "âï¸ Bekor qilish", "callback_data": "yopish"})))}))}))
        else:
            bot("sendMessage", Array({"chat_id": cid_, "text": str("*â ï¸ Buyurtma miqdorini notogâri kiritilmoqda.\n \nâ¬ Minimal buyurtma - ") + str(min_) + str("\n â« Maksimal buyurtma - ") + str(max_) + str("\n \nð Boshqa miqdor kiriting.*"), "parse_mode": "markdown", "reply_markup": black_}))
        # end if
    else:
        bot("sendMessage", Array({"chat_id": cid_, "text": "*â ï¸ Buyurtma miqdori faqat raqamdan tashkil topgan boÊ»lishi kerak!*", "parse_mode": "markdown", "reply_markup": black_}))
    # end if
# end if
if php_mb_stripos(data_, "tasdiqnakin-") != False:
    ex_ = php_explode("-", data_)
    turi_ = ex_[1]
    narx_ = ex_[2]
    orid_ = ex_[3]
    ba_ = ex_[4]
    link_ = ex_[5]
    son_ = ex_[6]
    bot("deleteMessage", Array({"chat_id": ccid_, "message_id": ccid_}))
    pul_ = php_file_get_contents(str("foydalanuvchi/hisob/") + str(ccid_) + str(".txt"))
    if pul_ >= narx_:
        link_by_ = php_file_get_contents(str("nak/") + str(ccid_) + str("/havola.txt"))
        son_by_ = php_file_get_contents(str("nak/") + str(ccid_) + str("/nechta.txt"))
        urll_ = php_json_decode(php_file_get_contents(str("https://") + str(api_sayt_) + str("/api/v2/?key=") + str(api_kalit_) + str("&action=add&link=") + str(link_by_) + str("&quantity=") + str(son_by_) + str("&service=") + str(orid_)), True)
        order_ = urll_["order"]
        error_ = urll_["error"]
        if (php_isset(lambda : error_)):
            bot("sendMessage", Array({"chat_id": ccid_, "text": str(orid_) + str(" ") + str(error_), "parse_mode": "html", "reply_markup": menu_}))
        else:
            mm_ = pul_ - narx_
            file_put_contents(str("foydalanuvchi/hisob/") + str(ccid_) + str(".txt"), str(mm_))
            bot("sendMessage", Array({"chat_id": ccid_, "text": str("â Buyurtma qabul qilindi!\n\n Buyurtma IDsi: <code>") + str(order_) + str("</code>\n\nYuqoridagi ID orqali buyurtmangiz haqida ma'lumot olishingiz mumkin!"), "parse_mode": "html", "disable_web_page_preview": True, "reply_markup": main_menu_}))
            bson_ = php_file_get_contents(str("foydalanuvchi/buyurtma/") + str(ccid_) + str(".txt"))
            b_ = bson_ + 1
            file_put_contents(str("foydalanuvchi/buyurtma/") + str(ccid_) + str(".txt"), "b")
            #//
            unlink(str("step/") + str(ccud_) + str(".step"))
            unlink(str("nak/") + str(ccid_) + str("/havola.txt"))
            unlink(str("nak/") + str(ccid_) + str("/nechta.txt"))
        # end if
    else:
        bot("sendmessage", Array({"chat_id": ccid_, "text": "â ï¸ Balansingizda mablag' yetarli emas!", "reply_markup": main_menu_}))
    # end if
    unlink(str("step/") + str(ccid_) + str(".step"))
    unlink(str("nak/") + str(ccid_) + str("/havola.txt"))
    unlink(str("nak/") + str(ccid_) + str("/nechta.txt"))
# end if
if data_ == "yopish" and joinchat(ccid_) == "true":
    unlink(str("step/") + str(ccid_) + str(".step"))
    unlink(str("nak/") + str(ccid_) + str("/havola.txt"))
    unlink(str("nak/") + str(ccid_) + str("/nechta.txt"))
    bot("deleteMessage", Array({"chat_id": ccid_, "message_id": cmid_}))
# end if
mkdir("status")
mkdir(str(cid_))
api_kalit_ = php_file_get_contents("sozlamalar/api_kalit.txt")
api_sayt_ = php_file_get_contents("sozlamalar/api_sayt.txt")
okstat_ = php_file_get_contents(str("status/") + str(cid_) + str(".status"))
if text_ == "ð Buyurtma kuzatish" and joinchat(cid_) == True:
    bot("sendMessage", Array({"chat_id": cid_, "text": "*ð Buyurtma ID sini kiriting:*", "parse_mode": "MarkDown", "reply_markup": php_json_encode(Array({"resize_keyboard": True, "keyboard": Array(Array(Array({"text": "â¬ï¸ Orqaga"})))}))}))
    mkdir("status")
    file_put_contents(str("status/") + str(cid_) + str(".status"), "1")
# end if
if okstat_ == 1:
    if php_is_numeric(text_):
        orderstat_ = php_json_decode(php_file_get_contents(str("https://") + str(api_sayt_) + str("/api/v2?key=") + str(api_kalit_) + str("&action=status&order=") + str(text_)), True)
        miqdor_ = orderstat_["remains"]
        xolati_ = orderstat_["status"]
        if orderstat_["status"] != None or orderstat_["remains"] != None:
            bot("sendMessage", Array({"chat_id": cid_, "text": str("*\nð Buyurtma idsi: ") + str(text_) + str("\nð Buyurtmangiz: ") + str(xolati_) + str("\nð¢ Qoldiq miqdori: ") + str(miqdor_) + str(" ta*"), "parse_mode": "MarkDown", "reply_markup": main_menu_}))
            unlink(str("status/") + str(cid_) + str(".status"))
        else:
            bot("sendMessage", Array({"chat_id": cid_, "text": "*ð¤·ââ Mavjud emas!*", "parse_mode": "MarkDown"}))
            unlink(str("status/") + str(cid_) + str(".status"))
        # end if
    # end if
# end if
if tx_ == "ðï¸ Xizmatlar" and cid_ == admin_:
    bot("sendMessage", Array({"chat_id": cid_, "text": "ðï¸ <b>Xizmatlar sozlash bo'limidasiz:</b>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "ð Bo'lim", "callback_data": "kategoriyaxiz"})), Array(Array({"text": "ð Ichki bolim", "callback_data": "ichki"})), Array(Array({"text": "ðï¸ Xizmatlar", "callback_data": "xizmat"})))}))}))
# end if
if data_ == "kategoriyaxiz":
    bot("editMessageText", Array({"chat_id": ccid_, "message_id": cmid_, "text": "ð <b>Quyidagilardan birini tanlang:</b>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "â Kategoriya qo'shish", "callback_data": "adbolim"})), Array(Array({"text": "ð Kategoriya", "callback_data": "delbolim"})), Array(Array({"text": "âï¸ Orqaga", "callback_data": "nakxiz"})))}))}))
# end if
if data_ == "xizmat":
    bot("editMessageText", Array({"chat_id": ccid_, "message_id": cmid_, "text": "ð <b>Quyidagilardan birini tanlang:</b>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "â Ichki xizmat qo'shish", "callback_data": "IchkiAdXiz"})), Array(Array({"text": "ðï¸ OÊ»chirish", "callback_data": "xizochir"})), Array(Array({"text": "âï¸ Orqaga", "callback_data": "nakxiz"})))}))}))
# end if
#// Add Xizmat
if data_ == "IchkiAdXiz":
    kategoriya_ = php_file_get_contents("sozlamalar/xizmat/kategoriya.txt")
    more_ = php_explode("\n", kategoriya_)
    soni_ = php_substr_count(kategoriya_, "\n")
    keys_ = Array()
    for_ = 1
    while for_ <= soni_:
        
        title_ = php_str_replace("\n", "", more_[for_])
        keys_[-1] = Array({"text": str(title_) + str(" - sozlash"), "callback_data": str("ichkisetxiz-") + str(title_)})
        keysboard2_ = array_chunk(keys_, 1)
        keysboard2_[-1] = Array(Array({"text": "âï¸ Orqaga", "callback_data": "bbosh"}))
        keyy_ = php_json_encode(Array({"inline_keyboard": keysboard2_}))
        for_ += 1
    # end while
    if kategoriya_ != None:
        bot("editMessageText", Array({"chat_id": ccid_, "message_id": cmid_, "text": "<b>ð Kategoriyalar ro'yxati:</b>", "parse_mode": "html", "reply_markup": keyy_}))
    else:
        bot("answerCallbackQuery", Array({"callback_query_id": callid_, "text": "ð Kategoriyalar mavjud emas!", "show_alert": True}))
    # end if
# end if
if php_mb_stripos(data_, "ichkisetxiz-") != False:
    ex_ = php_explode("-", data_)
    kat_ = ex_[1]
    xizmat_ = php_file_get_contents(str("sozlamalar/xizmat/") + str(kat_) + str("/xizmat.txt"))
    more_ = php_explode("\n", xizmat_)
    soni_ = php_substr_count(xizmat_, "\n")
    keys_ = Array()
    for_ = 1
    while for_ <= soni_:
        
        title_ = php_str_replace("\n", "", more_[for_])
        keys_[-1] = Array({"text": str(title_) + str(" - sozlash"), "callback_data": str("xizmatset-") + str(title_) + str("-") + str(kat_)})
        keysboard2_ = array_chunk(keys_, 1)
        keysboard2_[-1] = Array(Array({"text": "âï¸ Orqaga", "callback_data": "bbosh"}))
        keyyy_ = php_json_encode(Array({"inline_keyboard": keysboard2_}))
        for_ += 1
    # end while
    if xizmat_ != None:
        bot("editMessageText", Array({"chat_id": ccid_, "message_id": cmid_, "text": "<b>ð Xizmatlar ro'yxati:</b>", "parse_mode": "html", "reply_markup": keyyy_}))
    else:
        bot("answerCallbackQuery", Array({"callback_query_id": callid_, "text": "ð Xizmatlar mavjud emas!", "show_alert": True}))
    # end if
# end if
if php_mb_stripos(data_, "xizmatset-") != False:
    ex_ = php_explode("-", data_)
    xiz_ = ex_[1]
    kat_ = ex_[2]
    mkdir(str("sozlamalar/xizmatlar/") + str(kat_))
    mkdir(str("sozlamalar/xizmatlar/") + str(kat_) + str("/") + str(xiz_))
    bot("deleteMessage", Array({"chat_id": ccid_, "message_id": cmid_}))
    bot("sendMessage", Array({"chat_id": ccid_, "text": "<b>ð Yangi xizmat nomini yuboring:</b>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"resize_keyboard": True, "keyboard": Array(Array(Array({"text": "ð Boshqaruv"})))}))}))
    file_put_contents(str("step/") + str(ccid_) + str(".txt"), str("royhatset-") + str(xiz_) + str("-") + str(kat_))
# end if
if php_mb_stripos(userstep_, "royhatset-") != False:
    ex_ = php_explode("-", userstep_)
    xiz_ = ex_[1]
    roy_ = ex_[2]
    if tx_ == "ð Boshqaruv":
        unlink(str("step/") + str(cid_) + str(".txt"))
    else:
        if cid_ == admin_:
            if (php_isset(lambda : text_)):
                mkdir(str("sozlamalar/xizmatlar/") + str(roy_) + str("/") + str(text_))
                royhat_ = php_file_get_contents(str("sozlamalar/xizmatlar/") + str(roy_) + str("/") + str(xiz_) + str(".txt"))
                file_put_contents(str("sozlamalar/xizmatlar/") + str(roy_) + str("/") + str(xiz_) + str(".txt"), str(royhat_) + str("\n") + str(text_))
                bot("SendMessage", Array({"chat_id": cid_, "text": str(text_) + str(" <b> qabul qilindi!\n\nXizmat narxini yuboring:</b>"), "parse_mode": "html", "reply_markup": php_json_encode(Array({"resize_keyboard": True, "keyboard": Array(Array(Array({"text": "ð Boshqaruv"})))}))}))
                file_put_contents(str("step/") + str(cid_) + str(".txt"), str("xizmatnarx-") + str(xiz_) + str("-") + str(roy_) + str("-") + str(text_))
            # end if
        # end if
    # end if
# end if
if php_mb_stripos(userstep_, "xizmatnarx-") != False:
    ex_ = php_explode("-", userstep_)
    xiz_ = ex_[1]
    roy_ = ex_[2]
    turi_ = ex_[3]
    if tx_ == "ð Boshqaruv":
        pass
    else:
        if cid_ == admin_:
            if (php_isset(lambda : text_)):
                file_put_contents(str("sozlamalar/xizmatlar/") + str(roy_) + str("/") + str(turi_) + str("/narxi.txt"), str(text_))
                bot("SendMessage", Array({"chat_id": cid_, "text": str(text_) + str(" <b> qabul qilindi!\n\nma'lumotlarni kiriting:</b>"), "parse_mode": "html", "reply_markup": php_json_encode(Array({"resize_keyboard": True, "keyboard": Array(Array(Array({"text": "ð Boshqaruv"})))}))}))
                file_put_contents(str("step/") + str(cid_) + str(".txt"), str("xizmattavsiya-") + str(xiz_) + str("-") + str(roy_) + str("-") + str(turi_))
            # end if
        # end if
    # end if
# end if
if php_mb_stripos(userstep_, "xizmattavsiya-") != False:
    ex_ = php_explode("-", userstep_)
    xiz_ = ex_[1]
    roy_ = ex_[2]
    turi_ = ex_[3]
    if tx_ == "ð Boshqaruv":
        unlink(str("step/") + str(cid_) + str(".txt"))
    else:
        if cid_ == admin_:
            if (php_isset(lambda : text_)):
                file_put_contents(str("sozlamalar/xizmatlar/") + str(roy_) + str("/") + str(turi_) + str("/tavsiya.txt"), str(text_))
                bot("SendMessage", Array({"chat_id": cid_, "text": str(text_) + str(" <b> qabul qilindi!\n\nMinimal buyurtmani kiriting:</b>"), "parse_mode": "html", "reply_markup": php_json_encode(Array({"resize_keyboard": True, "keyboard": Array(Array(Array({"text": "ð Boshqaruv"})))}))}))
                file_put_contents(str("step/") + str(cid_) + str(".txt"), str("min-") + str(xiz_) + str("-") + str(roy_) + str("-") + str(turi_))
            # end if
        # end if
    # end if
# end if
if php_mb_stripos(userstep_, "min-") != False:
    ex_ = php_explode("-", userstep_)
    xiz_ = ex_[1]
    roy_ = ex_[2]
    turi_ = ex_[3]
    if tx_ == "ð Boshqaruv":
        unlink(str("step/") + str(cid_) + str(".txt"))
    else:
        if cid_ == admin_:
            if (php_isset(lambda : text_)):
                file_put_contents(str("sozlamalar/xizmatlar/") + str(roy_) + str("/") + str(turi_) + str("/min.txt"), str(text_))
                bot("SendMessage", Array({"chat_id": cid_, "text": str(text_) + str(" <b> qabul qilindi!\n\nMaksimal buyurtmani kiriting:</b>"), "parse_mode": "html", "reply_markup": php_json_encode(Array({"resize_keyboard": True, "keyboard": Array(Array(Array({"text": "ð Boshqaruv"})))}))}))
            # end if
            file_put_contents(str("step/") + str(cid_) + str(".txt"), str("max-") + str(xiz_) + str("-") + str(roy_) + str("-") + str(turi_))
        # end if
    # end if
# end if
if php_mb_stripos(userstep_, "max-") != False:
    ex_ = php_explode("-", userstep_)
    xiz_ = ex_[1]
    roy_ = ex_[2]
    turi_ = ex_[3]
    if tx_ == "ð Boshqaruv":
        unlink(str("step/") + str(cid_) + str(".txt"))
    else:
        if cid_ == admin_:
            if (php_isset(lambda : text_)):
                file_put_contents(str("sozlamalar/xizmatlar/") + str(roy_) + str("/") + str(turi_) + str("/max.txt"), str(text_))
                bot("SendMessage", Array({"chat_id": cid_, "text": str(text_) + str(" <b> qabul qilindi!\n\nUshbu Xizmat idsini kiriting:</b>"), "parse_mode": "html", "reply_markup": php_json_encode(Array({"resize_keyboard": True, "keyboard": Array(Array(Array({"text": "ð Boshqaruv"})))}))}))
                file_put_contents(str("step/") + str(cid_) + str(".txt"), str("id-") + str(xiz_) + str("-") + str(roy_) + str("-") + str(turi_))
            # end if
        # end if
    # end if
# end if
if php_mb_stripos(userstep_, "id-") != False:
    ex_ = php_explode("-", userstep_)
    xiz_ = ex_[1]
    roy_ = ex_[2]
    turi_ = ex_[3]
    if tx_ == "ð Boshqaruv":
        unlink(str("step/") + str(cid_) + str(".txt"))
    else:
        if cid_ == admin_:
            if (php_isset(lambda : text_)):
                file_put_contents(str("sozlamalar/xizmatlar/") + str(roy_) + str("/") + str(turi_) + str("/id.txt"), str(text_))
                bot("SendMessage", Array({"chat_id": cid_, "text": "<b>Xizmati qoÊ»shildi:</b>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"resize_keyboard": True, "keyboard": Array(Array(Array({"text": "ð Boshqaruv"})))}))}))
            # end if
            unlink(str("step/") + str(cid_) + str(".txt"))
        # end if
    # end if
# end if
if data_ == "ichki":
    bot("editMessageText", Array({"chat_id": ccid_, "message_id": cmid_, "text": "ð <b>Quyidagilardan birini tanlang:</b>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "â Xizmat qo'shish", "callback_data": "ichkiqosh"})), Array(Array({"text": "ðï¸ OÊ»chirish", "callback_data": "listXiz"})), Array(Array({"text": "âï¸ Orqaga", "callback_data": "nakxiz"})))}))}))
# end if
#// Delete Ichki bolim
if data_ == "listXiz":
    kategoriya_ = php_file_get_contents("sozlamalar/xizmat/kategoriya.txt")
    more_ = php_explode("\n", kategoriya_)
    soni_ = php_substr_count(kategoriya_, "\n")
    keys_ = Array()
    for_ = 1
    while for_ <= soni_:
        
        title_ = php_str_replace("\n", "", more_[for_])
        keys_[-1] = Array({"text": str(title_) + str(" - sozlash"), "callback_data": str("settxiz-") + str(title_)})
        keysboard2_ = array_chunk(keys_, 1)
        keysboard2_[-1] = Array(Array({"text": "âï¸ Orqaga", "callback_data": "bbosh"}))
        keyy_ = php_json_encode(Array({"inline_keyboard": keysboard2_}))
        for_ += 1
    # end while
    if kategoriya_ != None:
        bot("editMessageText", Array({"chat_id": ccid_, "message_id": cmid_, "text": "<b>ð Kategoriyalar ro'yxati:</b>", "parse_mode": "html", "reply_markup": keyy_}))
    else:
        bot("answerCallbackQuery", Array({"callback_query_id": callid_, "text": "ð Kategoriyalar mavjud emas!", "show_alert": True}))
    # end if
# end if
if php_mb_stripos(data_, "settxiz-") != False:
    ex_ = php_explode("-", data_)
    kat_ = ex_[1]
    xizmat_ = php_file_get_contents(str("sozlamalar/xizmat/") + str(kat_) + str("/xizmat.txt"))
    more_ = php_explode("\n", xizmat_)
    soni_ = php_substr_count(xizmat_, "\n")
    keys_ = Array()
    for_ = 1
    while for_ <= soni_:
        
        title_ = php_str_replace("\n", "", more_[for_])
        keys_[-1] = Array({"text": str(title_) + str(" - sozlash"), "callback_data": str("xizmatsozlash-") + str(title_) + str("-") + str(kat_)})
        keysboard2_ = array_chunk(keys_, 1)
        keysboard2_[-1] = Array(Array({"text": "âï¸ Orqaga", "callback_data": "bbosh"}))
        keyyy_ = php_json_encode(Array({"inline_keyboard": keysboard2_}))
        for_ += 1
    # end while
    if xizmat_ != None:
        bot("editMessageText", Array({"chat_id": ccid_, "message_id": cmid_, "text": "<b>ð Xizmatlar ro'yxati:</b>", "parse_mode": "html", "reply_markup": keyyy_}))
    else:
        bot("answerCallbackQuery", Array({"callback_query_id": callid_, "text": "ð Xizmatlar mavjud emas!", "show_alert": True}))
    # end if
# end if
if php_mb_stripos(data_, "xizmatsozlash-") != False:
    ex_ = php_explode("-", data_)
    royxat_ = ex_[1]
    kategoriya_ = ex_[2]
    narxi_ = php_file_get_contents(str("sozlamalar/xizmatlar/") + str(kategoriya_) + str("/") + str(royxat_) + str("/narxi.txt"))
    tavsif_ = php_file_get_contents(str("sozlamalar/xizmatlar/") + str(kategoriya_) + str("/") + str(royxat_) + str("/tavsiya.txt"))
    min_ = php_file_get_contents(str("sozlamalar/xizmatlar/") + str(kategoriya_) + str("/") + str(royxat_) + str("/min.txt"))
    max_ = php_file_get_contents(str("sozlamalar/xizmatlar/") + str(kategoriya_) + str("/") + str(royxat_) + str("/max.txt"))
    bot("editMessageText", Array({"chat_id": ccid_, "message_id": cmid_, "text": str("<b>ð Xizmat nomi:</b> ") + str(royxat_), "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "ðï¸ OÊ»chirish", "callback_data": str("delxizmat-") + str(royhat_) + str("-") + str(kategoriya_)})), Array(Array({"text": "âï¸ Orqaga", "callback_data": "Xizmatlar"})))}))}))
# end if
if php_mb_stripos(data_, "delxizmat-") != False:
    ex_ = php_explode("-", data_)
    roy_ = ex_[1]
    kat_ = ex_[2]
    royxat_ = php_file_get_contents(str("sozlamalar/xizmat/") + str(kat_) + str("/xizmat.txt"))
    k_ = php_str_replace("\n\n" + roy_ + "", "", royxat_)
    file_put_contents(str("sozlamalar/xizmat/") + str(kat_) + str("/xizmat.txt"), k_)
    bot("editMessageText", Array({"chat_id": ccid_, "message_id": cmid_, "text": "<b>O'chirish yakunlandi!</b>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "âï¸ Orqaga", "callback_data": "kategoriya"})))}))}))
    deleteFolder(str("sozlamalar/xizmat/") + str(kat_) + str("/") + str(roy_))
# end if
if data_ == "nakxiz":
    bot("deleteMessage", Array({"chat_id": ccid_, "message_id": cmid_}))
    bot("sendMessage", Array({"chat_id": ccid_, "text": "ðï¸ <b>Xizmatlar sozlash bo'limidasiz:</b>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "ð Bo'lim", "callback_data": "kategoriyaxiz"})), Array(Array({"text": "ð Ichki bolim", "callback_data": "ichki"})), Array(Array({"text": "ðï¸ Xizmatlar", "callback_data": "xizmat"})))}))}))
# end if
#// Add Ichki bolim
if data_ == "ichkiqosh":
    kategoriya_ = php_file_get_contents("sozlamalar/xizmat/kategoriya.txt")
    more_ = php_explode("\n", kategoriya_)
    soni_ = php_substr_count(kategoriya_, "\n")
    keys_ = Array()
    for_ = 1
    while for_ <= soni_:
        
        title_ = php_str_replace("\n", "", more_[for_])
        keys_[-1] = Array({"text": str(title_), "callback_data": str("ichkiqosh-") + str(title_)})
        keysboard2_ = array_chunk(keys_, 1)
        keysboard2_[-1] = Array(Array({"text": "âï¸ Orqaga", "callback_data": "bbosh"}))
        ichkiqosh_ = php_json_encode(Array({"inline_keyboard": keysboard2_}))
        for_ += 1
    # end while
    if kategoriya_ != None:
        bot("editMessageText", Array({"chat_id": ccid_, "message_id": cmid_, "text": "<b>ð Qaysi kategoriyaga qo'shamiz?</b>", "parse_mode": "html", "reply_markup": ichkiqosh_}))
    else:
        bot("answerCallbackQuery", Array({"callback_query_id": callid_, "text": "ð Kategoriyalar mavjud emas!", "show_alert": True}))
    # end if
# end if
if php_mb_stripos(data_, "ichkiqosh-") != False:
    ex_ = php_explode("-", data_)
    kat_ = ex_[1]
    bot("deleteMessage", Array({"chat_id": ccid_, "message_id": cmid_}))
    bot("sendMessage", Array({"chat_id": ccid_, "text": "<b>ð Yangi xizmat nomini yuboring:</b>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"resize_keyboard": True, "keyboard": Array(Array(Array({"text": "ð Boshqaruv"})))}))}))
    file_put_contents(str("step/") + str(ccid_) + str(".txt"), str("ichkiqosh-") + str(kat_))
    sys.exit(0)
# end if
if php_mb_stripos(userstep_, "ichkiqosh-") != False:
    ex_ = php_explode("-", userstep_)
    kat_ = ex_[1]
    if tx_ == "ð Boshqaruv":
        unlink(str("step/") + str(cid_) + str(".txt"))
    else:
        if cid_ == admin_:
            if (php_isset(lambda : text_)):
                mkdir(str("sozlamalar/xizmat/") + str(kat_) + str("/") + str(text_))
                file_put_contents(str("sozlamalar/xizmat/") + str(kat_) + str("/") + str(text_) + str("/xizmat.txt"))
                xizmat_ = php_file_get_contents(str("sozlamalar/xizmat/") + str(kat_) + str("/xizmat.txt"))
                file_put_contents(str("sozlamalar/xizmat/") + str(kat_) + str("/xizmat.txt"), str(xizmat_) + str("\n") + str(text_))
                bot("SendMessage", Array({"chat_id": cid_, "text": str(text_) + str(" <b>nomli xizmat qo'shildi</b>"), "parse_mode": "html", "reply_markup": admin1_menu_}))
            # end if
            unlink(str("step/") + str(cid_) + str(".txt"))
        # end if
    # end if
# end if
#// Delete bolim
if data_ == "delbolim":
    kategoriya_ = php_file_get_contents("sozlamalar/xizmat/kategoriya.txt")
    more_ = php_explode("\n", kategoriya_)
    soni_ = php_substr_count(kategoriya_, "\n")
    keys_ = Array()
    for_ = 1
    while for_ <= soni_:
        
        title_ = php_str_replace("\n", "", more_[for_])
        keys_[-1] = Array({"text": str(title_) + str(" - sozlash"), "callback_data": str("delbolim-") + str(title_)})
        keysboard2_ = array_chunk(keys_, 1)
        keysboard2_[-1] = Array(Array({"text": "âï¸ Orqaga", "callback_data": "bbosh"}))
        key_ = php_json_encode(Array({"inline_keyboard": keysboard2_}))
        for_ += 1
    # end while
    if kategoriya_ != None:
        bot("editMessageText", Array({"chat_id": ccid_, "message_id": cmid_, "text": "<b>ð Kategoriyalar ro'yxati:</b>", "parse_mode": "html", "reply_markup": key_}))
    else:
        bot("answerCallbackQuery", Array({"callback_query_id": callid_, "text": "ð Kategoriyalar mavjud emas!", "show_alert": True}))
    # end if
# end if
if php_mb_stripos(data_, "delbolim-") != False:
    ex_ = php_explode("-", data_)
    kat_ = ex_[1]
    bot("editMessageText", Array({"chat_id": ccid_, "message_id": cmid_, "text": str("ð <b>Kategoriya nomi:</b> ") + str(kat_), "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "ð O'chirish", "callback_data": str("deletebolim-") + str(kat_)})), Array(Array({"text": "âï¸ Orqaga", "callback_data": "listKat"})))}))}))
# end if
if php_mb_stripos(data_, "deletebolim-") != False:
    ex_ = php_explode("-", data_)
    kat_ = ex_[1]
    k_ = php_str_replace("\n" + kat_ + "", "", kategoriya_)
    file_put_contents("sozlamalar/xizmat/kategoriya.txt", k_)
    bot("editMessageText", Array({"chat_id": ccid_, "message_id": cmid_, "text": "<b>O'chirish yakunlandi!</b>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "âï¸ Orqaga", "callback_data": "kategoriya"})))}))}))
    deleteFolder(str("sozlamalar/xizmat/") + str(kat_))
# end if
#// Add bolim
if data_ == "adbolim":
    bot("deleteMessage", Array({"chat_id": ccid_, "message_id": cmid_}))
    bot("sendMessage", Array({"chat_id": ccid_, "text": "<b>ð Yangi kategoriya nomini yuboring:</b>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"resize_keyboard": True, "keyboard": Array(Array(Array({"text": "ð Boshqaruv"})))}))}))
    file_put_contents(str("step/") + str(ccid_) + str(".txt"), "adbolim")
    sys.exit(0)
# end if
if userstep_ == "adbolim":
    if tx_ == "ð Boshqaruv":
        unlink(str("step/") + str(cid_) + str(".txt"))
    else:
        if cid_ == admin_:
            if (php_isset(lambda : text_)):
                kategoriya_ = php_file_get_contents("sozlamalar/xizmat/kategoriya.txt")
                file_put_contents("sozlamalar/xizmat/kategoriya.txt", str(kategoriya_) + str("\n") + str(text_))
                mkdir(str("sozlamalar/xizmat/") + str(text_))
                bot("SendMessage", Array({"chat_id": cid_, "text": str(text_) + str(" <b>nomli kategoriya qo'shildi</b>"), "parse_mode": "html", "reply_markup": admin1_menu_}))
            # end if
            unlink(str("step/") + str(cid_) + str(".txt"))
        # end if
    # end if
# end if
if text_:
    if holat_ == "â":
        if cid_ == admin_:
            pass
        else:
            bot("sendMessage", Array({"chat_id": cid_, "text": "âï¸ <b>Bot vaqtinchalik o'chirilgan!</b>\n\n<i>âï¸ Botda ta'mirlash ishlari olib borilayotgan bo'lishi mumkin!</i>", "parse_mode": "html"}))
            sys.exit(0)
        # end if
    # end if
# end if
if data_:
    if holat_ == "â":
        if ccid_ == admin_:
            pass
        else:
            bot("answerCallbackQuery", Array({"callback_query_id": qid_, "text": "âï¸ Bot vaqtinchalik o'chirilgan!\n\nâï¸ Botda ta'mirlash ishlari olib borilayotgan bo'lishi mumkin!", "show_alert": True}))
            sys.exit(0)
        # end if
    # end if
# end if
if text_ == "ð¤ Bot holati":
    if cid_ == admin_:
        bot("SendMessage", Array({"chat_id": admin_, "text": str("<b>ð Hozirgi holat:</b> ") + str(holat_), "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "â", "callback_data": "holat-â"}), Array({"text": "â", "callback_data": "holat-â"})), Array(Array({"text": "Yopish", "callback_data": "boshqaruv"})))}))}))
    # end if
# end if
if php_mb_stripos(data_, "holat-") != False:
    ex_ = php_explode("-", data_)
    xolat_ = ex_[1]
    file_put_contents("sozlamalar/holat.txt", xolat_)
    bot("editMessageText", Array({"chat_id": ccid_, "message_id": mid2_, "text": str("<b>ð Hozirgi holat:</b> ") + str(xolat_), "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "â", "callback_data": "holat-â"}), Array({"text": "â", "callback_data": "holat-â"})), Array(Array({"text": "Yopish", "callback_data": "boshqaruv"})))}))}))
# end if
api_kalit_ = php_file_get_contents("sozlamalar/api_kalit.txt")
api_sayt_ = php_file_get_contents("sozlamalar/api_sayt.txt")
holat_ = php_file_get_contents("sozlamalar/holat.txt")
if tx_ == "ð Api sozlamalari" and cid_ == admin_:
    bot("sendMessage", Array({"chat_id": cid_, "text": "<b>ð Api sozlash bo'limidasiz:</b>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "ð Hozirgi holati", "callback_data": "api_holati"})), Array(Array({"text": "ð Api kalit", "callback_data": "Api_kalit"}), Array({"text": "ð Api sayt", "callback_data": "Api_sayt"})), Array(Array({"text": "ðµ Api hisob", "callback_data": "Api_hisob"})))}))}))
# end if
if data_ == "api_holati":
    api_balance_ = php_json_decode(php_file_get_contents(str("https://") + str(api_sayt_) + str("/api/v2?key=") + str(api_kalit_) + str("&action=balance")), True)
    bot("editMessageText", Array({"chat_id": ccid_, "message_id": cmid_, "text": str("<b>\nð Api kalit: ") + str(api_kalit_) + str("\n\nð Api Sayt: ") + str(api_sayt_) + str("""\n\nðµ API Balansingizda\n""") + api_balance_["balance"] + str(" ") + str(pul_) + str(" </b>"), "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "âï¸ Ortga", "callback_data": "api_sozlamalari"})))}))}))
# end if
if data_ == "Api_hisob" and ccid_ == admin_:
    api_balance_ = php_json_decode(php_file_get_contents(str("https://") + str(api_sayt_) + str("/api/v2?key=") + str(api_kalit_) + str("&action=balance")), True)
    if api_balance_:
        bot("editMessageText", Array({"chat_id": ccid_, "message_id": cmid_, "text": "<b>ðµ API Balansingizda\n" + api_balance_["balance"] + str(" ") + str(pul_) + str(" </b>"), "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "âï¸ Ortga", "callback_data": "api_sozlamalari"})))}))}))
    else:
        bot("answerCallbackQuery", Array({"callback_query_id": callid_, "text": "â ï¸ Api kalit yoki api sayt kiritilmagan!", "show_alert": True}))
    # end if
# end if
api_ = php_file_get_contents("api.txt")
if data_ == "Api_kalit" and ccid_ == admin_:
    bot("DeleteMessage", Array({"chat_id": admin_, "message_id": cmid_}))
    bot("sendMessage", Array({"chat_id": admin_, "text": str("<b>ð ") + str(api_sayt_) + str(" dan olingan api kalitni yuboring:</b>"), "parse_mode": "html", "reply_markup": php_json_encode(Array({"resize_keyboard": True, "keyboard": Array(Array(Array({"text": "ð Boshqaruv"})))}))}))
    file_put_contents("api.txt", "kalit")
# end if
if api_ == "kalit" and cid_ == admin_:
    if tx_ == "ð Boshqaruv":
        unlink("taklif.txt")
    else:
        file_put_contents("sozlamalar/api_kalit.txt", str(tx_))
        bot("sendMessage", Array({"chat_id": admin_, "text": "<b>Muvaffaqiyatli o'zgartirildi!</b>", "parse_mode": "html", "reply_markup": asosiy_soz_}))
        unlink("api.txt")
    # end if
# end if
if data_ == "Api_sayt" and ccid_ == admin_:
    bot("DeleteMessage", Array({"chat_id": admin_, "message_id": cmid_}))
    bot("sendMessage", Array({"chat_id": admin_, "text": "<b>ð Api olinadigan saytni yuboring:\nNamuna</b> <code>Topsmm.uz</code>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"resize_keyboard": True, "keyboard": Array(Array(Array({"text": "ð Boshqaruv"})))}))}))
    file_put_contents("api.txt", "sayt")
# end if
if api_ == "sayt" and cid_ == admin_:
    if tx_ == "ð Boshqaruv":
        unlink("taklif.txt")
    else:
        file_put_contents("sozlamalar/api_sayt.txt", str(tx_))
        bot("sendMessage", Array({"chat_id": admin_, "text": "<b>Muvaffaqiyatli o'zgartirildi!</b>", "parse_mode": "html", "reply_markup": asosiy_soz_}))
        unlink("api.txt")
    # end if
# end if
if data_ == "api_sozlamalari" and ccid_ == admin_:
    bot("deleteMessage", Array({"chat_id": admin_, "message_id": cmid_}))
    bot("sendMessage", Array({"chat_id": admin_, "text": "<b>ð Api sozlash bo'limidasiz:</b>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "ð Hozirgi holati", "callback_data": "api_holati"})), Array(Array({"text": "ð Api kalit", "callback_data": "Api_kalit"}), Array({"text": "ð Api sayt", "callback_data": "Api_sayt"})), Array(Array({"text": "ðµ Api hisob", "callback_data": "Api_hisob"})))}))}))
# end if
bolim_ = php_file_get_contents("sozlamalar/xizmat/kategoriya.txt")
if data_ == "xizochir":
    bolim_ = php_file_get_contents("sozlamalar/xizmat/kategoriya.txt")
    more_ = php_explode("\n", bolim_)
    soni_ = php_substr_count(bolim_, "\n")
    keys_ = Array()
    for_ = 1
    while for_ <= soni_:
        
        ichida_ = php_file_get_contents("sozlamalar/bot/" + more_[for_] + "/ichkibolim.txt")
        ta_ = php_substr_count(ichida_, "\n")
        keys_[-1] = Array({"text": str(more_[for_]) + str(" ") + str(ta_) + str("->"), "callback_data": "xizdel-" + more_[for_]})
        keysboard2_ = array_chunk(keys_, byson_)
        keysboard2_[-1] = Array(Array({"text": "âï¸ Orqaga", "callback_data": "xizmat"}))
        key_ = php_json_encode(Array({"inline_keyboard": keysboard2_}))
        for_ += 1
    # end while
    if bolim_ != None:
        bot("editMessageText", Array({"chat_id": ccid_, "message_id": cmid_, "text": "<b>Quyidagilardan birini tanlang:</b>", "parse_mode": "html", "reply_markup": key_}))
    else:
        bot("answerCallbackQuery", Array({"callback_query_id": callid_, "text": "ð Bo'limlar mavjud emas!", "show_alert": True}))
    # end if
# end if
if php_mb_stripos(data_, "xizdel-") != False:
    ex_ = php_explode("-", data_)
    kat_ = ex_[1]
    royxat_ = php_file_get_contents(str("sozlamalar/bot/") + str(kat_) + str("/ichkibolim.txt"))
    file_put_contents(str("step/") + str(ccid_) + str(".bol"), str(kat_))
    more_ = php_explode("\n", royxat_)
    soni_ = php_substr_count(royxat_, "\n")
    keys_ = Array()
    for_ = 1
    while for_ <= soni_:
        
        ichida_ = php_file_get_contents(str("sozlamalar/bot/") + str(kat_) + str("/") + more_[for_] + "/xizmatbolim.txt")
        ta_ = php_substr_count(ichida_, "\n")
        keys_[-1] = Array({"text": str(more_[for_]) + str(" ") + str(ta_) + str("->"), "callback_data": "delochir-" + more_[for_]})
        keysboard2_ = array_chunk(keys_, ibyson_)
        keysboard2_[-1] = Array(Array({"text": "âï¸ Orqaga", "callback_data": "xizochir"}))
        key_ = php_json_encode(Array({"inline_keyboard": keysboard2_}))
        for_ += 1
    # end while
    if royxat_ != None:
        bot("editMessageText", Array({"chat_id": ccid_, "message_id": cmid_, "text": "<b>Quyidagilardan birini tanlang:</b>", "parse_mode": "html", "reply_markup": key_}))
    else:
        bot("answerCallbackQuery", Array({"callback_query_id": callid_, "text": "ð Ichki bo'limlar mavjud emas!", "show_alert": True}))
    # end if
# end if
if php_mb_stripos(data_, "delochir-") != False:
    ex_ = php_explode("-", data_)
    roy_ = ex_[1]
    kat_ = php_file_get_contents(str("step/") + str(ccid_) + str(".bol"))
    file_put_contents(str("step/") + str(ccid_) + str(".ich"), str(roy_))
    royxat_ = php_file_get_contents(str("sozlamalar/bot/") + str(kat_) + str("/") + str(roy_) + str("/xizmatbolim.txt"))
    ids_ = php_explode("\n", royxat_)
    soni_ = php_substr_count(royxat_, "\n")
    for id_ in ids_:
        key_ = Array()
        text_ = ""
        for_ = 1
        while for_ <= soni_:
            
            text_ += str("<b>") + str(for_) + str("</b> ") + ids_[for_] + "\n"
            key_[-1] = Array({"text": str(for_), "callback_data": "deletexiz-" + ids_[for_]})
            for_ += 1
        # end while
        keysboard2_ = array_chunk(key_, xizson_)
        keysboard2_[-1] = Array(Array({"text": "âï¸ Orqaga", "callback_data": str("xizdel-") + str(kat_)}))
        key_ = php_json_encode(Array({"inline_keyboard": keysboard2_}))
    # end for
    if royxat_ != None:
        bot("editMessageText", Array({"chat_id": ccid_, "message_id": cmid_, "text": str("ð <b>O'chiriladigan xizmatni tanlang:</b>\n\n") + str(text_), "parse_mode": "html", "reply_markup": key_}))
    else:
        bot("answerCallbackQuery", Array({"callback_query_id": callid_, "text": "ð Ichki bo'limlar mavjud emas!", "show_alert": True}))
    # end if
# end if
if php_mb_stripos(data_, "deletexiz-") != False:
    ex_ = php_explode("-", data_)
    xiz_ = ex_[1]
    roy_ = php_file_get_contents(str("step/") + str(ccid_) + str(".ich"))
    kat_ = php_file_get_contents(str("step/") + str(ccid_) + str(".bol"))
    royxat_ = php_file_get_contents(str("sozlamalar/bot/") + str(kat_) + str("/") + str(roy_) + str("/xizmatbolim.txt"))
    k_ = php_str_replace("\n" + xiz_ + "", "", royxat_)
    file_put_contents(str("sozlamalar/bot/") + str(kat_) + str("/") + str(roy_) + str("/xizmatbolim.txt"), k_)
    bot("deleteMessage", Array({"chat_id": ccid_, "message_id": cmid_}))
    bot("sendMessage", Array({"chat_id": ccid_, "text": str("<b>") + str(xiz_) + str(" - nomli xizmat o'chirildi</b>"), "parse_mode": "html", "reply_markup": admin1_menu_}))
    deleteFolder(str("sozlamalar/xizmatlar/") + str(kat_) + str("/") + str(roy_) + str("/") + str(xiz_))
# end if
adminuser_ = php_file_get_contents("admin.user")
if tx_ == "*â£ Birlamchi sozlamalar" and cid_ == admin_:
    bot("sendMessage", Array({"chat_id": cid_, "text": "<b>ð Quyidagilardan birini tanlang:</b>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"inline_keyboard": Array(Array(Array({"text": "ð Hozirgi holat", "callback_data": "hholat"})), Array(Array({"text": "ð Taklif narxi", "callback_data": "taklif_narxi"}), Array({"text": "ð¶ Valyuta nomi", "callback_data": "valyuta_nomi"})), Array(Array({"text": "ð¨âð» Admin useri", "callback_data": "adminuser"}), Array({"text": "âï¸ Foiz qoÊ»yish", "callback_data": "foizqoy"})))}))}))
# end if
#// Tarqatgan kot mehnatimni qadrlela @muzadev & @education_coders
#// Tarqatgan kot mehnatimni qadrlela @muzadev & @education_coders
if data_ == "hholat":
    bot("deleteMessage", Array({"chat_id": admin_, "message_id": cmid_}))
    bot("sendMessage", Array({"chat_id": ccid_, "text": str("<b>ð \n\nð Taklif narxi - ") + str(taklifpul_) + str("\nð¶ Valyuta nomi - ") + str(pul_) + str("\n\nð¨âð» Admin useri - ") + str(adminuser_) + str("\n\nð Reklama kanali - ") + str(rekkanal_) + str("\nð Reklama narxi - ") + str(reknarx_) + str("</b>"), "parse_mode": "html", "reply_markup": php_json_encode(Array({"resize_keyboard": True, "keyboard": Array(Array(Array({"text": "ð Boshqaruv"}), Array({"text": "âï¸ Orqaga"})))}))}))
    sys.exit(0)
# end if
if data_ == "adminuser":
    bot("deleteMessage", Array({"chat_id": admin_, "message_id": cmid_}))
    bot("sendMessage", Array({"chat_id": ccid_, "text": "<b>ð Yangi admin userini yuboring:</b>", "parse_mode": "html", "reply_markup": php_json_encode(Array({"resize_keyboard": True, "keyboard": Array(Array(Array({"text": "ð Boshqaruv"})))}))}))
    file_put_contents(str("step/") + str(ccid_) + str(".txt"), "adminuser")
    sys.exit(0)
# end if
#// Tarqatgan kot mehnatimni qadrlela @muzadev & @education_coders
#// Tarqatgan kot mehnatimni qadrlela @muzadev & @education_coders
if userstep_ == "adminuser":
    if tx_ == "ð Boshqaruv":
        unlink(str("step/") + str(cid_) + str(".txt"))
    else:
        if cid_ == admin_:
            if (php_isset(lambda : text_)):
                adminuser_ = php_file_get_contents("admin.user")
                file_put_contents("admin.user", str(text_))
                bot("SendMessage", Array({"chat_id": cid_, "text": "<b>Qabul qilidim</b>", "parse_mode": "html", "reply_markup": admin1_menu_}))
            # end if
            unlink(str("step/") + str(cid_) + str(".txt"))
        # end if
    # end if
# end if
pass
