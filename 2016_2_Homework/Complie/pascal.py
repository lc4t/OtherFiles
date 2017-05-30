#! /usr/bin/python3
#-*- coding: utf-8 -*-
import argparse
import re
import os
from data import symbol_to_sort_map, max_length_symbol
import logging
from colorlog import ColoredFormatter

logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = ColoredFormatter(
    "%(log_color)s%(levelname)-8s %(message)s",
    datefmt=None,
    reset=True,
    log_colors={
    'DEBUG': 'cyan',
    'INFO': 'green',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'red,bg_white',
},
secondary_log_colors={},
style='%'
)
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)


class SymbolTable:
    def __init__(self):
        self.symbol = {}

    def create(self, symbol):
        if symbol not in self.symbol:
            self.symbol[symbol] = {}

class LexicalAnalysis:
    def __init__(self, filename):
        '''
        二元式:
            单词符号[space]种别
            16     1      2
        '''
        self.filename = filename + '.dyd'
        self.errorfile = filename + '.err'


    @classmethod
    def is_const(cls, symbol):
        if re.match('^\d+$', symbol):
            return True


    def error(self, text):
        open(self.errorfile, 'a').write(text)

    def is_identify(self, symbol, line=0):
        if symbol in symbol_to_sort_map:
            return False
        elif re.match('^[a-zA-Z_]+[a-zA-Z0-9_]*$', symbol):
            if len(str(symbol)) <= 16:
                return True
            else:
                e = '***LINE:%02d  overlength symbol "%s"' % (line, symbol)
                errorMsg = 'LexicalAnalysis.is_identify(1): %s' % e
                logger.error(errorMsg)
                self.error(e)
                return None
        else:
            return False


    def write(self, symbol, sort):
        text = '%16s %02d' % (symbol, sort)
        logger.debug('LexicalAnalysis.write: %s' % text)
        open(self.filename, 'a').write(text + '\n')


    def writeEOLN(self):
        text = '%16s %02d' % ('EOLN', 24)
        logger.debug('LexicalAnalysis.writeEOLN: %s' % text)
        open(self.filename, 'a').write(text + '\n')


    def writeEOF(self):
        text = '%16s %02d' % ('EOF', 24)
        logger.debug('LexicalAnalysis.writeEOF: %s' % text)
        open(self.filename, 'a').write(text + '\n')


    def do(self, source_code, line=1):
        # _ = re.findall('<\s+=', source_code)
        # for i in _:
        #     source_code = source_code.replace(i, '<=')
        # _ = re.findall('<\s+>', source_code)
        # for i in _:
        #     source_code = source_code.replace(i, '<>')
        # _ = re.findall('>\s+=', source_code)
        # for i in _:
        #     source_code = source_code.replace(i, '>=')
        # _ = re.findall(':\s+=', source_code)
        # for i in _:
        #     source_code = source_code.replace(i, ':=')
        source_code_split = source_code.replace('\n', ' \n ').split(' ')
        for k in source_code_split:
            if k == '\n':
                line += 1
                self.writeEOLN()
                continue
            if k == '':
                continue
            try:
                code, token = self.check_defines(k, line)
            except TypeError:
                continue
            # if code is None:
                # continue
            self.write(code, token)
            if len(code) < len(k):
                self.do(k[len(code):], line)


    def check_defines(self, code, line=0):
        l = len(code)
        for i in range(max_length_symbol, 0, -1):
            if code[0:i] in symbol_to_sort_map:
                return (code[0:i], symbol_to_sort_map.get(code[0:i]))
        if self.is_const(code):
            return (code, 11)
        if self.is_identify(code, line=line) is None:
            return None
        elif self.is_identify(code, line=line):
            return (code, 10)
        else:
            pass
        if l > 1:
            return self.check_defines(code[0:-1], line)
        else:
            criticalMsg = '***LINE:%02d  invalid symbol "%s"' % (line, code)
            logger.critical('LexicalAnalysis.do(1): %s' % criticalMsg)
            self.error(criticalMsg + '\n')
            # exit(0)
            # return (-1, -1)

class Var:
    def __init__(self):

        self.vname = ''  # 变量名
        self.vproc = '' # 所属过程
        self.vkind = -1  # 分类 0变量 1形参
        self.vtype = int # 变量类型
        self.vlev = -1   # 变量层次
        self.vadr = 0  # 变量在变量表中的位置 相对第一个变量而言

class Pro:
    def __init__(self):

        self.pname = ''  # 过程名
        self.ptype = int # 过程类型
        self.plev = 0   # 过程层次
        self.varNum = 0 # 变量数量
        self.fadr = 0   # 第一个变量位置
        self.ladr = 0   # 最后一个变量位置
        self.parameter = -1
        self.parameterIsDefined = False

class GrammarAnalysis:
    def __init__(self, filename):
        '''
        '''
        self.filename = filename + '.dyd'
        self.dysfilename = filename + '.dys'
        self.errorfile = filename + '.err'
        self.varfile = filename + '.var'
        self.profile = filename + '.pro'
        self.line = 1
        self.token_index = 0
        self.var = []
        self.pro = []
        self.currentVar = Var()
        self.currentPro = Pro()
        self.char_index = 0
        self.error_cnt = 0
        pass

    def init(self):
        logger.debug('GrammarAnalysis.init(1)')
        logger.info('GrammarAnalysis.init(2): read file %s' % self.filename)
        os.system('cp %s %s' % (self.filename, self.dysfilename))
        self.tokens = open(self.filename, 'r').readlines()

    def check(self, currentVar=None):
        print('total error: %d ' % self.error_cnt)
        print('----')
        # print('list is:')
        # for i in range(0, len(self.tokens), 1):
        #     print('<%d>%s' % (i, self.tokens[i]), end='')
        print('now read:')
        print(self.token_index, self.tokens[self.token_index])
        print('var[]:')
        for i in self.var:
            print('vname=%s, vproc=%s, vkind=%d, vlev=%d, vadr=%d' % (i.vname, i.vproc, i.vkind, i.vlev, i.vadr))
        print('pro[]:')
        for i in self.pro:
            print('pname=%s, ptype=%s, plev=%d, varNum=%d, fadr=%d, ladr=%d, parameter=%d, parameterIsDefined=%s' % (i.pname, i.ptype, i.plev, i.varNum, i.fadr, i.ladr, i.parameter, i.parameterIsDefined))

        if currentVar is not None:
            print('currentVar')
            i = currentVar
            print('vname=%s, vproc=%s, vkind=%d, vlev=%d, vadr=%d' % (i.vname, i.vproc, i.vkind, i.vlev, i.vadr))
        print('currentPro:')
        i = self.currentPro
        print('pname=%s, ptype=%s, plev=%d, varNum=%d, fadr=%d, ladr=%d, parameter=%d, parameterIsDefined=%s' % (i.pname, i.ptype, i.plev, i.varNum, i.fadr, i.ladr, i.parameter, i.parameterIsDefined))
        print('----')
    def get_token(self, index=-1, code=False, change=True):
        if index == -1:
            index = self.token_index

        d = ''.join(self.tokens[index].strip('\n')[0:16].split())
        c = int(''.join(self.tokens[index].strip('\n')[17:19].split()))
        if d == 'EOLN':
            logger.info('get EOLN')

            if change:
                self.line += 1
                logger.info('now line is %d, ->%s %d' % (self.line, d, c))
                self.set_token_offset(1)
            return self.get_token(index+1)
        # logger.debug('-> %s' % d)
        if code:
            return c
        else:
            return d


    def set_token_offset(self, offset=0, absolute=0):
        self.char_index = 0
        if offset != 0:
            logger.debug('GrammarAnalysis.set_token_offset(1): get next %d' % offset)
            self.token_index += offset
        elif absolute != 0:
            logger.debug('GrammarAnalysis.set_token_offset(1): turn to %d' % absolute)
            self.token_index = absolute
        else:
            pass
        logger.info('now token offset is %d' % self.token_index)

    def error(self, text):
        logger.error(text)
        open(self.errorfile, 'a').write(text + '\n')
        self.error_cnt += 1


    def do(self):
        self.init()
        logger.debug('GrammarAnalysis.do(1)')
        self.A()
        self.check()
        self.writeVar()
        self.writePro()

    def writeVar(self):
        line = '%16s %16s %1d %s %d %d\n'
        for i in self.var:
            if i.vtype == int:
                types = 'integer'
            else:
                types = ''
            open(self.varfile, 'a').write(line % (i.vname, i.vproc,  i.vkind, types, i.vlev, i.vadr))

    def writePro(self):
        line = '%16s %s %d %d %d\n'
        for i in self.pro:
            if i.ptype == int:
                types = 'integer'
            else:
                types = ''
            open(self.profile, 'a').write(line % (i.pname, types, i.plev, i.fadr, i.ladr))


    def A(self):
        logger.debug('GrammarAnalysis.A(1)')
        self.B()


    def B(self):
        logger.debug('GrammarAnalysis.B(1)')

        if self.get_token() == 'begin':
            logger.debug('GrammarAnalysis.B(2): get <begin>')
            self.set_token_offset(offset=1)
        else:
            self.error('***LINE:%02d  No Symbol "%s"' % (self.line, 'begin'))
            if self.get_token() != 'integer':
                self.set_token_offset(1)
        self.C()
        if self.get_token() == ';':
            logger.debug('GrammarAnalysis.B(3): get <;>')
            self.set_token_offset(1)
        else:
            self.error('***LINE:%02d  No Symbol "%s"' % (self.line, ';'))
            if self.get_token() != 'integer' and self.get_token() != 'read' and self.get_token() != 'write' and self.get_token(code=True) != 10:
                self.set_token_offset(1)
        self.M()
        if self.get_token() == 'end':
            logger.debug('GrammarAnalysis.B(4): get <end>')
            self.set_token_offset(1)
        else:
            self.error('***LINE:%02d  No Symbol "%s"' % (self.line, 'end'))


    def C(self):
        logger.debug('GrammarAnalysis.C(1)')

        self.D()
        self.C_()


    def C_(self):
        logger.debug('GrammarAnalysis.C_(1)')

        self.get_token()
        if self.get_token() == ';' and self.get_token(self.token_index + 1, change=False) == 'integer':
            logger.info('GrammarAnalysis.C(1): get ";" and next is "integer"')
            self.set_token_offset(1)
            self.D()
            self.C_()
        else:
            if self.get_token() == 'integer':
                logger.info('GrammarAnalysis.C(1): get "integer"')
                self.error('***LINE:%02d  No Symbol "%s"' % (self.line, ';'))
                self.D()
                self.C_()


    def D(self):
        logger.debug('GrammarAnalysis.D(1)')
        self.get_token()
        if self.get_token(self.token_index + 1, change=False) == 'function':
            logger.info('GrammarAnalysis.D(2): next is "function"')
            self.J()
        else:
            logger.info('GrammarAnalysis.D(3): next is %s NOT "function"' % self.get_token())
            self.E()

    def is_var_exists(self, vname, vproc, vkind):
        for i in self.var:
            logger.info('GrammarAnalysis.is_var_exists(1): check this <%s, %s, %s> == <%s, %s, %s>' % (vname, vproc, vkind, i.vname, i.vproc, i.vkind))
            if i.vname == vname and i.vproc == vproc and i.vkind == vkind:
                return True

        for i in self.pro:
            logger.info('GrammarAnalysis.is_var_exists(1): check this <%s> == <%s>' % (vname, i.pname))
            if i.pname == vname:
                return True
        if vproc != '':
            return self.is_var_exists(vname, '', vkind)
        else:
            return False

    def is_pro_exists(self, vname):
        for i in self.var:
            if vname == i.vname:
                return True
        for i in self.pro:
            if vname == i.pname:
                return True
        return False


    def E(self):
        logger.debug('GrammarAnalysis.E(1)')
        currentVar = Var()

        if self.get_token() == 'integer':
            logger.info('GrammarAnalysis.E(2): get "%s"' % self.get_token())
            self.set_token_offset(1)
        else:
            self.error('***LINE:%02d  No Symbol "%s"' % (self.line, 'integer'))
            self.set_token_offset(1)

        currentVar.vname = self.get_token()
        currentVar.vproc = self.currentPro.pname
        # if self.token_index == self.currentPro.parameter:
        if currentVar.vproc != '':
            currentVar.vkind = 1
            self.currentPro.parameterIsDefined = 1
        else:
            currentVar.vkind = 0
        currentVar.vtype = int
        currentVar.vlev = self.currentPro.plev
        currentVar.vadr = len(self.var)

        if self.is_var_exists(self.get_token(), self.currentPro.pname, currentVar.vkind):
            self.error('***LINE:%02d  Redifine var "%s"' % (self.line, self.get_token()))
        else:
            if self.currentPro.varNum == 0:
                self.currentPro.fadr = currentVar.vadr
            self.currentPro.ladr = currentVar.vadr
            self.currentPro.varNum += 1
            self.var.append(currentVar)

        self.F();


    def F(self):
        logger.debug('GrammarAnalysis.F(1)')
        self.G()


    def G(self):
        logger.debug('GrammarAnalysis.G(1)')
        if self.get_token(code=True) == 10:
            logger.info('GrammarAnalysis.G(2): get const "%s"' % self.get_token())
            self.set_token_offset(1)


    def J(self):
        logger.debug('GrammarAnalysis.J(1)')

        pro_bak = self.currentPro

        if self.get_token() == 'integer':
            self.set_token_offset(1)
        else:
            self.error('***LINE:%02d  No Symbol "%s"' % (self.line, 'integer'))
            if self.get_token() != 'function':
                self.set_token_offset(1)
        if self.get_token() == 'function':
            self.set_token_offset(1)
        else:
            self.error('***LINE:%02d  No Symbol "%s"' % (self.line, 'function'))
            if self.get_token(code=True) != 10:
                self.set_token_offset(1)

        self.currentPro.pname = self.get_token()
        self.currentPro.ptype = int
        self.currentPro.plev += 1
        self.currentPro.varNum = 0
        self.currentPro.parameterIsDefined = False

        if self.is_pro_exists(self.get_token()):
            self.error('***LINE:%02d  Redefine "%s"' % (self.line, self.get_token()))

        self.G()

        if self.get_token() == '(':
            self.set_token_offset(1)
        else:
            self.error('***LINE:%02d  No Symbol "%s"' % (self.line, '('))
            if self.get_token(code=True) != 10:
                self.set_token_offset(1)


        self.currentPro.parameter = self.token_index
        self.K()

        if self.get_token() == ')':
            self.set_token_offset(1)
        else:
            self.error('***LINE:%02d  No Symbol "%s"' % (self.line, ')'))
            if self.get_token() != ';':
                self.set_token_offset(1)

        if self.get_token() == ';':
            self.set_token_offset(1)
        else:
            self.error('***LINE:%02d  No Symbol "%s"' % (self.line, ';'))
            if self.get_token() != 'begin':
                self.set_token_offset(1)

        self.L()

        self.currentPro = pro_bak


    def K(self):
        logger.debug('GrammarAnalysis.K(1)')

        self.F()


    def L(self):
        logger.debug('GrammarAnalysis.L(1)')

        if self.get_token() == 'begin':
            self.set_token_offset(1)
        else:
            self.error('***LINE:%02d  No Symbol "%s"' % (self.line, 'begin'))
            if self.get_token() != 'integer':
                self.set_token_offset(1)

        self.C()
        if not self.currentPro.parameterIsDefined:
            self.error('***LINE:%02d  No Para "%s"' % (self.line, self.get_token()))

        _ = self.currentPro
        self.pro.append(_)
        if self.get_token() == ';':
            self.set_token_offset(1)
        else:
            self.error('***LINE:%02d  No Symbol "%s"' % (self.line, ';'))
            if self.get_token() != 'integer' and self.get_token() != 'read' and self.get_token() != 'write' and self.get_token(code=True) != 10:
                self.set_token_offset(1)

        self.M()
        if self.get_token() == 'end':
            self.set_token_offset(1)
        else:
            self.error('***LINE:%02d  No Symbol "%s"' % (self.line, 'end'))
            if self.get_token() != ';' and self.get_token() != 'end':
                self.set_token_offset(1)

    def M(self):
        logger.debug('GrammarAnalysis.M(1)')

        self.N()
        self.M_()


    def M_(self):
        logger.debug('GrammarAnalysis.M_(1)')

        if self.get_token() == ';':
            logger.info('GrammarAnalysis.M_(2): get "%s"' % self.get_token())
            self.set_token_offset(1)
            self.N()
            self.M_()
        else:
            if self.get_token() != 'end' and self.get_token() != 'EOF':
                logger.info('GrammarAnalysis.M_(3): get "%s"' % self.get_token())
                self.error('***LINE:%02d  No Symbol "%s"' % (self.line, ';'))
                self.N()
                self.M_()


    def N(self):
        logger.debug('GrammarAnalysis.N(1)')

        logger.info('GrammarAnalysis.N(2): get "%s"' % self.get_token())
        if self.get_token() == 'read':
            self.O()
        elif self.get_token() == 'write':
            self.P()
        elif self.get_token() == 'if':
            self.W()
        elif self.get_token(code=True) == 10:
            logger.info('GrammarAnalysis.N(2): get const "%s"' % self.get_token())
            self.Q()
        else:
            self.error('***LINE:%02d  Symbol exec error "%s"' % (self.line, self.get_token()))
            self.set_token_offset(1)

    def O(self):
        logger.debug('GrammarAnalysis.O(1)')

        if self.get_token() == 'read':
            self.set_token_offset(1)
        else:
            self.error('***LINE:%02d  No Symbol "%s"' % (self.line, ';'))
            if self.get_token() != '(':
                self.set_token_offset(1)

        if self.get_token() == '(':
            self.set_token_offset(1)
        else:
            self.error('***LINE:%02d  No Symbol "%s"' % (self.line, '('))
            if self.get_token(code=True) != 10:
                self.set_token_offset(1)

        if not self.is_var_exists(self.get_token(), self.currentPro.pname, False) and not self.is_var_exists(self.get_token(), self.currentPro.pname, True):
            self.error('***LINE:%02d  Undefined Symbol "%s"' % (self.line, self.get_token()))
        self.F()
        if self.get_token() == ')':
            self.set_token_offset(1)
        else:
            self.error('***LINE:%02d  No Symbol "%s"' % (self.line, ')'))
            if self.get_token() != ';' and self.get_token() != 'end':
                self.set_token_offset()

    def P(self):
        logger.debug('GrammarAnalysis.P(1)')

        if self.get_token() == 'write':
            self.set_token_offset(1)
        else:
            self.error('***LINE:%02d  No Symbol "%s"' % (self.line, 'write'))
            if self.get_token() != '(':
                self.set_token_offset(1)
        if self.get_token() == '(':
            self.set_token_offset(1)
        else:
            self.error('***LINE:%02d  No Symbol "%s"' % (self.line, ')'))
            if self.get_token(code=True) != 10:
                self.set_token_offset(1)

        if not self.is_var_exists(self.get_token(), self.currentPro.pname, False) and not self.is_var_exists(self.get_token(), self.currentPro.pname, True):
            self.error('***LINE:%02d  Undefined Symbol "%s"' % (self.line, self.get_token()))

        self.F()
        if self.get_token() == ')':
            self.set_token_offset(1)
        else:
            self.error('***LINE:%02d  No Symbol "%s"' % (self.line, ')'))
            if self.get_token() != ';' and self.get_token() != 'end':
                self.set_token_offset(1)

    def Q(self):
        logger.debug('GrammarAnalysis.Q(1)')

        if not self.is_var_exists(self.get_token(), self.currentPro.pname, False) and not self.is_var_exists(self.get_token(), self.currentPro.pname, True):
            logger.info('GrammarAnalysis.Q(2): get "%s"' % self.get_token())
            self.error('***LINE:%02d  Undefined Symbol "%s"' % (self.line, self.get_token()))

        self.F()
        if self.get_token() == ':=':

            self.set_token_offset(1)
        else:
            self.error('***LINE:%02d  No Symbol "%s"' % (self.line, ':='))
            if self.get_token(code=True) != 10 and self.get_token(code=True) != 11:
                self.set_token_offset(1)
        self.R()

    def R(self):
        logger.debug('GrammarAnalysis.R(1)')

        self.S()
        self.R_()


    def R_(self):
        logger.debug('GrammarAnalysis.R_(1)')

        if self.get_token() == '-':
            logger.info('GrammarAnalysis.R_(2): get "%s"' % self.get_token())
            self.set_token_offset(1)
            self.S()
            self.R_()
        else:
            if self.get_token(code=True) == 10 or self.get_token(code=True) == 11:
                logger.info('GrammarAnalysis.R_(3): get const "%s"' % self.get_token())
                self.S()
                self.R_()


    def S(self):
        logger.debug('GrammarAnalysis.S(1)')
        self.T()
        self.S_()


    def S_(self):
        logger.debug('GrammarAnalysis.S_(1)')

        if self.get_token() == '*':
            logger.info('GrammarAnalysis.S_(2): get const "*"')
            self.set_token_offset(1)
            self.T()
            self.S_()
        else:
            if self.get_token(code=True) == 10 or self.get_token(code=True) == 11:
                logger.info('GrammarAnalysis.S_(3): get const "%s"' % self.get_token())
                self.T()
                self.S_()

    def T(self):
        logger.debug('GrammarAnalysis.T(1)')

        if ord('0') <= ord(self.get_token()[self.char_index]) <= ord('9'):
            logger.info('GrammarAnalysis.T(2): get const "%s"' % self.get_token())
            self.U()
        elif self.get_token(self.token_index + 1, change=False) == '(':
            logger.info('GrammarAnalysis.T(3): get "("')
            self.Z()
        else:
            if not self.is_var_exists(self.get_token(), self.currentPro.pname, False) and not self.is_var_exists(self.get_token(), self.currentPro.pname, True):
                self.error('***LINE:%02d  Undefined Symbol "%s"' % (self.line, self.get_token()))
            self.F()

    def U(self):
        logger.debug('GrammarAnalysis.U(1)')
        if self.get_token(code=True) == 11:
            self.set_token_offset(1)


    def W(self):
        logger.debug('GrammarAnalysis.W(1)')
        if self.get_token() == 'if':
            self.set_token_offset(1)
        else:
            self.error('***LINE:%02d  No Symbol "%s"' % (self.line, 'if'))
            if self.get_token(code=True) != 10 and self.get_token(code=True) != 11:
                self.set_token_offset(1)
        self.X()

        if self.get_token() == 'then':
            self.set_token_offset(1)
        else:
            self.error('***LINE:%02d  No Symbol "%s"' % (self.line, 'then'))
            if self.get_token() != 'integer' and self.get_token() != 'read' and self.get_token() != 'write' and self.get_token(code=True) != 10:
                self.set_token_offset(1)
        self.N()
        if self.get_token() == 'else':
            self.set_token_offset(1)
        else:
            self.error('***LINE:%02d  No Symbol "%s"' % (self.line, 'else'))
            if self.get_token() != 'integer' and self.get_token() != 'read' and self.get_token() != 'write' and self.get_token(code=True) != 10:
                self.set_token_offset(1)
        self.N()


    def X(self):
        logger.debug('GrammarAnalysis.X(1)')
        self.R()
        self.Y()
        self.R()


    def Y(self):
        logger.debug('GrammarAnalysis.Y(1)')
        if self.get_token() == '<' or self.get_token() == '<=' or self.get_token() == '>' or self.get_token() == '>=' or self.get_token() == '=' or self.get_token() == '<>':
            self.set_token_offset(1)
        else:
            self.error('***LINE:%02d  No Symbol "%s"' % (self.line, 'compair symbol'))
            if self.get_token(code=True) != 10 and self.get_token(code=True) != 11:
                self.set_token_offset(1)


    def Z(self):
        logger.debug('GrammarAnalysis.Z(1)')
        if not self.is_pro_exists(self.get_token()):
            self.error('***LINE:%02d  Undefined Symbol "%s"' % (self.line, self.get_token()))
        self.G()
        if self.get_token() == '(':
            logger.info('GrammarAnalysis.Z(2): get "("')
            self.set_token_offset(1)
        else:
            self.error('***LINE:%02d  No Symbol "%s"' % (self.line, '('))
            if self.get_token(code=True) != 10 and self.get_token(code) != 11:
                logger.info('GrammarAnalysis.Z(3): get "%s"' % self.get_token())
                self.set_token_offset(1)
        self.R()
        if self.get_token() == ')':
            logger.info('GrammarAnalysis.Z(4): get "%s"' % self.get_token())
            self.currentPro = Pro()

            self.set_token_offset(1)
        else:
            logger.info('GrammarAnalysis.Z(5): get "%s"' % self.get_token())
            self.error('***LINE:%02d  No Symbol "%s"' % (self.line, ')'))
            if self.get_token() != '-' and self.get_token() != '*' and self.get_token() != ';' and self.get_token() != 'end':
                self.set_token_offset(1)


class ReadFile:
    def __init__(self, input_file):
        self.input_file = input_file
        try:
            source_lines = open(input_file, 'r').readlines()
        except FileNotFoundError as e:
            logger.error('FileNotFound: %s' % input_file)
            exit(0)
        self.source_code = ''.join(source_lines)
    def get_source_code(self):
        return self.source_code


if __name__ == '__main__':
    # a = LexicalAnalysis('test')
    # a.write('begin', 1)
    parser = argparse.ArgumentParser(description='little exp')
    parser.add_argument('-f', '--file', help='source code file')
    parser.add_argument('-c', '--clean', help='clean mid code', action='store_true')
    parser.add_argument('-l', '--lexical', help='LexicalAnalysis', action='store_true')
    parser.add_argument('-g', '--grammer', help='GrammarAnalysis', action='store_true')

    #
    source_code = ''
    args = parser.parse_args()
    if args.clean:
        logger.info('main: delete files')
        os.system('rm -f *.dyd *.err *.var *.pro *.dys')
    elif args.file is None:
        parser.print_help()
    else:
        logger.info('Read file from %s' % args.file)
        source_code = ReadFile(args.file).get_source_code()
        if args.lexical:
            la = LexicalAnalysis('.'.join(args.file.split('.')[:-1]))
            la.do(source_code)
            la.writeEOF()
        if args.grammer:
            ga = GrammarAnalysis('.'.join(args.file.split('.')[:-1]))
            ga.do()
