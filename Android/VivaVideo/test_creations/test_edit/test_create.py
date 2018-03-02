# -*- coding: utf-8 -*-
"""edit创建视频的测试用例."""
import time
from selenium.webdriver.support.ui import WebDriverWait
from Android import script_ultils as sc


class TestEditCreate(object):
    """edit创建视频的测试类."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_create_craft(self):
        """创建一个草稿视频."""
        sc.logger.info('创建一个草稿视频')
        fun_name = 'test_create_craft'

        time.sleep(1)
        sc.logger.info('点击创作中心主按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/img_creation').click()
        sc.logger.info('点击“剪辑”按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/icon1').click()
        el_video_list = sc.driver.find_elements_by_id('com.quvideo.xiaoying:id/img_click_mask')
        for i in range(3):
            el_video_list[i].click()
            sc.logger.info('点击“添加”按钮')
            sc.driver.find_element_by_id('com.quvideo.xiaoying:id/imgbtn_import').click()
            try:
                WebDriverWait(sc.driver, 60).until(
                    lambda V_improt: V_improt.find_element_by_android_uiautomator('text("下一步")'))
                sc.logger.info('点击“下一步”按钮')
            except TimeoutError as t:
                sc.logger.error('导入视频超时', t)
                return False
            except Exception as e:
                sc.logger.error('导入视频出错', e)
                return False
        sc.logger.info('点击“视频”按钮')
        sc.driver.find_element_by_android_uiautomator('text("视频")').click()
        sc.logger.info('点击“图片”按钮')
        sc.driver.find_element_by_android_uiautomator('text("图片")').click()
        sc.find_by_ids('com.quvideo.xiaoying:id/img_icon', fun_name, self.img_path)
        sc.logger.info('点击“下一步”按钮')
        sc.driver.find_element_by_android_uiautomator('text("下一步")').click()
        sc.logger.info('点击“存草稿”按钮')
        sc.driver.find_element_by_android_uiautomator('text("存草稿")').click()

        sc.logger.info('返回创作中心主界面')
        sc.driver.press_keycode(4)
        sc.logger.info('创建一个草稿视频完成')
