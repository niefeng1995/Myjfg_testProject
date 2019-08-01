from common.Myunit import StartEnd
from businessView.login_jinfengou import Login_jinfenggou
import unittest
import logging
class TestLogin(StartEnd):
    csv_file = '../data/account1.csv'
    logging.basicConfig(level=logging.INFO, filename='../logs/runlog.log',
                        format='%(asctime)s %(filename)s[line:%(lineno)d]%(levelname)s%(message)s')
    def test_001(self):
        logging.info('=====test_login_15979994517===========')
        l = Login_jinfenggou(self.driver)
        data =l.get_csv_data(self.csv_file,1)
        l.login_jinfenggou(data[0],data[1])
        self.assertTrue()
    def test_002(self):
        logging.info('=====test_login_error_password===========')
        l = Login_jinfenggou(self.driver)
        data =l.get_csv_data(self.csv_file,2)
        l.login_jinfenggou(data[0],data[1])
    def test_003(self):
        logging.info('=====test_login_error_account===========')
        l = Login_jinfenggou(self.driver)
        data = l.get_csv_data(self.csv_file,3)
        l.login_jinfenggou(data[0],data[1])
if __name__ == '__main__':
    unittest.main()