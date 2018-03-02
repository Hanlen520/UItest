# -*- coding: utf-8 -*-
"""转场的基本操作测试用例."""
import time
from Android import script_ultils as sc


class TestEditTransition(object):
    """转场的基本操作测试类."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_edit_transition(self):
        """剪辑-转场-添加."""
        sc.logger.info('剪辑-转场-添加')
        fun_name = 'test_edit_transition'

        start_x = self.width - self.width // 4
        start_bottom = self.height - self.height // 10

        time.sleep(1)
        sc.logger.info('点击创作中心主按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/img_creation').click()
        sc.logger.info('点击“更多草稿”')
        sc.driver.find_element_by_android_uiautomator('text("更多草稿")').click()

        sc.logger.info('点击草稿封面')
        el_draft = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_studio_img_project_thumb')
        el_draft.click()
        sc.logger.info('点击“剪辑”')
        sc.driver.find_element_by_android_uiautomator('text("剪辑")').click()

        sc.swipe_by_ratio(start_x, start_bottom, 'left', 0.6, 500)
        time.sleep(1)

        el_edit_list = sc.driver.find_elements_by_id('com.quvideo.xiaoying:id/title')
        for el_item in el_edit_list:
            if el_item.text == '转场':
                sc.logger.info('开始点击转场')
                el_item.click()
                break
        el_cover_list = sc.driver.find_elements_by_id('com.quvideo.xiaoying:id/ImageView_Content_Thumbnail')
        el_cover_list[2].click()
        sc.capture_screen(fun_name, self.img_path)
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_com_btn_right').click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('返回创作中心主界面')
        for i in range(4):
            time.sleep(1)
            sc.driver.press_keycode(4)
        sc.logger.info('剪辑-转场-添加测试完成')

    def test_transition_cancel(self):
        """剪辑-转场-放弃."""
        sc.logger.info('剪辑-转场-放弃')
        fun_name = 'test_transition_cancel'
        start_x = self.width - self.width // 4
        start_bottom = self.height - self.height // 10

        time.sleep(1)
        sc.logger.info('点击创作中心主按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/img_creation').click()
        sc.logger.info('点击“更多草稿”')
        sc.driver.find_element_by_android_uiautomator('text("更多草稿")').click()

        sc.logger.info('点击草稿封面')
        el_draft = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_studio_img_project_thumb')
        el_draft.click()
        sc.logger.info('点击“剪辑”')
        sc.driver.find_element_by_android_uiautomator('text("剪辑")').click()

        sc.swipe_by_ratio(start_x, start_bottom, 'left', 0.6, 500)
        time.sleep(1)

        el_edit_list = sc.driver.find_elements_by_id('com.quvideo.xiaoying:id/title')
        for el_item in el_edit_list:
            if el_item.text == '转场':
                sc.logger.info('开始点击转场')
                el_item.click()
                break
        el_cover_list = sc.driver.find_elements_by_id('com.quvideo.xiaoying:id/ImageView_Content_Thumbnail')
        el_cover_list[3].click()
        sc.capture_screen(fun_name, self.img_path)
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_com_btn_left').click()
        sc.driver.find_element_by_android_uiautomator('text("确认")').click()

        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('返回创作中心主界面')
        for i in range(4):
            time.sleep(1)
            sc.driver.press_keycode(4)
        sc.logger.info('剪辑-转场-放弃测试完成')
