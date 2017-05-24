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
    "%(log_color)s%(levelname)-8s%(reset)s %(white)s%(message)s",
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


class LexicalAnalysis:
    def __init__(self, filename):
        '''
        二元式:
            单词符号[space]种别
            16     1      2
        '''
        self.filename = filename + '.dyd'
        self.line = 0
        pass


    @classmethod
    def is_const(cls, symbol):
        if re.match('^\d+$', symbol):
            return True


    @classmethod
    def is_identify(cls, symbol):
        if symbol in symbol_to_sort_map:
            return False
        elif re.match('^[a-zA-Z_]+[a-zA-Z0-9_]*$', symbol) and len(str(symbol)) <= 16:
            return True
        else:
            return False


    def write(self, symbol, sort):
        text = '%16s %02d' % (symbol, sort)
        logger.debug('LexicalAnalysis.write: %s' % text)
        open(self.filename, 'a').write(text + '\n')
        self.writeEOLN()


    def writeEOLN(self):
        text = '%16s %02d' % ('EOLN', 24)
        logger.debug('LexicalAnalysis.writeEOLN: %s' % text)
        open(self.filename, 'a').write(text + '\n')


    def writeEOF(self):
        text = '%16s %02d' % ('EOF', 24)
        logger.debug('LexicalAnalysis.writeEOF: %s' % text)
        open(self.filename, 'a').write(text + '\n')


    # @classmethod
    # def get_symbol_s_sort(cls, symbol):
    #     sort = -1
    #     if symbol in symbol_to_sort_map:
    #         sort = symbol_to_sort_map.get(symbol)
    #     elif LexicalAnalysis.is_identify(symbol):
    #         sort = 10
    #     elif LexicalAnalysis.is_const(symbol):
    #         sort = 11
    #     else:
    #         logger.error('unknow symbol: %s', symbol)
    #         exit(0)
    #     return sort
    def do(self, source_code):
        _ = re.findall('<\s+=', source_code)
        for i in _:
            source_code = source_code.replace(i, '<=')
        _ = re.findall('<\s+>', source_code)
        for i in _:
            source_code = source_code.replace(i, '<>')
        _ = re.findall('>\s+=', source_code)
        for i in _:
            source_code = source_code.replace(i, '>=')
        _ = re.findall(':\s+=', source_code)
        for i in _:
            source_code = source_code.replace(i, ':=')
        source_code_split = source_code.replace('\n', ' ').replace(';', ' ').split()
        # logger.debug('LexicalAnalysis.do(1): now code list is: %s' % str(source_code_split))

        for k in source_code_split:
            code, token = self.check_defines(k)
            # logger.debug('LexicalAnalysis.do(2): check %s, get-> code: %s, token: %s' % (str(k), str(code), str(token)))
            self.write(code, token)
            if len(code) < len(k):
                self.do(k[len(code):])






    def check_defines(self, code):
        l = len(code)
        for i in range(max_length_symbol, 0, -1):
            if code[0:i] in symbol_to_sort_map:
                return (code[0:i], symbol_to_sort_map.get(code[0:i]))
        if self.is_const(code):
            return (code, 11)
        if self.is_identify(code):
            return (code, 10)
        if l > 1:
            return self.check_defines(code[0:-1])
        else:
            logger.error('LexicalAnalysis.do(1): %s' % 'Error')
            return (-1, -1)

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

    #
    source_code = ''
    args = parser.parse_args()
    if args.clean:
        logger.info('main: delete all .dyd files')
        os.system('rm -f *.dyd')
    elif args.file is None:
        parser.print_help()
    else:
        logger.debug('Read file from %s' % args.file)
        source_code = ReadFile(args.file).get_source_code()
        la = LexicalAnalysis('.'.join(args.file.split('.')[:-1]))
        la.do(source_code)
        la.writeEOF()
