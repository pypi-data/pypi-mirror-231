import requests
import pandas as pd
import re
import os
import json
import glob

ROOT = os.path.dirname(os.path.abspath(__file__))

def getDouBanComment(url, header): 
    """
    这个函数的功能是抓取豆瓣电影短评数据
    Args:
        url: 短评页面的URL地址
        header: 请求头
    Return:
        name, comment_time, comment_location, comment
    e.g.:
        >>> url = 'https://movie.douban.com/subject/35267224/comments?status=P'
        >>> header = {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
            }
        >>> getDouBanComment(url, header)
        (['谢明宏',
        '青绿的流水',
        '次等水货',
        ...
        如果改为智斗反派脱难的商业爽片估计更好看'])
    """
    # 发送请求，并获取相应
    response = requests.get(url, headers=header)
    # 解析评论
    comment = re.findall('<span class="short">(.*?)</span>', response.text, flags=re.S)
    # 抓取用户昵称
    name = re.findall('<div class="avatar">\n            <a title="(.*?)" href="', response.text, flags=re.S)
    # 抓取评论时间
    comment_time = re.findall('<span class="comment-time " title="(.*?)">', response.text, flags=re.S)
    # 抓取评论地点
    comment_location = re.findall('<span class="comment-location">(.*?)</span>', response.text, flags=re.S)
    return name, comment_time, comment_location, comment

def saveListStr2DataFrame(saveExcelPath=None, **kwargs):
    """
    保存多个字段到DataFrame并返回
    当saveExcelPath指定具体的Excel路径时，会将结果直接保存到Excel文件中，不返回内容
    Args:
        saveExcelPath: Excel路径， 当saveExcelPath指定具体的Excel路径时，会将结果直接保存到Excel文件中，不返回数据框
        **kwargs: DataFrame字段内容，columnName=columnValues
        
    Return:
        如果saveExcelPath=None(默认)，返回指定的数据框
        如果saveExcelPath!=None，无返回值

    Examples:
        >>> a1 = [1, 2, 3]
        >>> b1 = [4, 5, 6]
        >>> saveListStr2DataFrame(A=a1, B=b1)
            A	B
        0	1	4
        1	2	5
        2	3	6
    """
    data = pd.DataFrame(kwargs.values(), index=kwargs.keys()).T
    if saveExcelPath:
        data.to_excel(saveExcelPath, index=None)
        return 
    return data


def getSinaText(url, header={}):
    """
        获取新浪微博博文内容
        Args:
            url: 新浪微博博文数据包地址
            header: 请求头字典
        
        Retuen:
            max_id, screen_name, created_at, text_raw, reposts_count, comments_count, attitudes_count
            max_id: 下一页URL地址中的max_id字段
            screen_name: 博主昵称
            created_at: 博文发布时间
            text_raw: 博文内容
            reposts_count: 转发数
            comments_count: 评论数
            attitudes_count: 点赞数
        
        Examples:
            >>> url = 'https://weibo.com/ajax/feed/hottimeline?since_id=0&refresh=0&group_id=102803&containerid=102803&extparam=discover%7Cnew_feed&max_id=0&count=10'
            >>> getSinaText(url)
            (1,
             ['新华社',
              '捕月少女',
              '大数据查牌员'
              ...
    """
    response = requests.get(url, headers=header)
    response_dict = response.json()

    max_id = response_dict['max_id']
    text_raw = [i['text_raw'] for i in response_dict['statuses']]
    screen_name = [i['user']['screen_name'] for i in response_dict['statuses']]
    created_at = [i['created_at'] for i in response_dict['statuses']]
    reposts_count = [i['reposts_count'] for i in response_dict['statuses']]
    comments_count = [i['comments_count'] for i in response_dict['statuses']]
    attitudes_count = [i['attitudes_count'] for i in response_dict['statuses']]
    return max_id, screen_name, created_at, text_raw, reposts_count, comments_count, attitudes_count

def getSinaComment(url, header={}):
    """
        获取新浪微博博文评论内容
        Args:
            url: 新浪微博博文评论数据包地址
            header: 请求头字典
        
        Retuen:
            max_id, screen_name, created_at, text_raw
            max_id: 下一页URL地址中的max_id字段
            screen_name: 评论人昵称
            created_at: 评论实践
            text_raw: 评论内容
        
        Examples:
            >>> url = 'https://weibo.com/ajax/statuses/buildComments?is_reload=1&id=4940045989970652&is_show_bulletin=2&is_mix=0&count=10&uid=2836883273&fetch_level=0&locale=zh-CN'
            >>> header = {
                    "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
                    "cookie": "XSRF-TOKEN=n360u4rN64m8U_4BorSD8xAv; SUB=_2A25J-gNsDeThGeBM41sT9y7Kyj-IHXVqjnOkrDV8PUNbmtANLUv5kW9NRKwn9pbnmriKVevH_qsT9DFHf631YzOa; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5U7_hCLB2yxZo8QkxYAXSs5JpX5KzhUgL.FoqE1h.ES05ceKe2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMceon4eoM7So20; ALF=1725933244; SSOLoginState=1694397244; WBPSESS=wi7CfG2VcnaC63Kg8n7kwtsSt9BL87XyXiz2F3wAdeWP4TOIRUKIpv_oqRdHrjaRLCQOnpMk4zpexBxov_b58c8s130uJAsV_dUW1xUNAZvfTx8KcXiu4Q9qUBdgkspD1YVIDsbUuijuTGZ9_RhJJQ=="
                }
            >>> getSinaComment(url, headers=header)
            (138870126847611,
                ['墨客墨客y',
                '等待初心丶',
                '桑凡缇--sunfunty',
                '明天AxA',
                ...
    """
    response = requests.get(url, headers=header)
    response_dict = response.json()
    
    max_id = response_dict['max_id']
    # 获取评论人昵称
    screen_name = [i['user']['screen_name'] for i in response_dict['data']]
    # 评论时间
    created_at = [i['created_at'] for i in response_dict['data']]
    # 评论内容
    text_raw = [i['text_raw'] for i in response_dict['data']]
    return max_id, screen_name, created_at, text_raw

def get_stopword():
    """
        Return:
            返回停用词构成的列表
    """
    with open(os.path.join(ROOT, 'files', 'stopwords.txt'), 'r', encoding='UTF-8') as f:
        stopword = f.readlines()
    stopword = [i.strip() for i in stopword]
    return stopword

# 下载B站视频
class Get_Bilibili_Vedio:
    """
        B站视频下载类，可以下载单个视频和某个视频合集。
        需要注意的是B站中音视频是分开的，所以后面调用此类下载的也是音频和视频。
        如果你想要将音频和视频合并，可以调用`concatAV(inputpath='.', outputpath='ConcatResult')`
        但是也需要你提前去安装ffmpeg软件【https://ffmpeg.org/download.html】，并将ffmpeg的bin目录放入PATH系统环境变量中。

        Args:
            url: B站视频地址

        Return:
            下载好的视频，会在自动下载到当前文件夹。
            如果是单个视频那么会直接下载对应的视频和音频到当前文件夹；
            如果是视频全集那么会首先创建一个该视频的文件夹，然后再去下载所有的视频和音频到该文件夹。

        Examples:
            >>> url = 'https://www.bilibili.com/video/BV1hE411t7RN'
            >>> getBilibiliVedio = Get_Bilibili_Vedio(url)
        下载单个视频
            >>> getBilibiliVedio.download()
            Save: PyTorch深度学习快速入门教程（绝对通俗易懂！）【小土堆】.mp4
            获取[PyTorch深度学习快速入门教程（绝对通俗易懂！）【小土堆】]视频完毕！
            Save: PyTorch深度学习快速入门教程（绝对通俗易懂！）【小土堆】.mp3
            获取[PyTorch深度学习快速入门教程（绝对通俗易懂！）【小土堆】]音频完毕！
        下载视频全集
            >>> getBilibiliVedio.download(OnlyFlag=False)
            当前视频有33集。
            Save: PyTorch深度学习快速入门教程（绝对通俗易懂！）【小土堆】\1_P1. PyTorch环境的配置及安装（Configuration and Installation of PyTorch)【PyTorch教程】.mp4
            Save: PyTorch深度学习快速入门教程（绝对通俗易懂！）【小土堆】\1_P1. PyTorch环境的配置及安装（Configuration and Installation of PyTorch)【PyTorch教程】.mp3
            Save: PyTorch深度学习快速入门教程（绝对通俗易懂！）【小土堆】\2_P2. Python编辑器的选择、安装及配置（PyCharm、Jupyter安装）【PyTorch教程】.mp4
            Save: PyTorch深度学习快速入门教程（绝对通俗易懂！）【小土堆】\2_P2. Python编辑器的选择、安装及配置（PyCharm、Jupyter安装）【PyTorch教程】.mp3
    """
    def __init__(self, url, Cookie="buvid3=0C1ADF4F-53AA-F9DF-45F0-A826B382EDFB72960infoc; b_nut=1680506872; i-wanna-go-back=-1; _uuid=FF977C41-C53B-9C4D-AC7D-B1B28264A13F73972infoc; nostalgia_conf=-1; header_theme_version=CLOSE; CURRENT_PID=85375300-d29c-11ed-9423-1b0fe92a80c0; rpdid=|(RlRuu~k~Y0J'uY)|l)|lkk; CURRENT_QUALITY=80; LIVE_BUVID=AUTO8716808562932706; b_ut=5; FEED_LIVE_VERSION=V8; buvid4=B1F37553-1C32-BBE8-0181-1F9C3901F9CB74129-023040315-%2B6moO9JdWYBP6q7zlEAc7A%3D%3D; CURRENT_FNVAL=4048; buvid_fp_plain=undefined; home_feed_column=5; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTUzNDQ3NzcsImlhdCI6MTY5NTA4NTU3NywicGx0IjotMX0.sRI-9Z2SD1wsSbSoE6B5LYDj3SHWswLgV5cIerntRKk; bili_ticket_expires=1695344777; fingerprint=5f1a7b1f05034d9220e75e239b17f065; buvid_fp=e844bd76c7e8e3d828a696c670cbdb11; bp_video_offset_32636793=843440553716613156; browser_resolution=1745-838; b_lsid=1B101AEBC_18AB5DC44AC; SESSDATA=4cf24c26%2C1710820528%2Ccbecb%2A92CjCtEr5XGtIBAmVpgFkHYyj_V7tna7urtxz_WeHhtIjsLhmy2_XCE0eDJ-rqEUFJL8oSVjNRQjJXbWxSemxsb01BQlFEaGZsbEQza2hLSmRLbjkzaF80ZkdwYlBGWFNHdkdIZmFYRUJWcHY4TzVoa20zZVZkSG1TUmNXeEhFdGZmejhabmt6czh3IIEC; bili_jct=1b288ccf55ef2217a67e6814a2ef3893; DedeUserID=32636793; DedeUserID__ckMd5=622f1525d2637f75; sid=7xwah286"):
        self.url = url
        # 设置请求头
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36',
            'Cookie': Cookie,
            'referer': self.url  # 设置防盗链，告诉请求是从哪个网站过来的
        }
    
    def __get_res(self, url):
        res = requests.get(url, headers=self.headers)
        return res

    def __parse_av(self, res):
        title = re.findall('<title data-vue-meta="true">(.*?)</title>', res.text)[0].split('_')[0].replace(' ', '_')
        title = re.sub('[/\\:*?"<>|]', '', title)
        data = re.findall('<script>window.__playinfo__=(.*?)</script>', res.text)[0]
        data = json.loads(data)  # 将json格式数据转化为字典
        video_url = data['data']['dash']['video'][0]['baseUrl']
        audio_url = data['data']['dash']['audio'][0]['baseUrl']
        return title, video_url, audio_url
    
    def __parse_av_all(self, res):
        title = re.findall('<title data-vue-meta="true">(.*?)</title>', res.text)[0].split('_')[0].replace(' ', '_')
        title = re.sub('[/\\:*?"<>|]', '', title)
        data = re.findall('"pages":\[(.*?)\],"subtitle":', res.text)[0]
        data = json.loads('{"data":[' + data + ']}')
        vedios = [(i['page'], i['part']) for i in data['data']]
        return title, vedios
    
    def __parse_av_all2(self, res):
        title = re.findall('target="_blank" title="(.*?)" class="first-line-title', res.text)[0]
        title = re.sub('[/\\:*?"<>| ]', '', title)
        data = re.findall('"type":1,("episodes":.*?),"isActive":', res.text)[0]
        data = json.loads('{' + data + '}')
        vedios = [(i['bvid'], i['title']) for i in data['episodes']]
        return title, vedios

    def __save_data(self, binary_data, name, data_type='v'):
        if data_type == 'v':
            print('Saving: ' + name + '.mp4')
            with open(name + '.mp4', 'wb') as f:
                f.write(binary_data)
        elif data_type == 'a':
            print('Saving: ' + name + '.mp3')
            with open(name + '.mp3', 'wb') as f:
                f.write(binary_data)
                
    def download(self, OnlyFlag=True):
        res = self.__get_res(self.url)
        if OnlyFlag:
            title, video_url, audio_url = self.__parse_av(res)
            binary_video = self.__get_res(video_url).content
            binary_audio = self.__get_res(audio_url).content
            self.__save_data(binary_video, title)
            print('获取[%s]视频完毕！' % title)
            self.__save_data(binary_audio, title, 'a')
            print('获取[%s]音频完毕！' % title)
        else:
            isCollection = ('<span class="cur-page">' in res.text) and ('视频选集' in res.text)
            if isCollection:
                title, vedios = self.__parse_av_all(res)
                print('经过检测当前视频为【选集】内容，共有%d个视频。' % len(vedios))
            else:
                title, vedios = self.__parse_av_all2(res)
                print('经过检测当前视频为【专栏】内容，共有%d个视频。' % len(vedios))
            if not os.path.exists(title):
                os.mkdir(title)
                downloaded_list = []
            else:
                downloaded_list = os.listdir(title)
            for num, (i, j) in enumerate(vedios):
                j = re.sub(r'[/\\ ]', '_', j)
                if isCollection:
                    vedio_path = title + '\\' + str(i) + '_' + j
                    tmp_url = self.url + '?p=' + str(i)
                else:
                    vedio_path = title + '\\' + str(num) + '_' + j
                    tmp_url = 'https://www.bilibili.com/video/' + str(i)
                tmp_res = self.__get_res(tmp_url)
                _, video_url, audio_url = self.__parse_av(tmp_res)
                print(f'- 正在请求{j}')
                if (j + '.mp4') not in downloaded_list:
                    self.__save_data(self.__get_res(video_url).content, vedio_path)
                else:
                    print('>>> ' + (j + '.mp4') + '已下载')
                if (j + '.mp3') not in downloaded_list:
                    self.__save_data(self.__get_res(audio_url).content, vedio_path, data_type='a')
                else:
                    print('>>> ' + (j + '.mp3') + '已下载')
                
def concatAV(inputpath='.', outputpath='ConcatResult'):
    """
        用于合并音频和视频
        
        Args:
            inputpath: 音视频存放地址，默认为当前路径下。
            outputpath: 合并后的音视频输出地址，默认会在当前路径下创建一个ConcatResult文件夹
        
        Return:
            将合并后的视频放入outputpath目录下。
    """
    if inputpath == outputpath:
        raise ValueError('输入输出地址不能一致。')
    a_list = [i for i in os.listdir(inputpath) if i.endswith('.mp3')]
    v_list = [i for i in os.listdir(inputpath) if i.endswith('.mp4')]
    if len(a_list) != len(v_list):
        raise ValueError(f'{inputpath} 目录下视频和音频数量不一致，请删除无关音视频然后重新操作。')
    if not os.path.exists(outputpath):
        os.makedirs(outputpath)
    for i in range(len(a_list)):
        file1 = os.path.join(inputpath, a_list[i])
        file2 = os.path.join(inputpath, v_list[i])
        result = outputpath + '//' + v_list[i]
        # 合并音视频
        os.system(f"ffmpeg -i {file1} -i {file2} -acodec copy -vcodec copy {result}")
        try:
            # 删除已经合并的音视频
            os.remove(file1)
            os.remove(file2)
        except:
            print(f"{file1}删除失败，请手动删除！")
        print(f'Concat： {file2} TO {result}')

if __name__ == '__main__':
    # url = 'https://www.bilibili.com/video/BV1ov411M7xL'
    url = 'https://www.bilibili.com/video/BV1hE411t7RN'
    b = Get_Bilibili_Vedio(url)
    b.download(False)
