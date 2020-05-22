# 学习笔记


## 11. 盛最多水的容器:

    https://leetcode-cn.com/problems/container-with-most-water/
    
    1. 采用暴力法，2重循环。执行时间有超时
    
    2. 采用2边夹击法。
    

## 70.  爬楼梯:
    
    https://leetcode-cn.com/problems/climbing-stairs/
    
    采用类似递归的方法，但使用循环。
    
    f(1) = 1
    f(2) = 2
    f(3）= f(1) + f(2)
    f(n) = f(n-2) + f(n-1)
    
## 283: 移动零:
    
    https://leetcode-cn.com/problems/move-zeroes/
    
    将非零的数依次移到list的最前面，后面补0
    
## 66. 加一:

    https://leetcode-cn.com/problems/plus-one/
    
    1. 方法一，倒序遍历每个数字，如果不为9，加一后直接返回。如果遍历结束没有返回，表示都是9，需要加一位。
    
    2. 方法二，使用str()和int()，数字和字符串变换。
    
## 88. 合并两个有序数组:

    https://leetcode-cn.com/problems/merge-sorted-array/
    
    使用2个下标，比较2个list元素大小，
    
## 1. 两数之和
    
    https://leetcode-cn.com/problems/two-sum/
    
    使用字典，判断差是否在字典中.
    
## 84. 柱状图中最大的矩形

    https://leetcode-cn.com/problems/largest-rectangle-in-histogram/
    
    1. 方法一： 使用暴力法
    2. 方法二： 使用stack
    
## 155. 最小栈

    https://leetcode-cn.com/problems/min-stack/
    
    使用辅助栈
    