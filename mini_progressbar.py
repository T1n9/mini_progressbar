
import sys
import time
 
 
class ProgressBar(object):

    @staticmethod
    def backward_print(str):
        sys.stdout.write("\033[33m\r{0}".format(str))
        sys.stdout.flush()
        sys.stdout.write('\033[4A')

    @staticmethod
    def build_progress_bar(all_ele, done_ele):
        progress = int(round(done_ele/all_ele, 1) * 100)
        progress_str = ''
        for i in range(progress):
            progress_str += '-'
        progress_str += '>'
        for i in range(100-progress):
            progress_str += '_'
        progress_str += '|'
        return progress_str
    @staticmethod
    def show_progress(str, all_ele, done_ele):
        string_to_print = ProgressBar.build_progress_bar(all_ele, done_ele)
        string_to_print = str + string_to_print
        ProgressBar.backward_print(string_to_print)
