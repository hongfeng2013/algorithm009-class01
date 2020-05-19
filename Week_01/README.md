学习笔记

#################################################
    11. 盛最多水的容器:
    https://leetcode-cn.com/problems/container-with-most-water/
    1. 采用暴力法，2重循环。执行时间有超时
    2. 采用2边夹击法。
##################################################
    70.  爬楼梯:
    https://leetcode-cn.com/problems/climbing-stairs/
    采用类似递归的方法，但使用循环。
    f(1) = 1
    f(2) = 2
    f(3）= f(1) + f(2)
    f(n) = f(n-2) + f(n-1)
##################################################
    283: 移动零:
    https://leetcode-cn.com/problems/move-zeroes/
    将非零的数依次移到list的最前面，后面补0
    