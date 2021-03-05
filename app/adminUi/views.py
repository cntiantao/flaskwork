from flask import render_template, flash, redirect, url_for
from app.adminUi import adminUi, db
from app.adminUi.forms import LoginForm


@adminUi.route('/adminUi')
@adminUi.route('/adminUi/')
@adminUi.route('/adminUi/main')
@adminUi.route('/adminUi/index')
@adminUi.route('/adminUi/index/main.html')
def adminUi_index_main():
    return render_template('/adminUi/index/main.html')


@adminUi.route('/adminUi/index/top.html')
def adminUi_index_top():
    sql = 'select id,title,icon,url as homepage,is_active,is_show from sys_menu where is_show=TRUE and pid=0 '
    topMenus = db.queryAll(sql)
    return render_template('/adminUi/index/top.html', menus=topMenus)


@adminUi.route('/adminUi/index/left', defaults={'top_menu_id': -1})
@adminUi.route('/adminUi/index/left/<int:top_menu_id>')
def adminUi_index_left(top_menu_id):
    '''
    :param top_menu_id:传递进来 top menu id，用于筛选左侧菜单项目
    :return:顶部菜单对应的左侧菜单
    '''

    if top_menu_id < 1:
        top_menu_id = 1
    # 根据顶部菜单传来的pid的值，来查对应顶部一级菜单下面的二级菜单
    sql = "select id,pid,title,icon,url,case is_active when 1 then 'active' when 0 then '' end as active ,is_show from sys_menu where is_show=TRUE and pid=%s"
    # navs是一个列表，每一个子元素都是一个二级菜单
    navs = db.queryAll(sql, [top_menu_id])
    # print(navs)
    leftNav = []
    for nav in navs:
        # 对每一个二级菜单进行循环，取得二级菜单下面的对应的三级菜单
        sql_t = "select id,pid,title,icon,url,case is_active when 1 then 'active' when 0 then '' end as active ,is_show from sys_menu where pid=%s"
        #menus是一个列表，每一个子元素都是一个三级菜单
        menus = db.queryAll(sql_t, nav['id'])
        #把三级菜单加入到二级菜单
        nav['menus'] = menus
        leftNav.append(nav)
        # print(menus)
    print(leftNav)
    sql_p="select id,pid,title,icon,url,case is_active when 1 then 'active' when 0 then '' end as active ,is_show from sys_menu where is_show=TRUE and id=%s"
    leftMenu=db.queryAll(sql_p,top_menu_id)
    leftMenu[0]['leftNav']=leftNav
    print(leftMenu[0])

    return render_template('/adminUi/index/left.html', leftMenu=leftMenu[0])


@adminUi.route('/adminUi/index/home.html')
def adminUi_index_home():
    return render_template('/adminUi/index/home.html')

@adminUi.route('/adminUi/index/welcome.html')
def adminUi_index_welcome():
    return render_template('/adminUi/index/welcome.html')



@adminUi.route('/adminUi/index/nav/left')
def adminUi_index_nav_left():
    return 'aa'


@adminUi.route('/adminUi/index/nav/top')
def adminUi_index_nav_top():
    return ''


@adminUi.route('/adminUi/index/login.html', methods=['GET', 'POST'])
def adminUi_index_login():
    formLogin = LoginForm()
    if formLogin.validate_on_submit():
        '''
        flask-wft 中的 formLogin.validate_on_submit()，相当于  wftForms 中：
        form.method==‘post’ and form.validate()  两个方法合一 
        '''
        flash('ddfd')
        '''
        这里进行登陆验证的过程
        '''
        username = formLogin.username.data
        password = formLogin.password.data
        # photo = formLogin.photo.data
        # photo_new_fileName= random_filename(photo.filename)
        # photo.save(os.path.join(adminUi.root_path,'uploads',photo_new_fileName))
        #
        # if "otherfiles" not in request.files:
        #     flash("多文件上传失败")
        #     return redirect(url_for('adminUi.adminUi_index_login'))
        # for f in request.files.getlist('otherFiles'):
        #     if f and allowed_file(f.filename):
        #         f.save(os.path.join(adminUi.root_path,'uploads',random_filename(f.filename)))

        print(username)
        print(password)
        # print(photo)

        isLoginOk = True
        if isLoginOk:  # 登陆成功
            return redirect(url_for('adminUi.adminUi_index_main'))
    else:
        return render_template('/adminUi/index/login.html', formLogin=formLogin)
