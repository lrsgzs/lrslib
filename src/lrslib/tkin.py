import tkinter

class IconImageError(ValueError):
    pass
class Window(tkinter.Tk):
    """
    对Tk()进行优化的适合中国人的一个类
    """
    def __init__(self, list=["No"]):
        """
        初始化
        :param list: 是否需要初始化，及初始化内容。第一项为是否需要，为No或Yes，第二项是标题，第三项是大小，第四项是icon。后面三项是在第一项为Yes的情况下加上，第一项为No时用默认配置
        """
        super().__init__()
        if list[0] != "No":
            self.setup(title=list[1], geo=list[2], icon=list[3])
        else:
            self.setup(title="tk", geo="500x500", icon="No")
    def setup(self, title="tk", geo="500x500", icon="No"):
        """
        设置配置
        :param title: 标题
        :param geo: 大小
        :param icon: 图案
        """
        self.title(title)
        self.geometry(geo)
        if icon != "No":
            try:
                self.iconbitmap(icon)
            except:
                tkinter.messagebox.showerror('文件错误', "对不起，你加载的文件不存在或不能成为图标。")
                raise IconImageError("对不起，你加载的文件不存在或不能成为图标。")
    def run(self):
        """
        运行
        """
        self.mainloop()
    def return_self(self):
        """
        返回self
        :return: self
        """
        return self