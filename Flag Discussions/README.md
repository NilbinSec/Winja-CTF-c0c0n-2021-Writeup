# Flag Discussion

This section contains all of the flags we found during the CTF with an associated discussion of how we solved them.

# Believe With You Eyes
**Point Value:** 100

**Prompt**

_patlu.winja.site_
_Look twice or thrice..._

![image](https://user-images.githubusercontent.com/85370905/141664255-ea134749-ff0e-41bd-a5a6-1c4f8d23dc30.png)

Flag: **flag{849d97fa58871dad45e81027f861739_maYB3_i_SHOULd_BELIeve-7HeM}**

**Methodology**
At first it looked like we should start by messing with contrast/color levels to pull out the flag as a form of steg. The below image found the end of the flag, but appending to the clearly visible one was no joy. 

![image](https://user-images.githubusercontent.com/85370905/141664291-44e19a18-1eed-43e8-9f8e-64ac4d40b108.png)

At this point, we transitioned to the normal image exploitation checklist and ran exiftool against the image which found this:

![image](https://user-images.githubusercontent.com/85370905/141664317-851bbcdb-1077-43f7-b73d-4d27a21aa5a9.png)

It is unclear if this was intentional on the part of the organizers because it was so trivial to find unless they were expecting people to get focused on what the picture showed.

# Find My Address
**Point Value:** 150

**Prompt**

_My vulnerable redis (3.0.6) instance is running in Gravelines. Help me find the address before its too late. Format : flag{xx.xx.xx.xx}_

Flag: **flag{149.202.183.147}**

**Methodology**
Wording was a little unusual, but operated under the hunch that Shodan would let me find a specific system in a geographic location. The search string _country:"FR" city:"Gravelines" product:"redis" version:"3.0.6"_ returned six systems in Gravelines, France running redis 3.0.6. The final system in the listing was the correct flag.

# Hardy
**Point Value:** 200

**Prompt**

_shinchan.winja.site_
_The growth of understanding follows an ascending spiral rather than a straight line_

Flag: **flag{Di77icu8tyI9now@!!#-Youdidit!!}**

**Methodology**
This was a basic puzzle for NilbinSec due to our ARG focus and would probably be better classified as a 100 point flag for us personally. We were provided with the following string in hardy.txt (in this folder). The order of operations to find the flag was: Base58 the provided code to get morse code (dcode.fr) -> Translate the morse code to text to get binary -> Convert the binary to ASCII to get decimals -> Convert the decimals to ASCII to get the flag.

# Reciprical Cypher
**Point Value:** 100

**Prompt**

_birbal.winja.site_
_They had nothing in common but the English language._

_籯籵籪籰粄籁簾簹籫籯籂籫籬簼簼籮籪簽簹籭籯簿籯籯籮簾籭簽籁籬籯籫籁籯簹籬籮籨籮籡簼籬籾籽籲籗籂籨籒籝籨籽籠籒籌籮籨类籮簾籽簹类簼籜籨籀籑籮籨簹类簺籂籲籷籪簺籨籀籮籡籝粆_
You may need to install a language pack to render properly.

Flag: **flag{850bf9bc33ea40df6ffe5d48cfb8f0ce_eX3cutiN9_IT_tWICe_re5t0r3S_7He_0r19ina1_7eXT}**

**Methodology**
This was a rehash for us of the Saintcon 2021 pre-conference challenge. Seeing weird repeating Chinese characters now screams check for rot8000. We did and were rewarded with the flag.

![image](https://user-images.githubusercontent.com/85370905/141664584-edd273c7-47ed-4c52-8ea7-a38739acbee1.png)

# Decode Me
**Point Value:** 100

**Prompt**

_hattori.winja.site_
_There's a world of difference between truth and facts. Facts can obscure the truth._

_Zm(xhZ(3tm-NGR-rM2-dre)DRm)Yjg)xZG"YwY"Xc0"dl9\iQX\MzN\jRf*aXN*fQX*czc~zBt~M30~K_

Flag: **flag{f4dk3gkx4fb81df0aw4v_bAs364_is_Aw3s0m3}**

**Methodology**
This is just base64. Technically base64 spec says to ignore any characters that aren't in the set, so adding a bunch of unrelated characters makes it hard to recognize as base64 just by looking. CyberChef magic didn't figure this out, but Ciphey did. Check out Ciphey at: https://github.com/Ciphey/Ciphey. 

# D@e77$ep
**Point Value:** 100

**Prompt**

_tom.winja.site_
_Decode the elasticity that resides within you, to give your own flavour in a salad or any stew._

Flag: **flag{Co@de7In@sp@ec@tor1_Never_miss_out_small_details}**

**Methodology**
We start with a stock webpage for an interior decorating store. The flag was stored locally in the javascript. If you look at the code to check for correctness, there was a variable like flag or password that was initialized with urldecode("XXXX"). Copying the urldecode command into the developer console spits out the flag. OWASP ZAP allows you to not search the script manually. After the first scan, it highlighted the code as a "suspicous comment" because it contained the word "pass".

# BlogQL
**Point Value:** 300

**Prompt**

_shaktimaan.winja.site_
_We have made a secure blog posting platform for our l33t which is powered by new Tech called BlogQL. You can, now, Query blog information without any limits._

Flag: **flag{ea6a3da74909e79a8aa38005c6810893_d1d_In7r0speC7i0n_wORk_F0r_gRaPhqL}**

**Methodology**
Initially tried to log in and watched the network tab of the developer console. Site made a request to a graphql endpoint with a login query that failed. But it also made a random call to a users query that returned the username and password. That user/pass allowed a login, and showed a private blog post. The blog post content wasn't shown though (presumably because it was private). The graphql endpoint wasn't protected so I did some introspection on the schema, found that there was a PrivateBlog type. Making a query for those records in graphql and the content was the flag.

# The Valet
**Point Value:** 300

**Prompt**

_vyom.winja.site_
_AES - Advanced Encryption Standard: It's already broken, so, you can break it too. Hint: Head over to .secret directory_

Flag: **flag{57555e23cf996b6fbcb667a1b541c52c_thE_VAl3t_H@S_bEst_$ECURi7y}**

**Methodology**
This showed a simulated Chrome browser with a bunch of useless tabs open.

![image](https://user-images.githubusercontent.com/85370905/141664770-0876b209-9c6d-4d46-99a6-e0e317b28506.png)

One of the tabs said "Nothing here, dirbuster might help". Dirbuster was not needed though, since the description of the challenge eventually added, "look for secret files/directories, try .secret". Adding .secret to the url leads to a directory with a readme, secret_key, and Login_Data files. The readme said something like "Chrome saved passwords aren't hard to decrypt when you've got the database and the secret key". Googling how to decrypt chrome passwords provides several tutorials. With the tutorial and python Login_Data was decrypted using the secret_key and the password was the flag. This tutorial was helpful: https://ohyicong.medium.com/how-to-hack-chrome-password-with-python-1bedc167be3d. The Python Script is uploaded above as valet.py. 

We were also delighted to learn we got First Blood for this flag:

![image](https://user-images.githubusercontent.com/85370905/141665908-0f8fd53b-d5cc-484b-8f8f-2ba8fdff8010.png)

