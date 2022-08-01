# _*_ coding: utf-8 _*_ #
# @Time     :7/29/2022 4:34 PM
# @Author   :Huiming Shi

import os

project_abs_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# -------------------------获取不同的path------------------------- #
logHtml_path = os.path.join(project_abs_dir,'logHtml')

pictures_path = os.path.join(project_abs_dir,'pictures')

logs_path = os.path.join(project_abs_dir,'outFiles','logs')

screenShots_path = os.path.join(project_abs_dir,'outFiles','screenShots','截图--')

reports_path = os.path.join(project_abs_dir,'outFiles','reports','tmp')