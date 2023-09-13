import HtmlTestRunner


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/home/priyansu/Desktop/testing/unifyng-automation-testing/UnifyNG/Reports"))

#path> python3 -m unittest login.py


#python3 -m UnifyNG.POM.Tests.login



if __name__ == "__main__":
    unittest.main()

n = 7
m = 10
name = ''.join(random.choices(string.ascii_lowercase, k=n))
randomName = str(name)
randomMobile = ''.join(random.choices(string.octdigits, k=m))
randomStrUpper = ''.join(random.choices(string.ascii_uppercase + string.digits, k=n))