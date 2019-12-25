import allure,pytest


class Test_01:
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    def test_01(self):
        assert True

    # @allure.step("这是一个测试步骤")
    # def test_02(self):
    #     pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    #     assert False
    #
    # @allure.step("这是一个测试步骤")
    # def test_03(self):
    #     pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    #     assert True
    #
    # @allure.step("这是一个测试步骤")
    # def test_04(self):
    #     pytest.allure.severity(pytest.allure.severity_level.MINOR)
    #     assert True
    #
    # @allure.step("这是一个测试步骤")
    # def test_05(self):
    #     pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    #     assert True



