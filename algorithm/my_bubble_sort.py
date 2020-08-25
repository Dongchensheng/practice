# coding=utf-8

def myBubblesort(test_arr):

    #先定义一个交换的方法
    def changePosition(a,b):
        test_arr[a], test_arr[b] = test_arr[b], test_arr[a]

    n = len(test_arr)

    # for i in range(0,n-1):
    #     print(test_arr[i],test_arr[i+1])
    #     if test_arr[i] > test_arr[i+1]:
    #         changePosition(i,i+1)
    #     else:
    #         pass
    print("当前数组为{}".format(test_arr))
    for i in range(0,n-1):
        print("第{}次循环".format(i+1))
        for j in range(0,n-1):
            if test_arr[j] > test_arr[j+1]:
                changePosition(j,j+1)
                print("我让{}和{}对调了".format(test_arr[j],test_arr[j+1]))
                print("此时数组为{}".format(test_arr))
            else:
                pass

    return test_arr

test_data=[7,6,5,4,3,2,1]
print("最终结果为：{}".format(myBubblesort(test_data)))
