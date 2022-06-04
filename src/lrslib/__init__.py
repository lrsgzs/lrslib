import .tkin
import .tools

def by():
    print('LrsLib作者：刘镕硕\n刘镕硕版权所有')
def func(fun='all'):
    function = {'tkin.Window':'仿tk窗口，用Button时，Tk()为 .win',
                'tools.pront':'一个一个地打印文本',
                'tools.show_image':'显示图片在pygame窗口中',
                'all':'''全部函数：
'tkin.Window':'仿tk窗口，用Button时，Tk()为 .win',
'tools.pront':'一个一个地打印文本',
'tools.show_image':'显示图片在pygame窗口中'
'by':'关于'
'func':'帮助'
'''
                }
    print(function[fun])
