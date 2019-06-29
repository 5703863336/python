erwei = []
n = int(input("进程数："))


def SHURU():
    i = 0
    while(i < n):
        jcName = input("第 %d 个进程名：" % (i+1))
        arriveTime = int(input("到达时间:"))
        serviceTime = int(input("服务时间:"))
        #进程名，到达时间，服务时间，开始，完成，周转，带权周转
        erwei.append([jcName, arriveTime, serviceTime, 0, 0, 0, 0])
        i += 1


#先到先服务
def FCFS():
    erwei.sort(key = lambda x:x[1], reverse = False )     #对列表按照到达时间进行升序排序
    # 计算开始、完成时间
    for i in range(n):
        if(i == 0):
            startTime = int(erwei[i][1])
            erwei[i][3] = startTime
            erwei[i][4] = startTime + int(erwei[i][2])

        elif(i > 0 and  int(erwei[i - 1][4]) < int(erwei[i][1])):
            startTime = int(erwei[i][1])
            erwei[i][3] = startTime
            erwei[i][4] = startTime + int(erwei[i][2])

        else:
            startTime = erwei[i - 1][4]
            erwei[i][3] = startTime
            erwei[i][4] = startTime + int(erwei[i][2])

        i += 1
    # 计算周转、带权周转时间
    for i in range(n):
        erwei[i][5] = float(erwei[i][4] - int(erwei[i][1]))
        erwei[i][6] = float(erwei[i][5] / int(erwei[i][2]))
        i += 1
    # 计算平均周转时间和平均带权周转时间
    ZhouTime = 0
    QuanTime = 0
    for i in range(n):
        ZhouTime = float(ZhouTime + float(erwei[i][5]))
        QuanTime = float(QuanTime + float(erwei[i][6]))
        AzzTime = float(ZhouTime / n)
        AdqzzTime = float(QuanTime / n)
    # 按照开始时间升序输出结果
    erwei.sort(key = lambda x:x[3], reverse = False)
    print("*"*100)
    print('输出')
    for i  in range(n):
        print("总时间: %d 进程名: %s  \n完成时间: %d 周转时间: %d 带权周转时间: %.2f" \
                  % (int(erwei[i][3]), erwei[i][0], int(erwei[i][4]), int(erwei[i][5]), float(erwei[i][6])))
        i += 1
    print("平均周转时间： %.2f" % float(AzzTime))
    print("平均带权周转时间： %.2f" % float(AdqzzTime))


# 最短进程优先
def SJF():
    sjf_erwei = erwei
    i = 1
    k = 0
    # 对列表按照到达时间进行升序排序
    sjf_erwei.sort(key=lambda x: x[1], reverse=False)
    startTime0 = int(sjf_erwei[0][1])
    # 定义列表第一个内容
    erwei[0][3] = startTime0
    erwei[0][4] = startTime0 + int(sjf_erwei[0][2])
    sjf_erwei[0][5] = int(sjf_erwei[0][4]) - int(sjf_erwei[0][1])
    sjf_erwei[0][6] = float(sjf_erwei[0][5]) / int(sjf_erwei[0][2])

    temp_erwei = sjf_erwei[1:len(sjf_erwei)]
    # 对后面的内容按照服务时间排序
    temp_erwei.sort(key=lambda x: x[2], reverse=False)
    sjf_erwei[1:len(sjf_erwei)] = temp_erwei

    while (i < n):
        h = 1
        # 比较到达时间和前一者的完成时间，判断是否需要进行重新排序
        while (int(sjf_erwei[i][1]) >= int(sjf_erwei[i - 1][4])):
            if (i == n - 1):                #当最后一个进程的到达时间大于前一个进程的完成时间
                startTime = sjf_erwei[i][1]
                sjf_erwei[i][3] = startTime
                sjf_erwei[i][4] = startTime + int(sjf_erwei[i][2])
                sjf_erwei[i][5] = int(sjf_erwei[i][4]) - int(sjf_erwei[i][1])
                sjf_erwei[i][6] = float(sjf_erwei[i][5]) / int(sjf_erwei[i][2])
                k = 1  #用于退出循环
                break
            else:        #对进程顺序进行调换
                temp_sjf_erwei = sjf_erwei[i]
                sjf_erwei[i] = sjf_erwei[i + h]
                sjf_erwei[i + h] = temp_sjf_erwei
                h += 1

                if (h >= n - i - 1):
                    temp_erwei2 = sjf_erwei[i:len(sjf_erwei)]
                    temp_erwei2.sort(key=lambda x: x[1], reverse=False)    # 后续队列重新按照到达时间顺序进行排序
                    sjf_erwei[i:len(sjf_erwei)] = temp_erwei2

                    sjf_erwei[i][3] = int(sjf_erwei[i][1])
                    sjf_erwei[i][4] = int(sjf_erwei[i][1]) + int(sjf_erwei[i][2])
                    sjf_erwei[i][5] = int(sjf_erwei[i][4]) - int(sjf_erwei[i][1])
                    sjf_erwei[i][6] = float(sjf_erwei[i][5]) / int(sjf_erwei[i][2])

                    temp_erwei2 = sjf_erwei[i + 1:len(sjf_erwei)]
                    temp_erwei2.sort(key=lambda x: x[2], reverse=False)  # 重新按照服务时间排序
                    sjf_erwei[i + 1:len(sjf_erwei)] = temp_erwei2
                    h = 1
                    i += 1
                else:
                    continue
        if (k == 1):
            break
        else:
            startTime = sjf_erwei[i - 1][4]
            sjf_erwei[i][3] = startTime
            sjf_erwei[i][4] = startTime + int(sjf_erwei[i][2])
            sjf_erwei[i][5] = int(sjf_erwei[i][4]) - int(sjf_erwei[i][1])
            sjf_erwei[i][6] = float(sjf_erwei[i][5]) / int(sjf_erwei[i][2])

            i += 1
    # 周转时间，平均带权周转时间
    ZhouTime = 0
    QuanTime = 0
    for i in range(n):
        ZhouTime = float(ZhouTime + float(erwei[i][5]))
        QuanTime = float(QuanTime + float(erwei[i][6]))
        AzzTime = float(ZhouTime / n)
        AdqzzTime = float(QuanTime / n)
    # 照时间排序
    sjf_erwei.sort(key=lambda x: x[3], reverse=False)
    print('^' * 200)
    print('输出')
    for i in range(n):
        print("总时间: %d 进程名: %s   \n完成时间: %d 周转时间: %d 带权周转时间: %.2f" \
              % (int(sjf_erwei[i][3]), sjf_erwei[i][0], int(sjf_erwei[i][4]), int(sjf_erwei[i][5]),
                 float(sjf_erwei[i][6])))
        i += 1
    print("平均周转时间为： %.2f" % float(AzzTime))
    print("带权周转时间为： %.2f" % float(AdqzzTime))


if __name__ == '__main__':
        SHURU()
        print("1：FCFS")
        print("2：SJF")
        wuqiong = 1
        while(wuqiong == 1):
            choice = int(input(" 1：FCFS \n 2: SJF\n 其他:退出"))
            if(choice == 1):
                FCFS()
            elif(choice == 2):
                SJF()
            else:
                print("已退出")
                m = 0
