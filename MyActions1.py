



import sys
import time
import logging

from selenium import  webdriver
from selenium.webdriver import  ActionChains, Keys
from selenium.webdriver.common.by import By

import base64
import os
import math
from datetime import datetime, timedelta
from PIL import Image, ImageGrab
# from PIL import ImageGrab
# import io
# import requests
# from bs4 import BeautifulSoup


# 实在懒得传参了，就写这里把
# SetStockPath = 'C:/Users/SITP/Desktop/sun04/重要文件/'
SetStockPath = 'D:/重要误删-软件重要数据/SaveImg/'

# SetSearchDate  搜索哪天的日期
# SetSatID  卫星ID
def MyActions1(SetSearchDate, SetSatID, SetBaseFolder, SetChromePath, SetAreaFilePath, SetBaseDelayTm, StartPage=1):


    #------------常量设置
    StartDate = SetSearchDate + " 00:00:00"
    EndDate = SetSearchDate + " 23:59:59"


    cService = webdriver.ChromeService(SetChromePath)
    # cService = webdriver.ChromeService("C:/Users/SITP/Desktop/sun04/pachong3/chromedriver_win64/chromedriver.exe")

    BaseFolder = SetBaseFolder + SetSatID + "/" + SetSearchDate + "/"    #存储路径




    #----------


    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service = cService, options=options)

    driver.get("https://data.cresda.cn/#/2dMap")

    actions = ActionChains(driver)
    time.sleep(SetBaseDelayTm+3)
    # time.sleep(1)
    # time.sleep(1)

    #搜索框旁边的按钮
    btn_fuhao61 = driver.find_element(By.CLASS_NAME,"menu")
    btn_fuhao61.click()
    time.sleep(SetBaseDelayTm)


    #卫星选择，按分辨率下拉菜单
    btn_switchdrop = driver.find_element(By.XPATH,"//*[@id=\"app\"]/div/div[9]/div[2]/div[3]/div[1]/div[2]")  #ZY1E
    btn_switchdrop.click()
    time.sleep(SetBaseDelayTm)

    #卫星选择，下拉菜单中，选择按发射时间
    btn_switchdrop_bytime = driver.find_element(By.XPATH,"/html/body/ul/li[4]")
    btn_switchdrop_bytime.click()
    time.sleep(SetBaseDelayTm)

    #卫星选择，下拉菜单中，选择按发射时间,[选择卫星ZY1F]
    if SetSatID == "ZY1E":
        btn_switchdrop_bytime_ZY1F = driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/div[1]/ul/li/div/div[3]/div[3]/div[4]/div/div[3]/div[3]/div[2]/div[2]")   #ZY1E
    elif SetSatID == "ZY1F":
        btn_switchdrop_bytime_ZY1F = driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/div[1]/ul/li/div/div[3]/div[3]/div[2]/div/div[3]/div[1]/div[2]/div[2]")  #ZY1F
    elif SetSatID == "GF5B":
        btn_switchdrop_bytime_ZY1F = driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/div[1]/ul/li/div/div[3]/div[3]/div[2]/div/div[3]/div[2]/div[2]/div[2]")  #GF5B
    elif SetSatID == "GF5A":
        btn_switchdrop_bytime_ZY1F = driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/div[1]/ul/li/div/div[3]/div[3]/div[1]/div/div[3]/div[1]/div[2]/div[2]")  #GF5A
    # elif SetSatID == "HJ2B":
    #     btn_switchdrop_bytime_ZY1F = driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/div[1]/ul/li/div/div[3]/div[3]/div[3]/div/div[3]/div[1]/div[3]/div[3]")  # HJ2B
    # elif SetSatID == "HJ2A":
    #     btn_switchdrop_bytime_ZY1F = driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/div[1]/ul/li/div/div[3]/div[3]/div[3]/div/div[3]/div[1]/div[2]/div[3]")  # HJ2A

    btn_switchdrop_bytime_ZY1F.click()
    time.sleep(SetBaseDelayTm)

    #卫星选择，下拉菜单中，选择按发射时间,选择卫星ZY1E,[点击确定]
    btn_switchdrop_bytime_ZY1F_confirm = driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/div[1]/ul/li/div/div[4]/div/div[3]")
    btn_switchdrop_bytime_ZY1F_confirm.click()
    time.sleep(SetBaseDelayTm)


    #时间选择
    btn_date = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[9]/div[2]/div[3]/div[4]")
    btn_date.click()
    time.sleep(SetBaseDelayTm)

    #时间选择,输入时间
    btn_date_StartTm = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[9]/div[2]/div[3]/div[4]/div/input[1]")
    actions.move_to_element(btn_date_StartTm).perform()  #移动到开始日期上


    btn_cdate_clear = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[9]/div[2]/div[3]/div[4]/div/i[2]")
    btn_cdate_clear.click()  #清除日期

    #btn_date_StartTm.clear()
    btn_date_StartTm.send_keys(StartDate)

    btn_date_EndTm = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[9]/div[2]/div[3]/div[4]/div/input[2]")

    #btn_date_EndTm.clear()
    btn_date_EndTm.send_keys(EndDate)
    btn_date_StartTm.click()




    btn_tmp = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[8]/div[1]/input")
    btn_tmp.click()
    time.sleep(SetBaseDelayTm)

    #时间选择,输入时间,确定
    # btn_date_StartTm_Confirm = driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/button[2]")
    # btn_date_StartTm_Confirm.click()
    # time.sleep(SetBaseDelayTm)

    #地点选择


    ## 点击自定义区域
    btn_custom = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[9]/div[2]/div[3]/div[8]/div/div[1]/div/div/div/div[3]")
    btn_custom.click()
    time.sleep(SetBaseDelayTm)
    ## 点击用户上传区域
    btn_custom_upload = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[9]/div[2]/div[3]/div[8]/div/div[2]/div[2]/div/div[3]/div[3]")
    btn_custom_upload.click()
    time.sleep(SetBaseDelayTm)
    ## 直接上传
    btn_custom_input = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[9]/div[3]/div[1]/div[2]/div[1]/div/input")
    # btn_custom_input.send_keys("C:/Users/SITP/Desktop/sun04/custom.zip")
    btn_custom_input.send_keys(SetAreaFilePath)
    time.sleep(SetBaseDelayTm+3)
    ## 点击确定
    btn_custom_confirm = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[9]/div[3]/div[2]/i[2]")
    btn_custom_confirm.click()
    time.sleep(SetBaseDelayTm)


    ##########################################
    # 下面这段是通过【输入中国】选中国，请保留
    ##########################################
    #
    # ## 先点击一下
    # btn_Pos_input = driver.find_element(By.XPATH,
    #                               "/html/body/div[1]/div/div[9]/div[2]/div[3]/div[8]/div/div[2]/div[1]/div[1]")  # 位置输入框
    # btn_Pos_input.click()
    # time.sleep(SetBaseDelayTm)
    # ## 然后输入2次中国，在不同层级
    # btn_Pos_input_real = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[9]/div[2]/div[3]/div[8]/div/div[2]/div[1]/div[1]/div/div[2]/div[1]/input")  # 找到位置选择菜单
    # btn_Pos_input_real.send_keys("中国")
    # btn_Pos_input_real = btn_Pos_input.find_element(By.TAG_NAME, "input")  # 找到位置选择菜单
    # btn_Pos_input_real.send_keys("中国")
    #
    # time.sleep(SetBaseDelayTm)
    #
    # ## 在下拉菜单中，找到中国
    # btn_Pos_menu1 = driver.find_element(By.XPATH, "/html/body/div[6]/div[1]")  # 下拉菜单
    # btn_Pos_menu2 = btn_Pos_menu1.find_elements(By.TAG_NAME, "li")  # 下拉菜单中，列出所有的菜单行
    # b_china = False
    # for e_text in btn_Pos_menu2:
    #     btn_span2_2 = e_text.find_element(By.TAG_NAME, "span")  # 定位到菜单行中国
    #     if btn_span2_2.text == "中国":
    #         b_china = True
    #         e_text.click()
    #         break
    #     else:
    #         continue
    # if b_china == False:
    #     print("Error:中国地区不存在")
    #     driver.close()
    #     return -20000 - StartPage  # 2万表示错误编号，StartPage是要重启的页面
    # time.sleep(SetBaseDelayTm)
    ##########################################





    ##########################################
    # 下面这段是通过【热点区域】选中国，请保留
    ##########################################
    # btn_Pos = driver.find_element(By.XPATH,
    #                               "/html/body/div[1]/div/div[9]/div[2]/div[3]/div[8]/div/div[2]/div[1]/div[2]")  # 点选位置框
    #
    # btn_area3s = btn_Pos.find_elements(By.TAG_NAME, "a")  # 找到位置选择菜单
    #
    # b_china = False
    # for e_text in btn_area3s:
    #
    #     btn_span = e_text.find_element(By.TAG_NAME, "span")  # 找到位置选择菜单
    #     span_html = btn_span.get_attribute("outerHTML")
    #     print(span_html)
    #
    #     if "中国" in span_html:
    #         e_text.click()
    #         b_china = True
    #         break
    #     else:
    #         continue
    #
    # if b_china == False:
    #     print("Error:中国地区不存在")
    #     driver.close()
    #     return -1
    #
    # time.sleep(SetBaseDelayTm)
    ##########################################

    #搜索
    btn_search = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[9]/div[2]/div[3]/div[9]/div[1]/div[1]")
    btn_search.click()
    time.sleep(10)

    #=================上面设置完搜索条件，现在进入下载图片=======================

    #获取到底有多少景
    btn_totalfrm = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[11]/div[1]/div/div/div[2]/div/div[3]/div[3]/div[3]/span[2]")
    print("Total: " + btn_totalfrm.text + " Frames")
    TotalFrames = int(btn_totalfrm.text)  #重要变量，总共多少景
    if TotalFrames <= 0:   # 如果景太少了，那么就推出
        print("Error: No frames, Plz contact Bobby Sun")
        driver.close()
        return -30000

    #更改到每页显示100景
    # btn_100drop = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[11]/div[1]/div/div/div[2]/div/div[3]/div[3]/div[2]")
    # btn_100drop.click()
    # time.sleep(SetBaseDelayTm)
    #
    # btn_100 = driver.find_element(By.XPATH,"/html/body/div[5]/div[1]/div[1]/ul/li[5]")
    # btn_100.click()
    # time.sleep(SetBaseDelayTm)


    #判断有多少页
    # TotalPages = math.ceil(TotalFrames/100)
    TotalPages = math.ceil(TotalFrames/20)
    if StartPage>TotalPages:  #容错，理论上不可能大于
        print("Error: StartPage > TotalPages")
        driver.close()
        return -1

    for i_page in range(StartPage,TotalPages+1):

        #-----切换到第i_page页
        btn_page = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[11]/div[1]/div/div/div[2]/div/div[3]/div[3]/div[5]/span[2]/div/input")
        btn_page.clear()
        btn_page.send_keys(str(i_page))
        btn_page.send_keys(Keys.ENTER)
        print("正在处理第"+str(i_page)+"页...")
        time.sleep(SetBaseDelayTm+3)



        #开始循环显示元素
        #先定位到列表
        List_table = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[11]/div[1]/div/div/div[2]/div/div[3]/div[2]/div[3]/table/tbody")
        List_elements =List_table.find_elements(By.TAG_NAME,"tr")


        #容错，确定跳转页面是否有元素。因为超时，很可能没有元素了。
        if len(List_elements)==0:
            print("Warn: 第"+ str(i_page) +"页面因为超时没有元素，故重启")
            driver.close()
            return i_page

        #################################
        #正式开始循环扫描
        cnt = 0
        for e in List_elements:
            try:
        #    e.click()
                driver.execute_script("arguments[0].scrollIntoView();", e)
                time.sleep(SetBaseDelayTm+2)
                actions.move_to_element(e).perform()  # 移动到这个东西上
                time.sleep(SetBaseDelayTm+2)

                #找到中间感叹号
                btn_gantanhao = e.find_element(By.CLASS_NAME,"caozuo.clearfix")
                btn_gantanhao.click()
                #actions.move_to_element(btn_gantanhao).perform()  #移动到这个东西上
                #actions.click().perform()
                time.sleep(SetBaseDelayTm+5)

                #------先截取图像的meta信息
                strArray_meta = ["信息一览"]
                SceneID = "0"
                set_imgmeta = driver.find_elements(By.CLASS_NAME, "infoTd.fl")
                for e_meta in set_imgmeta:   #提取所有meta元素
                    tmp_str = e_meta.text
                    strArray_meta.append(tmp_str)   #把信息压入堆栈
                    if "景号" in tmp_str:  #记录一下景号
                        SceneID = tmp_str.split("景号:")[1]

                #-------创建对应的目录并存储
                if SceneID == "0":
                    print("Error: 不能获取到SceneID")
                    driver.close()
                    return -1
                new_folder_name = BaseFolder + SceneID + "/"  #新目录的名字
                os.makedirs(new_folder_name, exist_ok=True)
                metafile_path = os.path.join(new_folder_name, "meta.txt")   #新meta的名字

                # 判断这景数据是否存过了，也就是在Stock是否存在？
                meta_Stock_full = SetStockPath + SetSatID + "/" + SetSearchDate + "/" +SceneID + "/meta.txt"  #在stock文件夹的位置，Stock是每天下载爬虫数据会被手动放置在硬盘某个地方，大概率是D:/重要文件
                if os.path.exists(meta_Stock_full):
                    print("已经存在："+meta_Stock_full+"，因此略过该景")
                    # 关闭图像窗体
                    btn_close_img = driver.find_element(By.XPATH,
                                                        "/html/body/div[1]/div/div[11]/div[10]/div/div[2]/div/div[1]/div[4]")
                    btn_close_img.click()
                    # 计数器累加
                    cnt = cnt + 1
                    time.sleep(SetBaseDelayTm)
                    continue

                # 将字符串数组写入txt文件
                with open(metafile_path, 'w', encoding='utf-8') as file:
                    for line in strArray_meta:
                        file.write(line + "\n")

                print(datetime.now().strftime("%H:%M:%S") + ": 处理[" + str(SceneID) + "]中，第" + str(cnt) + "个")
                time.sleep(SetBaseDelayTm)
                # -----进入保存图片环节
                #点击显示图片，出现新的页面
                btn_img = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[11]/div[10]/div/div[2]/div/div[1]/div[1]")
                btn_img.click()
                time.sleep(SetBaseDelayTm)

                #保存图片到剪切板
                windowsID=driver.window_handles


                safe_cnt=0  #安全监察循环
                safe_result=0 #安全监察结果
                while len(windowsID)!=2:   #因网页无法弹出，进入循环安全监察
                    time.sleep(10)
                    #关闭所有垃圾网页
                    windowsID = driver.window_handles
                    for j_window in range(1,len(windowsID)+1): #开始一个一个关闭
                        if j_window-1 ==0:  #主页不关闭
                            continue
                        driver.switch_to.window(windowsID[j_window-1])
                        driver.close()
                        time.sleep(SetBaseDelayTm)
                    #end for

                    #准备重新点击blob
                    safe_cnt = safe_cnt+1
                    driver.switch_to.window(windowsID[0])   #切回到主页
                    #再次点击试试看，是否能弹出界面
                    btn_img = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[11]/div[10]/div/div[2]/div/div[1]/div[1]")
                    btn_img.click()
                    time.sleep(SetBaseDelayTm)
                    windowsID = driver.window_handles
                    print("Info: 景"+ SceneID +"图片下载重试，"+str(safe_cnt))
                    if safe_cnt>10:
                        safe_result = -1
                        break
                #end  while len(windowsID)<2:   #因网页无法弹出，进入循环安全监察

                #安全监察未通过
                if safe_result!=0:
                    print("Warn: 景"+ SceneID +"图片下载失败")
                    #关闭弹出的对话框，准备进入下一景
                    btn_close_img = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[11]/div[10]/div/div[2]/div/div[1]/div[4]")
                    btn_close_img.click()
                    time.sleep(SetBaseDelayTm)
                    continue
                #安全监察通过
                driver.switch_to.window(windowsID[1])

                #保存图片到硬盘
                image_element = driver.find_element(By.XPATH,'/html/body/img')   # 找到图像元素
                blob_url = image_element.get_attribute('src')      # 获取图像链接

                script = """
                var blob_url = arguments[0];
                return fetch(blob_url)
                    .then(response => response.blob())
                    .then(blob => new Promise((resolve, reject) => {
                        var reader = new FileReader();
                        reader.onloadend = () => resolve(reader.result);
                        reader.onerror = reject;
                        reader.readAsDataURL(blob);
                    }));
                """
                base64_data = driver.execute_script(script, blob_url)
                base64_data = base64_data.split(',')[1]

                newsavepath = new_folder_name + 'pic.png'
                with open(newsavepath, 'wb') as f:
                    f.write(base64.b64decode(base64_data))


                #关闭blob网页，并且切换到原来的网页
                ActionChains(driver).send_keys(Keys.CONTROL, 'w').perform()
                driver.close()
                time.sleep(SetBaseDelayTm)
                driver.switch_to.window(windowsID[0])

                # im = ImageGrab.grabclipboard()
                # im.save(r'C:\Users\bobby\Desktop\sun04\pic_'+cnt+'.png')
                # if isinstance(im, Image.Image):
                #     im.save(r'C:\Users\bobby\Desktop\sun04\pic_'+cnt+'.png')
                #     print('save1')
                # else:
                #     print('error')

                #关闭图像窗体
                btn_close_img = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[11]/div[10]/div/div[2]/div/div[1]/div[4]")
                btn_close_img.click()
                time.sleep(SetBaseDelayTm)

                #计数器累加
                cnt = cnt+1
                # if cnt==3:
                #     break
                time.sleep(SetBaseDelayTm)
            except Exception as e:
                print("Warn: 第" + str(i_page) + "页面因第2类错误，大概率因为网卡，失败，故重启页面")
                driver.close()
                return i_page
        #end for e in List_elements:
    #end for i_page in range(1,TotalPages+1):
    time.sleep(5)
    driver.close()
    return 0  #正常返回
