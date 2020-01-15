def cut(a):#剪辑
	a.event_generate("<<Cut>>")
def copy(a):#拷贝
	a.event_generate("<<Copy>>")
def paste(a):#粘贴
	a.event_generate('<<Paste>>')