import tkinter

class IconImageError(ValueError):
    pass
class Window:
    def __init__(self, list=["No"]):
        self.win = tkinter.Tk()
        if list[0] != "No":
            self.setup(title=list[0], geo=list[1], icon=list[2])
        else:
            self.setup(title="tk", geo="500x500", icon="No")
    def setup(self, title="tk", geo="500x500", icon="No"):
        self.win.title(title)
        self.win.geometry(geo)
        if icon != "No":
            try:
                self.win.iconbitmap(icon)
            except:
                tkinter.messagebox.showerror('文件错误', "对不起，你加载的文件不存在或不能成为图标。")
                raise IconImageError("对不起，你加载的文件不存在或不能成为图标。")
    def run(self):
        self.win.mainloop()