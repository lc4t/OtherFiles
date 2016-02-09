#-*-coding:utf-8-*-
__author__='lc4t'
import base64

def fourChar(seq, encoding = 'utf-8'):
    encoding = encoding.lower()
    for a in [seq[0].lower(), seq[0].upper()]:
        for b in [seq[1].lower(), seq[1].upper()]:
            for c in [seq[2].lower(), seq[2].upper()]:
                for d in [seq[3].lower(), seq[3].upper()]:
                    string = a + b + c + d
                    try:
                        ans = base64.b64decode(string).decode(encoding)
                        if (encoding == 'utf-8'):
                            for i in ans:
                                assert 32 <= ord(i) <= 126
                        return ans
                    except Exception as e:
                        pass

def main():
    IN = input('input string:')
    
    ans = ''
    for seqID in range(0, len(IN), 4):
        seq = IN[seqID:seqID+4]
        req = fourChar(seq)
        if req != None:
            ans += req
        else:
            print ('None @', seqID) 
    print (ans)


if __name__ == '__main__':
    main()
