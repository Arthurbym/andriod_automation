# from retail.test_case.page_obj.login_page import LoginPage
import unittest
from retail.test_case.models.myunittest import MyUnitTest
import  time
import sys
from retail.test_case.models.log import Logger
import logging

log = Logger(__name__)
class LoginTc(MyUnitTest):
    def test_login_correct_user_correct_password(self):
        '''正确的用户名及正确密码'''
        try:
            self.login.goLogin()
            self.login.loginFunc(int(self.login.loginTestDate[0][0]),int(self.login.loginTestDate[0][1]))
            time.sleep(2)
            cuurUrl = self.driver.current_url
            self.assertIn('my',cuurUrl,'登录失败或登录后的默认页面不对')
        except Exception:
            self.login.saveScreenShot('%s_fail.png'%(sys._getframe().f_code.co_name))
            time.sleep(1)
            raise
        else:
            self.login.saveScreenShot('%s_pass.png'%(sys._getframe().f_code.co_name))
            time.sleep(1)
            log.logger.info('%s test completed '%(sys._getframe().f_code.co_name))

    def test_login_correct_user_incorrect_password(self):
        '''正确的用户名及不正确的密码'''
        try:
            self.login.goLogin()
            self.login.loginFunc(int(self.login.loginTestDate[1][0]),int(self.login.loginTestDate[1][1]))
            alertIfo = self.login.findElement('xpath','/html/body/div[2]').get_attribute('class')
            log.logger.info(alertIfo)
            time.sleep(2)
            self.assertIn('el-message el-message--error',alertIfo,'提示不正确或没有提示')
        except Exception:
            self.login.saveScreenShot('%s_fail.png'%(sys._getframe().f_code.co_name))
            time.sleep(1)
            raise
        else:
            self.login.saveScreenShot('%s_pass.png'%(sys._getframe().f_code.co_name))
            time.sleep(1)
            log.logger.info('%s test completed '%(sys._getframe().f_code.co_name))

    def test_login_correct_user_empty_password(self):
        '''正确的用户名及空的密码'''
        try:
            self.login.goLogin()
            self.login.loginFunc(self.login.loginTestDate[2][0],self.login.loginTestDate[2][1])
            time.sleep(1)
            alertIfo = self.login.findElement('xpath','//*[@id="app"]/div/div/div/div/div[1]/form/div[2]/div/div[2]').text
            self.assertIn('请输入密码',alertIfo,'提示不正确或没有提示')
        except Exception:
            self.login.saveScreenShot('%s_fail.png'%(sys._getframe().f_code.co_name))
            time.sleep(1)
            raise
        else:
            self.login.saveScreenShot('%s_pass.png'%(sys._getframe().f_code.co_name))
            time.sleep(1)
            log.logger.info('%s test completed '%(sys._getframe().f_code.co_name))

    def test_login_incorrect_user_correct_name(self):
        '''错误的用户名及正确的密码'''
        try:
            self.login.goLogin()
            self.login.loginFunc(self.login.loginTestDate[3][0],self.login.loginTestDate[3][1])
            time.sleep(1)
            alertIfo = self.login.findElement('xpath','//*[@id="app"]/div/div/div/div/div[1]/form/div[1]/div/div[2]').text

            # cuurUrl = self.driver.current_url
            self.assertEqual('长度在11 个字符',alertIfo,'提示不正确或没有提示')
        except Exception:
            self.login.saveScreenShot('%s_fail.png'%(sys._getframe().f_code.co_name))
            time.sleep(1)
            raise
        else:
            self.login.saveScreenShot('%s_pass.png'%(sys._getframe().f_code.co_name))
            time.sleep(1)
            log.logger.info('%s test completed '%(sys._getframe().f_code.co_name))

    def test_login_empty_user_empty_name(self):
        '''空的用户名及空的密码'''
        try:
            self.login.goLogin()
            self.login.loginFunc(self.login.loginTestDate[4][0],self.login.loginTestDate[4][1])
            time.sleep(1)
            alertIfo = self.login.findElement('xpath','//*[@id="app"]/div/div/div/div/div[1]/form/div[1]/div/div[2]').text
            alertIfo1 = self.login.findElement('xpath','//*[@id="app"]/div/div/div/div/div[1]/form/div[2]/div/div[2]').text
            self.assertEqual('请输入密码', alertIfo1, '提示不正确或没有提示') and \
            self.assertEqual('长度在11 个字符',alertIfo,'提示不正确或没有提示')
        except Exception:
            self.login.saveScreenShot('%s_fail.png'%(sys._getframe().f_code.co_name))
            time.sleep(1)
            raise
        else:
            self.login.saveScreenShot('%s_pass.png'%(sys._getframe().f_code.co_name))
            time.sleep(1)
            log.logger.info('%s test completed '%(sys._getframe().f_code.co_name))





















