#-*-coding:utf-8-*-
import base64



#must begin from little
def convert4(four):
    if (four[3].islower()):#***d
        four = four[0:3] + four[3].upper()#***D
    elif (four[2].islower()):#**cD
        four = four[0:2] + four[2].upper() + four[3].lower()#**Cd
    elif (four[1].islower()):#*bCD
        four = four[0:1] + four[1].upper() + four[2:4].lower()#*Bcd
    elif (four[0].islower()):#aBCD
        four = four[0].upper() + four[1:4].lower()
    else:
        return '#'
    return four

def isOK(string):
    string = string.replace('\r\n','').replace('\r\n','').replace(' ','')
    return string.isalnum()
def decode(s):
    equle = 4 - len(s) % 4
    if (equle != 4):
        s += '=' * equle
        print 'new:' + s
    result = ''
    base = ''
    for i in range(0,len(s),4):
        now = s[i:i+4]

        try:
            ans = base64.b64decode(now)
        except:
            pass

        if isOK(ans):
            base += now
            result += ans
            continue
        else:
            while(not isOK(ans)):
                now = convert4(now)
                if (now == '#'):
                    exit('Not base64')
                ans = base64.b64decode(now)
                # print ans
        base += now
        result += ans
    print base
    print result


decode('KMGFKYIIMGQAAJERYUGCTYILQJTMDFBNDCFOTCXNGUWOTCBDJBKGZHOKYRDFYJYHGXFKIHVGELWFPKNNTCXNGUWOTCBDJBFGZFIGFFKKOWIGGCVIUIRIADAAGQJFYRGKKICTNXKKRIKYJCDUUUIRBNDCFYGEIQJXSYAPNVMNZCHVQKNPJWRXTPMEITCXNGUWOTCBDJBFLVBFMFQENCGKZVIOJYXHYCGKZAIJSVPILWDJLAVYKFNTCYLUWOTCBDJBCZHAWLOPNRCYURGXCZHAXHIMIFNIKBYKAUIZRLQRGEZGFYZWOTCCOIMCRBNDCFMQMUQRMSRTOLNOYVCIILRSXLLNMILLCGWMYDUAEOKWKQGMGVTUKMRPGSGWEKNXCFOWBUKQGMGVTUOFIKUMMZRMWPNXKQGMGVTUOHVFBZMMFDGQJUJIKFTYOSFAWMCVKUXXKJMDFDECVWCMCVKIAVGELWFPKNUFGNBGKYPMCKHFWVUAHEJAQAGXZDFKKOOKKWYGWCNAMAGBCWRVZVXZUOPLJRSAJXKUMKVXZYFKUHLMSAJXOIGKVXZSFORMSAJXKUKMCAJWYGFWIKMWNFQYFJKWKQIFVLNLDEUMXFPBTCOZQJGBVTSOV'.lower())