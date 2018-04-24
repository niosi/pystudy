# coding=utf-8
import psutil

print("CPU逻辑数量:%d" % psutil.cpu_count())
print("CPU物理数量:%d" % psutil.cpu_count(logical=False))
print("CPU空闲时间:{}".format(psutil.cpu_times()))
print("获取物理内存信息:{}".format(psutil.virtual_memory()))
print("获取交换内存信息:{}".format(psutil.swap_memory()))
print("磁盘信息情况:{}".format(psutil.disk_partitions()))
print("网络信息:{}".format(psutil.net_io_counters()))
print("网络接口信息:{}".format(psutil.net_if_addrs()))
print("网络状态信息:{}".format(psutil.net_if_stats()))
print("网络连接信息:{}".format(psutil.net_connections()))