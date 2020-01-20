# _*_ coding: utf-8 _*_
__author__ = 'fanafany'
__date__ = '2020-01-14 9:52 '
import psutil
import time
from pprint import pprint  #用于格式化打印

#定义一个专门用于系统信息的类

class Monitor(object):
    #专门用于单位转换的方法：
    def bytes_to_gb(self,data,key=""):
        if key == "percent":
            return data
        else:
            return round(data /(1024 ** 3),2)

    #专门获取CPU信息
    def cpu(self):
        #percpu:True获取的是每个CPU的使用率，False获取平均使用率
        #1.平均 2.单独 3.物理CPU核心数 4.逻辑CPU核心数
        data = dict(
            percent_avg = psutil.cpu_percent(interval=0,percpu=False),
            percent_per = psutil.cpu_percent(interval=0,percpu=True),
            num_p = psutil.cpu_count(logical=False),
            num_l = psutil.cpu_count(logical=True)
        )
        return data

    #专门获取内存信息
    def mem(self):
        #内存信息
        info = psutil.virtual_memory()
        data = dict(
            total = self.bytes_to_gb(info.total),
            used = self.bytes_to_gb(info.used),
            free = self.bytes_to_gb(info.free),
            percent = info.percent
        )
        return data

    #专门获取交换分区/文件信息
    def swap(self):
        #交换文件/分区信息
        info = psutil.swap_memory()
        data = dict(
            total=self.bytes_to_gb(info.total),
            used=self.bytes_to_gb(info.used),
            free=self.bytes_to_gb(info.free),
            percent=info.percent
        )
        return data

    #专门获取磁盘信息
    def disk(self):
        #专门获取磁盘分区信息
        info = psutil.disk_partitions()
        #列表推导式
        data = [
            dict(
                device = v.device,
                mountpoint = v.mountpoint,
                fstype = v.fstype,
                used = {
                    k: self.bytes_to_gb(v,k)
                    for k, v in psutil.disk_usage(v.mountpoint)._asdict().items()
                }
            )
            for v in info
        ]
        return data


    #专门获取网络的信息
    def net(self):
        #获取地址的信息
        addrs = psutil.net_if_addrs()
        #val.family.name取出协议地址族名称，AF_INET
        addrs_info = {
            k:[
                dict(
                    family=val.family.name,
                    address=val.address,
                    netmask=val.netmask,
                    broadcast=val.broadcast
                )
                for val in v if val.family.name == "AF_INET"
            ]
            for k,v in addrs.items()
        }
        return addrs_info


if __name__ == '__main__':
    m = Monitor()
    # for v in range(1,11):
    #     print(m.cpu())
    #     time.sleep(1)

    # print(m.mem())

    # print(m.swap())

    # pprint(m.disk())

    pprint(m.net())