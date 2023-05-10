import uiautomator2 as ua2

if __name__ == "__main__":
    d = ua2.connect('xcpz4l9dfyf675kv')
    print(d.info)
    d.app_start("cn.damai")
    d.set_fastinput_ime(False)
    d(resourceId="cn.damai:id/homepage_advert_pb").click()
    d(resourceId="cn.damai:id/channel_search_text").click()
    d.sleep(1)
    d(resourceId="cn.damai:id/header_search_v2_input").send_keys('梁静茹世界巡回演唱会苏州站')
    d.click(0.913, 0.895)

    d.xpath('//*[@resource-id="cn.damai:id/one_arch_recyclerView"]/android.widget.FrameLayout[1]').click()
    d.sleep(1)

    d(resourceId="cn.damai:id/damai_theme_dialog_cancel_btn").click_exists()
    d.sleep(1)

    d.click(0.608, 0.95)
    print('进入抢票页面')

    # 抢第几场的票
    group_id = 1
    d.xpath(f'//*[@resource-id="cn.damai:id/project_detail_perform_flowlayout"]/android.widget.FrameLayout[{group_id}]/android.widget.LinearLayout[1]').click()
    d.sleep(0.5)

    # 抢多少钱的票
    money_id = 3
    d.xpath(f'//*[@resource-id="cn.damai:id/project_detail_perform_price_flowlayout"]/android.widget.FrameLayout[{money_id}]/android.widget.LinearLayout[1]').click()
    d.sleep(0.2)

    while d(text="预售").exists(timeout=5):
        d.press("back")
        d.sleep(0.5)
        d.click(0.608, 0.95)
        print('进入抢票页面')

    # 需要购买张数
    for i in range(0, 1):
        d(resourceId="cn.damai:id/img_jia").click()

    d(text="确定").click()
