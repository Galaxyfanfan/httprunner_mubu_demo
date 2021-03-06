"""
mubu - 当前Project名称;
login_test.py - 在创建文件的对话框中指定的文件名;
galaxy - 当前用户名;
2020/10/24 2:52 下午 
"""
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseMubuLogin(HttpRunner):
    config = (
        Config("testcase description")
            .variables(**{
            'host': 'https://mubu.com',
            'phone': 'xxx',
            'password': 'xxx'
        })
            .base_url('${host}')
            .export('data_unique_id', 'JwtToken', 'user_persistence')
            .verify(False)
    )

    teststeps = [
        Step(
            RunRequest("/")
                .get("/")
                .with_headers(
                **{
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:81.0) Gecko/20100101 Firefox/81.0",
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                    "accept-language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                    "accept-encoding": "gzip, deflate, br",
                    "upgrade-insecure-requests": "1",
                    "cache-control": "max-age=0",
                    "te": "trailers",
                }
            )
                .extract()
                .with_jmespath('cookies.data_unique_id', "data_unique_id")
                .validate()
                .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("/login")
                .get("/login")
                .with_headers(
                **{
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:81.0) Gecko/20100101 Firefox/81.0",
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                    "accept-language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                    "accept-encoding": "gzip, deflate, br",
                    "referer": "${host}/",
                    "upgrade-insecure-requests": "1",
                    "te": "trailers",
                }
            )
                .with_cookies(
                **{
                    "data_unique_id": "${data_unique_id}",
                    # "reg_entrance": "https%3A%2F%2Fmubu.com%2Flogin",
                    # "_ga": "GA1.2.393581119.1603338104",
                    # "_gid": "GA1.2.1468470317.1603338104",
                    "SLARDAR_WEB_ID": "3d967836-6cbd-439f-9b16-d3426cc6350d",
                    # "Hm_lvt_4426cbb0486a79ea049b4ad52d81b504": "1603338106",
                    # "Hm_lpvt_4426cbb0486a79ea049b4ad52d81b504": "1603374272",
                    "reg_focusId": "faae839f-3684-4668-b55e-175508c5be9",
                    "reg_prepareId": "175508c54d1-175508c54ca-4668-b55e-8c4cc23a991c",
                    "mubu_inner": "1",
                    "s_v_web_id": "kgka62xo_moCbdJQ2_5Fuf_4EBO_8WEd_8JqwkBNYPNKm",
                    "language": "en-US",
                    "country": "US",
                    "data-unique-id": "55729c10-146c-11eb-88df-75fccb220896",
                    # "csrf_token": "a170eeb3-dcb8-4801-8a35-4227ae1c8392",
                    "SESSION": "40d77cbd-f81c-4c8f-b018-85c4c3e6e94b",
                    "_gat": "1",
                }
            )
                .validate()
                .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("/login/password")
                .get("/login/password")
                .with_headers(
                **{
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:81.0) Gecko/20100101 Firefox/81.0",
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                    "accept-language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                    "accept-encoding": "gzip, deflate, br",
                    "referer": "${host}/login",
                    "upgrade-insecure-requests": "1",
                    "te": "trailers",
                }
            )
                .with_cookies(
                **{
                    "data_unique_id": "${data_unique_id}",
                    # "reg_entrance": "https%3A%2F%2Fmubu.com%2Flogin",
                    # "_ga": "GA1.2.393581119.1603338104",
                    # "_gid": "GA1.2.1468470317.1603338104",
                    "SLARDAR_WEB_ID": "28d88f82-64fe-45f3-a47f-77bfdd4c0912",
                    # "Hm_lvt_4426cbb0486a79ea049b4ad52d81b504": "1603338106",
                    # "Hm_lpvt_4426cbb0486a79ea049b4ad52d81b504": "1603374275",
                    "reg_focusId": "76176d95-2ea5-4aec-9761-175508ddf8e",
                    "reg_prepareId": "175508dda07-175508dd9c7-4aec-9761-7187bf8b79ba",
                    "mubu_inner": "1",
                    "s_v_web_id": "kgka62xo_moCbdJQ2_5Fuf_4EBO_8WEd_8JqwkBNYPNKm",
                    "language": "en-US",
                    "country": "US",
                    "data-unique-id": "55729c10-146c-11eb-88df-75fccb220896",
                    # "csrf_token": "a170eeb3-dcb8-4801-8a35-4227ae1c8392",
                    "SESSION": "40d77cbd-f81c-4c8f-b018-85c4c3e6e94b",
                    "_gat": "1",
                }
            )
                .validate()
                .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("/api/login/submit")
                .post("/api/login/submit")
                .with_headers(
                **{
                    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:81.0) Gecko/20100101 Firefox/81.0",
                    "accept": "application/json, text/javascript, */*; q=0.01",
                    "accept-language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                    "accept-encoding": "gzip, deflate, br",
                    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "x-requested-with": "XMLHttpRequest",
                    "content-length": "50",
                    "origin": "${host}",
                    "referer": "${host}/login/password",
                    "te": "trailers",
                }
            )
                .with_cookies(
                **{
                    "data_unique_id": "${data_unique_id}",
                    # "reg_entrance": "https%3A%2F%2Fmubu.com%2Flogin",
                    # "_ga": "GA1.2.393581119.1603338104",
                    # "_gid": "GA1.2.1468470317.1603338104",
                    "SLARDAR_WEB_ID": "7a0c881a-6a71-470c-8a30-dea50daba2ba",
                    # "Hm_lvt_4426cbb0486a79ea049b4ad52d81b504": "1603338106",
                    # "Hm_lpvt_4426cbb0486a79ea049b4ad52d81b504": "1603374277",
                    "reg_focusId": "76176d95-2ea5-4aec-9761-175508ddf8e",
                    "reg_prepareId": "175508dda07-175508dd9c7-4aec-9761-7187bf8b79ba",
                    "mubu_inner": "1",
                    "s_v_web_id": "kgka62xo_moCbdJQ2_5Fuf_4EBO_8WEd_8JqwkBNYPNKm",
                    "language": "en-US",
                    "country": "US",
                    "data-unique-id": "55729c10-146c-11eb-88df-75fccb220896",
                    # "csrf_token": "a170eeb3-dcb8-4801-8a35-4227ae1c8392",
                    "SESSION": "40d77cbd-f81c-4c8f-b018-85c4c3e6e94b",
                    "_gat": "1",
                }
            )
                .with_data(
                {"phone": "${phone}", "password": "${password}", "remember": "true"}
            )
                .teardown_hook('${custom_sleep(2)}')
                .extract()
                .with_jmespath('cookies."Jwt-Token"', 'JwtToken')  # 若中间有-，可以加""隔离，如cookies."Jwt-Token"
                .with_jmespath('cookies.user_persistence', 'user_persistence')
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.code", 0)
                .assert_equal("body.msg", None)
                .assert_equal('body.data.next', '/list')
        ),
    ]


if __name__ == "__main__":
    TestCaseMubuLogin().test_start()
