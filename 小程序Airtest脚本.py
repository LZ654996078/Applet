
# -*- encoding=utf8 -*-
__author__ = "Administrator"
import random #导入随机数  
from airtest.core.api import *
from airtest.core.android import Android
auto_setup(__file__)

###############公用方法##################

#滑动方法：
def slide(randoms):
     # 向下滑动 
    width, height = device().get_current_resolution()
    # 校准滑动的起点和终点，因为大部分app上下有底栏和顶部导航，不在滑动范围，所以这里的height不是从0.1开始
    # 生成 随机数 
    # randoms = random.randint(13,15)
    # start_pt2 = (width *0.9,height / 2)
    # end_pt2 = (width *0.1,height / 2)
    # 等待设备的响应 # 
    # 左滑N次:# for i in range(2):
    # swipe(start_pt2 , end_pt2,1000)
    #     sleep(1)  
    # 等待设备的响应  
    start_pt1 = (width / 2,height * 0.7)
    end_pt1 = (width / 2,height * 0.3)
    # 上滑N次:
    for i in range(randoms):
        swipe(start_pt1, end_pt1,1000)
        sleep(1)          
#关闭弹窗方法： 
def Close():
    close = exists(Template(r"tpl1637203036057.png", rgb=True, target_pos=5, record_pos=(0.001, 0.475), resolution=(1080, 1920)))
    if close:
        touch(Template(r"tpl1637203068320.png", rgb=True, target_pos=5, record_pos=(-0.002, 0.48), resolution=(1080, 1920)))
    sleep(2)     
#返回层级方法：number 次数参数
def black(number):
    back=1 
    while (back<=number):
            keyevent("BACK")
            back+=1
            
            
################Case方法#################   
#进入小程序
def EnterApplets():
    start_app("com.tencent.mm")  # 启动微信，可通过"报名查看器.app",查看其包名
    sleep(2)
# poco(text="发现").click()
# poco(text="小程序").click()

    touch(Template(r"tpl1637205532676.png", record_pos=(0.126, 0.854), resolution=(1080, 1920)))

    sleep(1)
    touch(Template(r"tpl1636943778649.png", record_pos=(-0.289, 0.655), resolution=(1080, 1920)))
    sleep(1)
# posleep(2)co(text="良品铺子+").click()
    touch(Template(r"tpl1636943793507.png", record_pos=(-0.187, 0.114), resolution=(1080, 1920)))
    sleep(10)
    Close()
#会员码case >>>>>>>>>>>>>>     
def memberCode():
    touch(Template(r"tpl1636943434521.png", record_pos=(0.403, 0.855), resolution=(1080, 1920)))
    # poco(text="会员中心").click()
    sleep(10.0)
    # 二维码
    touch(Template(r"tpl1636942595548.png", record_pos=(0.171, -0.763), resolution=(1080, 1920)))
    # 会员码断言
    if assert_exists(Template(r"tpl1636946253922.png", record_pos=(0.011, 0.231), resolution=(1080, 1920)), "会员码加载成功"):
        print("通过+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    else:
        print("不通过")  
        keyevent("BACK") #手机返回键
    sleep(1)
#     text1 = pytesseract.image_to_string(Image.open(r'C:\Users\Administrator\Desktop\小程序.air\tpl1637117678191.png'))
#     print(text1)


    
    assert_exists(Template(r"tpl1637117678191.png", record_pos=(0.011, -0.272), resolution=(1080, 1920)), "会员卡号加载成功")
    touch(Template(r"tpl1636943601264.png", record_pos=(-0.439, -0.765), resolution=(1080, 1920)))
    sleep(1)
#积分case<<<<<<<<<<<<<<<<<
def total():
    touch(Template(r"tpl1637805386078.png", record_pos=(-0.059, -0.256), resolution=(1080, 1920)))
    sleep(3.0)
    if exists(Template(r"tpl1637805425907.png", record_pos=(-0.4, 0.299), resolution=(1080, 1920))):
        assert_exists(Template(r"tpl1637805646337.png", record_pos=(-0.404, 0.044), resolution=(1080, 1920)), "积分详情页面加载成功")
        keyevent("BACK")

    else:
        assert_not_exists(Template(r"tpl1637810565134.png", record_pos=(-0.406, 0.047), resolution=(1080, 1920)), "积分详情页面加载失败")
        keyevent("BACK")    
#签到Case>>>>>>>>>>>>>>>>>
def singLogin():
    integral = exists(Template(r"tpl1637722698587.png", record_pos=(-0.399, 0.606), resolution=(1080, 1920)))

    if  integral:
        sleep(2.0)
        print("走这里A")
        touch(Template(r"tpl1637630497667.png", record_pos=(-0.394, -0.039), resolution=(1080, 1920)))
        sleep(6.0)
        touch(Template(r"tpl1638419038274.png", rgb=True, record_pos=(-0.001, 0.475), resolution=(1080, 1920)))

        sleep(10.0)
        successLogin = exists(Template(r"tpl1637736110253.png", record_pos=(-0.005, -0.081), resolution=(1080, 1920)))

        if successLogin :
            assert_exists(Template(r"tpl1637632827780.png", record_pos=(-0.002, -0.167), resolution=(1080, 1920)), "签到成功")
            sleep(5.0)

            touch(Template(r"tpl1637632855316.png", record_pos=(0.424, -0.387), resolution=(1080, 1920)))
            sleep(5.0)
            black(2)
            print("走这里b")
        else:
            print("走这里c")
            assert_exists(Template(r"tpl1637633095863.png", record_pos=(-0.272, -0.295), resolution=(1080, 1920)), "签到成功&今天已签到")
            black(2)
                
    else:
        touch(Template(r"tpl1636943434521.png", record_pos=(0.403, 0.855), resolution=(1080, 1920)))
        sleep(5.0)
        print("走这里d，页面加载失败")           
#储值>>>>>>>>>>>>>>>>>>>>>>
def storedValue():
    touch(Template(r"tpl1638497129246.png", record_pos=(-0.336, -0.283), resolution=(1080, 1920)))
    sleep(5.0)
    OtherAmount =exists(Template(r"tpl1638497333928.png", record_pos=(-0.319, 0.371), resolution=(1080, 1920)))
    if OtherAmount:
        assert_exists(Template(r"tpl1638497365587.png", record_pos=(-0.323, 0.362), resolution=(1080, 1920)), "储值详情加载成功")
        touch(Template(r"tpl1638499921969.png", record_pos=(-0.32, 0.162), resolution=(1080, 1920)))
        touch(Template(r"tpl1638499932557.png", record_pos=(0.014, 0.815), resolution=(1080, 1920)))
        tanChuang =exists(Template(r"tpl1638499972445.png", record_pos=(0.006, -0.098), resolution=(1080, 1920)))
        if tanChuang:
            touch(Template(r"tpl1638499991041.png", record_pos=(0.236, 0.19), resolution=(1080, 1920)))
            sleep(5.0)
            if assert_exists(Template(r"tpl1638500237356.png", record_pos=(0.013, -0.481), resolution=(1080, 1920)), "唤起支付成功，储值成功"):
                touch(Template(r"tpl1638500292275.png", record_pos=(-0.323, -0.543), resolution=(1080, 1920)))
                sleep(2.0)

            else:
                assert_not_exists(Template(r"tpl1638500263542.png", record_pos=(0.02, -0.475), resolution=(1080, 1920)), "唤起支付失败")      
        else:
            sleep(4.0)
            if assert_exists(Template(r"tpl1638500237356.png", record_pos=(0.013, -0.481), resolution=(1080, 1920)), "唤起支付成功，储值成功"):
                touch(Template(r"tpl1638500292275.png", record_pos=(-0.323, -0.543), resolution=(1080, 1920)))

            else:
                assert_not_exists(Template(r"tpl1638500263542.png", record_pos=(0.02, -0.475), resolution=(1080, 1920)), "唤起支付失败")
        touch(Template(r"tpl1638498330827.png", record_pos=(-0.349, -0.392), resolution=(1080, 1920)))
        sleep(4.0)

        huiyuanma = exists(Template(r"tpl1638502676215.png", record_pos=(0.009, 0.223), resolution=(1080, 1920)))
        if huiyuanma:
            
            assert_exists(Template(r"tpl1638502698534.png", record_pos=(-0.001, 0.219), resolution=(1080, 1920)), "会员码加载成功")
            assert_exists(Template(r"tpl1637117678191.png", record_pos=(0.011, -0.272), resolution=(1080, 1920)), "会员卡号加载成功")
            touch(Template(r"tpl1638498666762.png", record_pos=(-0.443, -0.767), resolution=(1080, 1920)))
            sleep(2.0)
                  
        else:
            assert_not_exists(Template(r"tpl1638498503248.png", record_pos=(-0.005, 0.226), resolution=(1080, 1920)), "会员码加载失败")

            print("不通过")  
            keyevent("BACK") 
            sleep(1)      
        touch(Template(r"tpl1638498965691.png", record_pos=(0.331, -0.39), resolution=(1080, 1920)))
        sleep(2.0)
        record= exists(Template(r"tpl1638499386727.png", record_pos=(0.007, 0.092), resolution=(1080, 1920)))
        if record:
            assert_exists(Template(r"tpl1638499448217.png", record_pos=(-0.003, 0.093), resolution=(1080, 1920)), "暂无储值记录")
        else:
            assert_exists(Template(r"tpl1638499692962.png", record_pos=(-0.409, -0.514), resolution=(1080, 1920)), "储值记录加载成功")
            keyevent("BACK")
            sleep(3.0)
        touch(Template(r"tpl1638499789460.png", record_pos=(-0.265, -0.645), resolution=(1080, 1920)))
        sleep(5.0)
        valueJilu = exists(Template(r"tpl1638511180719.png", record_pos=(0.374, -0.561), resolution=(1080, 1920)))
        if valueJilu:
            assert_exists(Template(r"tpl1638512980660.png", record_pos=(0.368, -0.559), resolution=(1080, 1920)), "交易明细页加载成功")

            black(2)
        else:
            assert_not_exists(Template(r"tpl1638513001757.png", record_pos=(0.371, -0.314), resolution=(1080, 1920)), "交易明细页加载失败")
            keyevent("BACK")
    else:
        assert_not_exists(Template(r"tpl1638497951812.png", rgb=True, record_pos=(-0.324, 0.365), resolution=(1080, 1920)), "储值详情页加载失败")
        keyevent("BACK")
#拼团case>>>>>>>>>>>>>>>>>
def pingTuan():
    slide(4)
    pintuan = exists(Template(r"tpl1638411989546.png", record_pos=(0.152, 0.076), resolution=(1080, 1920)))
    if pintuan:
        touch(Template(r"tpl1638412033916.png", record_pos=(0.155, 0.074), resolution=(1080, 1920)))
        sleep(4.0)
        randoms = random.randint(1,9)
        slide(randoms)
        pingtaunParticulars =  exists(Template(r"tpl1638413747016.png", record_pos=(0.302, 0.065), resolution=(1080, 1920)))
        if pingtaunParticulars:
            assert_exists(Template(r"tpl1638413849669.png", record_pos=(0.307, 0.067), resolution=(1080, 1920)), "拼团列表加载成功")
            touch(Template(r"tpl1638412271707.png", record_pos=(0.315, 0.182), resolution=(1080, 1920)))
            sleep(4.0)
            product =exists(Template(r"tpl1638414231183.png", record_pos=(-0.319, -0.158), resolution=(1080, 1920)))
            if product:
                assert_exists(Template(r"tpl1638414259150.png", record_pos=(-0.319, 0.362), resolution=(1080, 1920)), "拼团商品详情加载成功")
                touch(Template(r"tpl1638414436780.png", record_pos=(0.251, 0.846), resolution=(1080, 1920)))
                sleep(2.0)
                ServiceTime= exists(Template(r"tpl1638414510225.png", record_pos=(0.002, -0.394), resolution=(1080, 1920)))
                if ServiceTime:
                    assert_exists(Template(r"tpl1638414535503.png", record_pos=(0.007, -0.391), resolution=(1080, 1920)), "拼团订单详情加载成功")
                    touch(Template(r"tpl1638414931163.png", record_pos=(-0.068, 0.824), resolution=(1080, 1920)))
                    sleep(6.0)
                    payTanchuang =exists(Template(r"tpl1638415363816.png", record_pos=(0.006, -0.478), resolution=(1080, 1920)))
                    if payTanchuang:
                        assert_exists(Template(r"tpl1638415385090.png", record_pos=(0.012, -0.479), resolution=(1080, 1920)), "创建拼团订单成功")
                        touch(Template(r"tpl1638415510107.png", record_pos=(-0.326, -0.546), resolution=(1080, 1920)))
                        sleep(2.0)
                        touch(Template(r"tpl1638415527175.png", record_pos=(-0.002, 0.165), resolution=(1080, 1920)))
                        black(3)
                        sleep(2.0)
                        touch(Template(r"tpl1638501208179.png", record_pos=(0.406, 0.852), resolution=(1080, 1920)))
                        sleep(4.0)

                    else:
                        assert_not_exists(Template(r"tpl1638415414270.png", record_pos=(0.004, -0.48), resolution=(1080, 1920)), "唤起支付失败")
                        black(3)
                else :
                    assert_not_exists(Template(r"tpl1638414626900.png", record_pos=(0.006, -0.395), resolution=(1080, 1920)), "拼团订单详情失败")
                    black(3)
            else:
                assert_not_exists(Template(r"tpl1638414353654.png", record_pos=(-0.319, 0.361), resolution=(1080, 1920)), "拼团商品详情加载失败")

                black(2)
        else:
            assert_not_exists(Template(r"tpl1638413980652.png", record_pos=(0.313, 0.063), resolution=(1080, 1920)), "拼团列表加载失败")
            keyevent("BACK")
    else:
        touch(Template(r"tpl1638412120621.png", record_pos=(0.406, 0.854), resolution=(1080, 1920)))
        sleep(10.0)
#首页case>>>>>>>>>>>>>>>>>
def homePage():
# poco(text="购物车").click()
    sleep(5.0)
    touch(Template(r"tpl1637118102946.png", record_pos=(-0.374, 0.848), resolution=(1080, 1920)))
    sleep(10)
    Close()
    sleep(2)
    #滑动屏幕 随机数 13 -15
    randoms = random.randint(13,14)
    slide(randoms)
    assert_exists(Template(r"tpl1638418394461.png", rgb=True, record_pos=(-0.082, 0.047), resolution=(1080, 1920)), "首页加载成功")

#加入商品购物车case>>>>>>>>
def addShopping():
    #购物车是否存在
    shoppingCart =exists(Template(r"tpl1638418412490.png", rgb=True, record_pos=(-0.078, 0.05), resolution=(1080, 1920)))


    if shoppingCart:

    #     进入商品详情页 
        touch(Template(r"tpl1638426537654.png", record_pos=(-0.081, 0.24), resolution=(1080, 1920)))

        sleep(4.0)
        #下滑一下
        slide(1)

        assert_exists(Template(r"tpl1637287524555.png", record_pos=(0.423, 0.68), resolution=(1080, 1920)), "商详加载成功")
        sleep(4.0)
    #     加入购物车

        touch(Template(r"tpl1637136410598.png", record_pos=(0.025, 0.827), resolution=(1080, 1920)))
        sleep(3)
    #     添加多个商品>>>>>>>>>>>>>>>>>while>>>>>>>>>>>>>>>>>>>>>>>
        add=1
        while (add <2):
            touch(Template(r"tpl1637136431404.png", record_pos=(0.388, 0.44), resolution=(1080, 1920)))
            add+=1
            print("首页加载成功-log")
        sleep(2)

        touch(Template(r"tpl1637138760028.png", record_pos=(-0.004, 0.63), resolution=(1080, 1920)))
        sleep(2)
        keyevent("BACK")
        sleep(2)
        touch(Template(r"tpl1637118102946.png", record_pos=(-0.374, 0.848), resolution=(1080, 1920)))
        sleep(2)   
            
    else:
        print("首页加载失败-log")
        keyevent("BACK")
# 关闭小程序
def closeApplets():
    touch(Template(r"tpl1637128041666.png", record_pos=(0.422, -0.766), resolution=(1080, 1920)))

    sleep(1)
    touch(Template(r"tpl1637128202465.png", record_pos=(-0.438, -0.762), resolution=(1080, 1920)))

    sleep(1)
    touch(Template(r"tpl1637205667724.png", record_pos=(-0.368, 0.851), resolution=(1080, 1920)))
    sleep(1)
    home()

    
###############调用Case方法################
# 进入小程序
EnterApplets()
# 会员中心case:
memberCode()    
#积分case<<<<<<<<<<<<<<<<<
total()
#签到Case>>>>>>>>>>>>>>>>>
singLogin()
#拼团case>>>>>>>>>>>>>>>>>
pingTuan()
#储值>>>>>>>>>>>>>>>>>>>>>>
storedValue()
#首页case>>>>>>>>>>>>>>>>>
homePage()
#加入购物车case>>>>>>>>>>>
addShopping()
# 关闭小程序>>>>>>>>>>>>>>
closeApplets()
# poco(text="微信").click()




