from tkinter import *#自带的tk图形模块linux不是自带的...tk显示png图片资料https://www.cnblogs.com/shemingli/p/6344866.html
class l():
	def ll(self):
		root = Tk()
		root.title('我的网络与计算机处理结果')
		root.resizable(width=False, height=False)#关闭拉伸
		duanxuankuanjiagou=Frame(root)
		duanxuankuanjiagou.grid(row=6 ,column=0,columnspan=2)

		self.gunlun=Scrollbar(duanxuankuanjiagou)#图形滚轮
		self.texteditor=Text(duanxuankuanjiagou,width=100, height=30,bg='Black',fg='Pink',yscrollcommand=self.gunlun.set)
		self.gunlun.grid(row=0,column=1,rowspan=2,sticky=N+S)			#width=宽度height高度
		#定义颜色https://blog.csdn.net/sinat_41104353/article/details/79307111
		#意思就是如果是DISABLED的话那就无法编辑、插入、删除。所以可以在你需要插入、删除的时候把状态变为NORMAL，完成插入、删除后再改回DISABLED
		#self.texteditor.focus_force()#使用focus_force()来使光标在文本后面
		self.texteditor.grid(row=0,column=0)
		#回车事件key(event)https://blog.csdn.net/bnanoou/article/details/38434443
		#---------------------------------------------------------------
		#这里不用texteditor作为事件对象，而是使用root事件做关闭对象，不然会有异常
		self.gunlun.config(command=self.texteditor.yview)#同步图形滚轮



		menu2= Menu(root, tearoff=0,bg='Black',fg='Pink')#tearoff=0是取消弹窗独立
		root.bind("<Button-3>",lambda event,x=menu2:x.post(event.x_root, event.y_root))#鼠标事件#鼠标右击事件https://blog.csdn.net/wangyiyan315/article/details/16367551
		menu2.add_command(label="复制", command=lambda x=self.texteditor:x.event_generate("<<Copy>>"))#拷贝
		menu2.add_command(label="粘贴", command=lambda x=self.texteditor:x.event_generate("<<Paste>>"))#粘贴
		menu2.add_command(label="清空", command=lambda x=self.texteditor:x.delete(0.1, END))
            #menu2.add_command(label="清空", command=lambda x=xianshi:x.delete(0, END))  #删除所有值	#https://www.cnblogs.com/botoo/p/8463702.html
		menu2.add_command(label='关闭')











		into=[]
		while 1:
		    try:
		        have=input()#使用管道的机制获取所有输入
		        into.append(have)

		    except:break
		self.texteditor.insert(INSERT,'\n'.join(into))#插入计时计

		root.mainloop()

l().ll()