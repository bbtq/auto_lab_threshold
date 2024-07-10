import sensor, image, time
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA)
sensor.skip_frames(time = 2000)
sensor.set_auto_gain(False) # 颜色跟踪必须关闭自动增益
sensor.set_auto_whitebal(False) # 颜色跟踪必须关闭白平衡
sensor.set_auto_exposure(8300) #设置一个固定曝光时间
clock = time.clock()

# 捕捉图像中心的颜色阈值。
#r = [104,172,23,20] # 50x50 center of QVGA.
r = [86,18,5,5] # 50x50 center of QVGA.

#众数获取lab，d为上下差
d = 10
for i in range(60):
    img = sensor.snapshot()
    img.draw_rectangle(r)

    hist = img.get_histogram(roi=r)#获取直方图
    a = hist.get_statistics()

k=[(a[2]-d,a[2]+d,a[10]-d,a[10]+d,a[18]-d,a[18]+d)]
print("Color threshold k: ", k)  # 打印颜色阈值

#最大最小值平均值,确定lab
#print("Learning thresholds...")
#threshold = [50, 50, 0, 0, 0, 0] # Middle L, A, B values.
#for i in range(60):
#    img = sensor.snapshot()
#    img.draw_rectangle(r)
#    hist = img.get_histogram(roi=r)
#    lo = hist.get_percentile(0.01) # 获取1％范围的直方图的CDF（根据需要调整）！
#    hi = hist.get_percentile(0.99) # 获取99％范围的直方图的CDF（根据需要调整）！
#    # 平均百分位值。
#    threshold[0] = (threshold[0] + lo.l_value()) // 2
#    threshold[1] = (threshold[1] + hi.l_value()) // 2
#    threshold[2] = (threshold[2] + lo.a_value()) // 2
#    threshold[3] = (threshold[3] + hi.a_value()) // 2
#    threshold[4] = (threshold[4] + lo.b_value()) // 2
#    threshold[5] = (threshold[5] + hi.b_value()) // 2
#print("Color threshold threshold: ", [threshold])  # 打印颜色阈值

while(True):
    clock.tick()
    img = sensor.snapshot()
    img.binary(k)#二值化图像
#    img.binary([threshold])#二值化图像
