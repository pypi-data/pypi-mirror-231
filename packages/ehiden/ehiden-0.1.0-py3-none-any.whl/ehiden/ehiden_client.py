import requests
import lxml.html
import json
from datetime import datetime
import time


class EhidenClient:
    def login(self, username, password, userType='2'):
        """
        ログイン
        Args:
            username: ユーザー名
            password: パスワード
            userType: ユーザータイプ
        Returns:
            bool: ログイン成功
        """
        login_data = {
            'username': username,
            'password': password,
            'userType': userType,
            'omit': 'true',
            'kcKey': '',
            'uk': 'false',
            'directIraiMosikomiFlg': 'false',
            'hikyakuTakuhaibinDisplayFlg': '',
            'svc': '',
            'dourl': '',
            'p': '',
        }
        session = requests.Session()
        res = session.get(('https://www.e-service.sagawa-exp.co.jp/'))
        html = lxml.html.fromstring(res.text)
        form = html.xpath('//form')[0]
        login_res = session.post(form.get('action'), data=login_data)
        # ログイン失敗
        if login_res.status_code != 200 or login_res.url != 'https://www.e-service.sagawa-exp.co.jp/a/wtx/':
            raise Exception('Login Failed. Check your username and password.')

        # e-hidenへのログイン
        e_hiden_res1 = session.get('https://www.e-service.sagawa-exp.co.jp/a/wtx/rest/wtx/sso/login')
        e_hiden_res2 = session.get('https://e-hiden3.sagawa-exp.co.jp/a/nsx/rest/rdev/service/sso/login')
        if e_hiden_res1.status_code != 200 or not e_hiden_res1.url.startswith('https://www.e-service.sagawa-exp.co.jp/a/wtx/spastart.jsp?wi='):
            raise Exception('Login Failed')
        e_hiden_res3 = session.get('https://e-hiden3.sagawa-exp.co.jp/a/nsx/rest/rdev/service/auth/login')
        # cert_info の設定
        self.cert_info = e_hiden_res3.json()
        # default_headers の設定
        self.default_headers = {
            'authorization': f'Bearer {self.cert_info["at"]}',
            'origin': 'https://e-hiden3.sagawa-exp.co.jp',
            'referer': e_hiden_res2.url,
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            'wt': self.cert_info['data']['wt'],
            'x-rdev-csrf-token': self.cert_info['data']['RDEV-CSRF-Token'],
            'x-requested-with': 'XMLHttpRequest',
        }
        # session の設定
        self.session = session
        return True


    def check_login_status(self):
        """
        ログイン状態の取得
        Returns:
            bool: ログイン状態
        """
        res = self.session.post('https://e-hiden3.sagawa-exp.co.jp/a/nsx/rest/rdev/service/transition/check/NSDIIM01D01/check', headers=self.default_headers, json={})
        if res.status_code != 200 or res.json()['at'] != self.cert_info['at']:
            raise Exception('Failed to get login status.')
        return True


    def dm_create_empty(self):
        """
        dm用の空データを作成
        Returns:
            dict: dm伝票の情報
        """
        ns_data = self.session.post('https://e-hiden3.sagawa-exp.co.jp/a/nsx/rest/rdev/service/general/NSDIIM01B01', json={'mailbinSeniEventKbn':1}, headers=self.default_headers).json()
        base_data ={
            "mailbinSeniEventKbn": "1",
            "mailbinRrkNo": None,
            "mailbinTorokuDd": None,
            "mailbinSrkKbn": "forward",
            "mailbinUpdKbn": "1",
            "mailbinExclcnt": None,
            "mailbinRrkNoList": None,
            "otdkSkCd": None,
            "otdkSkTel": None,
            "otdkSkYbn": None,
            "otdkSkJsy1": None,
            "otdkSkJsy2": None,
            "otdkSkJsy3": None,
            "otdkSkNm1": None,
            "otdkSkNm2": None,
            "otdkSkNm3": None,
            "otdkSkGrpNmSelectValue": None,
            "nsCd": None,
            "nsJsy1": None,
            "nsJsy2": None,
            "nsNm1": None,
            "nsNm2": None,
            "nsTel": None,
            "otdkskJyusyoJiscd": None,
            "otdkskJyusyoJis2cd": None,
            "otdkskJyusyoJis5cd": None,
            "otdkskJyusyoJis8cd": None,
            "jyusyoInfoYubin": None,
            "egysyoTenCd": None,
            "tenNm": None,
            "nsYbn": None,
            "nsSsanTencd": None
        }
        for key in base_data.keys():
            if key in ns_data['data']:
                base_data[key] = ns_data['data'][key]
        return base_data


    def dm_check_data(self, otdkSkJsy1=None, otdkSkJsy2=None, otdkSkJsy3=None, otdkSkNm1=None, otdkSkNm2=None, otdkSkTel=None, otdkSkYbn=None, otdkSkGrpNmSelectValue=None):
        """
        お届け先情報のチェック
        Args:
            otdkSkJsy1: お届け先住所1(必須)
            otdkSkJsy2: お届け先住所2
            otdkSkJsy3: お届け先住所3
            otdkSkNm1: お届け先名1(必須)
            otdkSkNm2: お届け先名2
            otdkSkTel: お届け先電話番号
            otdkSkYbn: お届け先郵便番号
            otdkSkGrpNmSelectValue: お届け先グループ名
        Returns:
            dict: dm伝票の情報
        """
        dm_data  = {
            'otdkSkJsy1': otdkSkJsy1,
            'otdkSkJsy2': otdkSkJsy2,
            'otdkSkJsy3': otdkSkJsy3,
            'otdkSkNm1': otdkSkNm1,
            'otdkSkNm2': otdkSkNm2,
            'otdkSkTel': otdkSkTel,
            'otdkSkYbn': otdkSkYbn,
            'otdkSkGrpNmSelectValue': otdkSkGrpNmSelectValue,
            'nsCd': self.cert_info['data']['userInfo']['nsCdLs'][0],
        }
        return self.session.post('https://e-hiden3.sagawa-exp.co.jp/a/nsx/rest/rdev/service/general/NSDIIM01B05', json=dm_data, headers=self.default_headers).json()


    def dm_register(self, otdkSkCd=None, otdkSkJsy1=None, otdkSkJsy2=None, otdkSkJsy3=None, otdkSkNm1=None, otdkSkNm2=None, otdkSkTel=None, otdkSkYbn=None, otdkSkGrpNmSelectValue=None):
        """
        お届け先情報の登録
        Args:
            otdkSkCd: お届け先コード
            otdkSkJsy1: お届け先住所1(必須)
            otdkSkJsy2: お届け先住所2
            otdkSkJsy3: お届け先住所3
            otdkSkNm1: お届け先名1(必須)
            otdkSkNm2: お届け先名2
            otdkSkTel: お届け先電話番号
            otdkSkYbn: お届け先郵便番号
            otdkSkGrpNmSelectValue: お届け先グループ名
        Returns:
            dict: dm伝票の情報
            {
                "mailbinRrkNo": "0000000000",
                "mailbinTorokuDd": "20210101",
                "mailbinExclcnt": "1",
            }
        """
        checked_data = self.dm_check_data(otdkSkJsy1, otdkSkJsy2, otdkSkJsy3, otdkSkNm1, otdkSkNm2, otdkSkTel, otdkSkYbn, otdkSkGrpNmSelectValue)
        # print(json.dumps(checked_data, ensure_ascii=False, indent=2))
        if 'errorInfo' in checked_data:
            error_info = checked_data['errorInfo']
            raise Exception('Failed to check dm data. ' + str(error_info))
        # お届け先情報の作成
        dm_data = self.dm_create_empty()
        for key in dm_data.keys():
            if key in checked_data['data']:
                dm_data[key] = checked_data['data'][key]
        dm_data['otdkSkCd'] = otdkSkCd
        dm_data['otdkSkJsy1'] = otdkSkJsy1
        dm_data['otdkSkJsy2'] = otdkSkJsy2
        dm_data['otdkSkJsy3'] = otdkSkJsy3
        dm_data['otdkSkNm1'] = otdkSkNm1
        dm_data['otdkSkNm2'] = otdkSkNm2
        dm_data['otdkSkTel'] = otdkSkTel
        dm_data['otdkSkYbn'] = checked_data['data']['jyusyoInfoYubin']

        response = self.session.post('https://e-hiden3.sagawa-exp.co.jp/a/nsx/rest/rdev/service/general/NSDIIM01B06', json=dm_data, headers=self.default_headers)
        if response.status_code != 200 or len(response.json()['data']['mailbinRrkNoList']) == 0:
            raise Exception('Failed to regist dm data.')
        return response.json()['data']['mailbinRrkNoList'][0]


    def dm_get_all(self):
        """
        全てのdm伝票を取得する
        Returns:
            list[dict]: dm伝票のリスト
        """
        post_data = {
            "errDNomi": False,
            "otdkSkGrpNm": "",
            "otdkSkCdFrom": "",
            "otdkSkCdTo": "",
            "otdkSkNm": "",
            "otdkSkJsy": "",
            "otdkSkTdfkn": []
        }
        ret = self.session.post('https://e-hiden3.sagawa-exp.co.jp/a/nsx/rest/rdev/service/general/NSDIIP01B02', json=post_data, headers=self.default_headers).json()
        return ret['data']['searchResultList']


    def dm_print_all(self):
        """
        全てのdm伝票を印刷する
        Returns:
            (bytearray): PDFデータ
            (list[dict]): 印刷した伝票の情報
        """
        mailbinRrkNoList = []
        for post_data3 in self.dm_get_all():
            mailbinRrkNoList.append({
                "mailbinRrkNo": post_data3['rowmailbinRrkNo'],
                "mailbinTorokuDd": post_data3['rowtrkDd'],
                "mailbinExclcnt": post_data3['rowmailbinExclCnt'],
            })
        assert len(mailbinRrkNoList) > 0
        return self.dm_print(mailbinRrkNoList)


    def dm_print(self, mailbinRrkNoList):
        """
        dm伝票を印刷する
        Args:
            mailbinRrkNoList:dm伝票のリスト
            {
                "mailbinRrkNo": "0000000000",
                "mailbinTorokuDd": "20210101",
                "mailbinExclcnt": "1",
            }
        Returns:
            (bytearray): PDFデータ
            (list[dict]): 印刷した伝票の情報
        """
        assert len(mailbinRrkNoList) > 0
        # 発行件数の取得
        post_data1 = {
            "seniMotoGamenId": "NSDIIP01D01",
            "mailbinRrkNoList": mailbinRrkNoList,
        }
        res1 = self.session.post('https://e-hiden3.sagawa-exp.co.jp/a/nsx/rest/rdev/service/general/NSDIIM02B01', json=post_data1, headers=self.default_headers).json()
        lblHakKensu = res1['data']['lblHakKensu']
        lblHakSosu = res1['data']['lblHakSosu']
        mailbinLblRiyoSetKbn = res1['data']['mailbinLblRiyoSetKbn']
        # 印刷枚数と順位の設定
        post_data2 =  {
            "seniMotoGamenId": "NSDIIP01D01",
            "mailbinRrkNoList": mailbinRrkNoList,
            "lblHakKensu": lblHakKensu,
            "lblHakSosu": lblHakSosu,
            "kokyaCdJynChk": False,
            "lblHakOutputjyn": "3",
            "mailbinJry": "2"
        }
        res2 = self.session.post('https://e-hiden3.sagawa-exp.co.jp/a/nsx/rest/rdev/service/general/NSDIIM02B02', json=post_data2, headers=self.default_headers).json()
        lblhakDd = datetime.now().strftime('%Y%m%d%H%M%S')
        post_data3 = res2['data']['mailbinDataSndInfo'][0].copy()
        post_data3['lblhakDd'] = lblhakDd
        post_data3['sndKaisu'] = 1
        post_data3['sosndKaisu'] = 1
        res3 = self.session.post('https://e-hiden3.sagawa-exp.co.jp/a/nsx/rest/rdev/service/general/NSDIIM03B01', json=post_data3, headers=self.default_headers).json()
        post_data4 = {
            "prtStIt": "1",
            "mailbinJry": "2",
            "mailbinInfo": res2['data']['mailbinInfo'],
            "mailbinLblRiyoSetKbn": res1['data']['mailbinLblRiyoSetKbn'],
            "mailbinYukNisu": "60",
            "mailbinTyusyutuJyoken": res2['data']['mailbinTyusyutuJyoken'],
            "gyomuYmd": res2['data']['gyomuYmd'],
            "lblHakKensu": res1['data']['lblHakKensu'],
            "mailbinHakDate": lblhakDd
        }
        res4 = self.session.post('https://e-hiden3.sagawa-exp.co.jp/a/nsx/rest/rdev/service/general/NSDIIM02B03', json=post_data4, headers=self.default_headers).json()
        for i in range(5):
            post_data5 = {'fileSeqNoList': res4['data']['cyhyoPrtResponse']['fileSeqNoList']}
            res5 = self.session.post('https://e-hiden3.sagawa-exp.co.jp/a/nsx/rest/rdev/service/general/NSDIIM02B05', json=post_data5, headers=self.default_headers).json()
            if res5['data']['prtDChkReturnCd'] == "0":
                break
            time.sleep(3)
        else:
            raise Exception('Failed to print.')
        # ダウンロード
        post_data6 = {"jsondata": json.dumps({'fileSeqNo':res4['data']['cyhyoPrtResponse']['fileSeqNoList'][0] }), 'wt':self.cert_info['data']['wt']}
        res6 = self.session.post('https://e-hiden3.sagawa-exp.co.jp/a/nsx/rest/rdev/service/NSDIIM02B06/directdownload', data=post_data6, headers={})
        try:
            json.loads(res6.text)
            raise Exception('Failed to download.')
        except:
            pass
        post_data7 = {
            'mailbinTyusyutuJyoken':  res2['data']['mailbinTyusyutuJyoken'],
            'gyomuYmd': res2['data']['gyomuYmd']
        }
        # 印刷済みにする
        res7 = self.session.post('https://e-hiden3.sagawa-exp.co.jp/a/nsx/rest/rdev/service/general/NSDIIM02B07', json=post_data7, headers=self.default_headers).json()
        return res6.content, res2['data']['mailbinInfo']


