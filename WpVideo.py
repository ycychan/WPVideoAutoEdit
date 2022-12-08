# -*- coding: utf-8 -*-
# @Time    : 2022/12/8 18:34
# @Author  : dominoar
# @Email   : duominuoaier@gmail.com
# @File    : WpVideo.py
# @Software: PyCharm

import os
import re


class WpVideo:
    # 动漫根目录
    VIDEO_HOME = 'https://video.ycychan.com/Arime/'

    def __init__(self, open_path, save_path, article_nub, arime_name):
        self.open_path = open_path  # 打开的文件
        self.save_path = save_path  # 关闭的文件
        self.next_video = 2  # 指向下一集视频(视频是从第一集开始的)
        self.previous_video = 0  # 指向上一集视频
        self.the_video = 1  # 指向自己这条视频
        self.article_num = article_nub  # 文章号码
        self.diversity = 0  # 视频总集
        self.arime_name = arime_name + '/'

    def scan_dir_(self):
        """扫描目录所有文件，包括子目录文件"""
        g = os.walk(self.open_path)
        for path, dir_list, file_list in g:
            for file_name in file_list:
                if file_name.find('mp4') or file_name.find('MP4'):
                    yield os.path.join(path, file_name)  # 迭代处理

    def scan_dir(self):
        """扫描当前目录和文件，不会扫描子目录"""
        fileDir = os.sep.join([self.open_path])
        fileList = os.listdir(fileDir)
        self.diversity = len(fileList)
        for file in fileList:
            yield file  # 迭代处理

    def write_dom(self):
        file = open(self.save_path, 'w+', encoding='UTF-8')
        for file_url in self.scan_dir():
            #  剔除标题无用的内容,将会用于视频标题
            file_url_ = re.sub(r'[.*?]', '', re.sub('(.mp4)', '', file_url))
            file.write('\n')
            file.write('\n')
            file.write('<!-- wp:group {"layout":{"type":"constrained"}} -->')
            file.write('\n')
            file.write('<div class="wp-block-group"><!-- wp:heading -->')
            file.write('\n')
            file.write(f'<h2>{file_url_}</h2>')
            file.write('\n')
            file.write('<!-- /wp:heading -->')
            file.write('\n')
            file.write('\n')
            file.write('<!-- wp:video -->')
            file.write('\n')
            file.write(
                f'<figure class="wp-block-video"><video controls src="{self.VIDEO_HOME + self.arime_name + file_url}"></video></figure>')
            file.write('\n')
            file.write('<!-- /wp:video -->')
            file.write('\n')
            file.write('\n')
            file.write('<!-- wp:buttons {"layout":{"type":"flex","justifyContent":"space-between"}} -->')
            file.write('\n')
            file.write('<div class="wp-block-buttons"><!-- wp:button -->')
            file.write('\n')
            if self.the_video == 1:  # 如果为第一集（尝试过N种少量代码的方案，但是就是有点小问题，令我都非常不满意，放弃了。）
                file.write(
                    f'<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="javascript">已经到顶啦</a></div>')
                file.write('\n')
                file.write('<!-- /wp:button -->')
                file.write('\n')
                file.write('\n')
                file.write('<!-- wp:button -->')
                file.write('\n')
                file.write(
                    f'<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="https://video.ycychan.com/?p={self.article_num}&amp;page={self.next_video}">下一集</a></div>')

            elif self.the_video == self.diversity:  # 是否为最后一集
                file.write(
                    f'<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="https://video.ycychan.com/?p={self.article_num}&amp;\page={self.previous_video}">上一集</a></div>')
                file.write('\n')
                file.write('<!-- /wp:button -->')
                file.write('\n')
                file.write('\n')
                file.write('<!-- wp:button -->')
                file.write('\n')
                file.write(
                    f'<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="javascript">已经到底啦</a></div>')
            else:
                file.write(
                    f'<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="https://video.ycychan.com/?p={self.article_num}&amp;\page={self.previous_video}">上一集</a></div>')
                file.write('\n')
                file.write('<!-- /wp:button -->')
                file.write('\n')
                file.write('\n')
                file.write('<!-- wp:button -->')
                file.write('\n')
                file.write(
                    f'<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="https://video.ycychan.com/?p={self.article_num}&amp;page={self.next_video}">下一集</a></div>')
            file.write('\n')
            file.write('<!-- /wp:button --></div>')
            file.write('\n')
            file.write('<!-- /wp:buttons --></div>')
            file.write('\n')
            file.write('<!-- /wp:group -->')
            file.write('\n')
            file.write('<!-- wp:nextpage -->')
            file.write('\n')
            file.write('<!--nextpage-->')
            file.write('\n')
            file.write('<!-- /wp:nextpage -->')
            file.write('\n')
            self.next_video += 1
            self.previous_video += 1
            self.the_video += 1
