from flask import render_template
from app.tmpl import tmpl

projects = []
for i in range(10):
    json = {
        'pName': '项目' + str(i),
        'pType': '类型' + str(i)
    }
    projects.append(json)

'''
@tmpl.context_processor 只在本模块的范围内有效
'''
tmpl.context_processor(lambda: dict(titel='模版的学习'))

#
# @tmpl.context_processor
# def context_title():
#     return dict(titel='模版学习')


'''
@tmpl.app_context_processor 可跨模块范围有效
'''


@tmpl.app_context_processor
def context_title():
    return dict(app_titel='模版学习')


@tmpl.route('/tmpl/index')
def tmpl_index():
    return render_template('/tmpl/home.html', projects=projects)
