# _*_ encoding:utf-8 _*_
__author__ = 'lizhe'
__time__ = '2018/05/06 17:42'
from lxml import etree

text='''
<div class="content_left">

                <!-- 依次填入左侧各个模块 -->

                <!--当前为公司标签时，隐藏筛选条件栏-->
                <div id="positionHead" class="">

                    <!-- 公司卡片 -->

                    

                    <!-- 筛选 -->

                    <ul id="filterBox" class="filter-wrapper">
    <input id="filterOption" type="hidden" value="1">

        <li class="li-taller brief dn" id="filterBrief">
        <span class="title">工作地点：</span>
                    <a rel="nofollow" href="javascript:;" class="active">全国</a>
        
        
        <span class="title">工作经验：</span>
                <a rel="nofollow" href="javascript:;" class="active">不限</a>
        
        <span class="title">学历要求：</span>
                <a rel="nofollow" href="javascript:;" class="active">不限</a>
        
        <span class="title">融资阶段：</span>
                <a rel="nofollow" href="javascript:;" class="active">不限</a>
        
        <span class="title">行业领域：</span>
                <a rel="nofollow" href="javascript:;" class="active">不限</a>
            </li>
    
        <div class="details" id="filterCollapse">
        <div class="has-more">
            <div class="more more-positions workPosition">
                <li class="hot">
                    <span class="title">工作地点：</span>
                                                            <a rel="nofollow" href="javascript:;" class="active" data-lg-tj-id="8p00" data-lg-tj-no="
                                                            0001
                                                    " data-lg-tj-cid="idnull" data-id="">全国</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8p00" data-lg-tj-no="
                                                            0002
                                                    " data-lg-tj-cid="idnull" data-id="5" class="more-city-name">北京</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8p00" data-lg-tj-no="
                                                            0003
                                                    " data-lg-tj-cid="idnull" data-id="6" class="more-city-name">上海</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8p00" data-lg-tj-no="
                                                            0004
                                                    " data-lg-tj-cid="idnull" data-id="765" class="more-city-name">深圳</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8p00" data-lg-tj-no="
                                                            0005
                                                    " data-lg-tj-cid="idnull" data-id="763" class="more-city-name">广州</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8p00" data-lg-tj-no="
                                                            0006
                                                    " data-lg-tj-cid="idnull" data-id="653" class="more-city-name">杭州</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8p00" data-lg-tj-no="
                                                            0007
                                                    " data-lg-tj-cid="idnull" data-id="801" class="more-city-name">成都</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8p00" data-lg-tj-no="
                                                            0008
                                                    " data-lg-tj-cid="idnull" data-id="635" class="more-city-name">南京</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8p00" data-lg-tj-no="
                                                            0009
                                                    " data-lg-tj-cid="idnull" data-id="736" class="more-city-name">武汉</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8p00" data-lg-tj-no="
                                                            0010
                                                    " data-lg-tj-cid="idnull" data-id="854" class="more-city-name">西安</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8p00" data-lg-tj-no="
                                                            0011
                                                    " data-lg-tj-cid="idnull" data-id="682" class="more-city-name">厦门</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8p00" data-lg-tj-no="
                                                            0012
                                                    " data-lg-tj-cid="idnull" data-id="749" class="more-city-name">长沙</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8p00" data-lg-tj-no="
                                                            0013
                                                    " data-lg-tj-cid="idnull" data-id="639" class="more-city-name">苏州</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8p00" data-lg-tj-no="
                                                            0014
                                                    " data-lg-tj-cid="idnull" data-id="7" class="more-city-name">天津</a>
                                                        </li>
                <li class="other">
                                                            <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0001
                                                    " data-lg-tj-cid="idnull" data-id="8" class="more-city-name">重庆</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0002
                                                    " data-lg-tj-cid="idnull" data-id="719" class="more-city-name">郑州</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0003
                                                    " data-lg-tj-cid="idnull" data-id="703" class="more-city-name">青岛</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0004
                                                    " data-lg-tj-cid="idnull" data-id="664" class="more-city-name">合肥</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0005
                                                    " data-lg-tj-cid="idnull" data-id="681" class="more-city-name">福州</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0006
                                                    " data-lg-tj-cid="idnull" data-id="702" class="more-city-name">济南</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0007
                                                    " data-lg-tj-cid="idnull" data-id="600" class="more-city-name">大连</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0008
                                                    " data-lg-tj-cid="idnull" data-id="766" class="more-city-name">珠海</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0009
                                                    " data-lg-tj-cid="idnull" data-id="636" class="more-city-name">无锡</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0010
                                                    " data-lg-tj-cid="idnull" data-id="768" class="more-city-name">佛山</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0011
                                                    " data-lg-tj-cid="idnull" data-id="779" class="more-city-name">东莞</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0012
                                                    " data-lg-tj-cid="idnull" data-id="654" class="more-city-name">宁波</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0013
                                                    " data-lg-tj-cid="idnull" data-id="638" class="more-city-name">常州</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0014
                                                    " data-lg-tj-cid="idnull" data-id="599" class="more-city-name">沈阳</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0015
                                                    " data-lg-tj-cid="idnull" data-id="565" class="more-city-name">石家庄</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0016
                                                    " data-lg-tj-cid="idnull" data-id="831" class="more-city-name">昆明</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0017
                                                    " data-lg-tj-cid="idnull" data-id="691" class="more-city-name">南昌</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0018
                                                    " data-lg-tj-cid="idnull" data-id="785" class="more-city-name">南宁</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0019
                                                    " data-lg-tj-cid="idnull" data-id="622" class="more-city-name">哈尔滨</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0020
                                                    " data-lg-tj-cid="idnull" data-id="799" class="more-city-name">海口</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0021
                                                    " data-lg-tj-cid="idnull" data-id="780" class="more-city-name">中山</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0022
                                                    " data-lg-tj-cid="idnull" data-id="773" class="more-city-name">惠州</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0023
                                                    " data-lg-tj-cid="idnull" data-id="822" class="more-city-name">贵阳</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0024
                                                    " data-lg-tj-cid="idnull" data-id="613" class="more-city-name">长春</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0025
                                                    " data-lg-tj-cid="idnull" data-id="576" class="more-city-name">太原</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0026
                                                    " data-lg-tj-cid="idnull" data-id="656" class="more-city-name">嘉兴</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0027
                                                    " data-lg-tj-cid="idnull" data-id="710" class="more-city-name">泰安</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0028
                                                    " data-lg-tj-cid="idnull" data-id="" class="more-city-name">昆山</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0029
                                                    " data-lg-tj-cid="idnull" data-id="707" class="more-city-name">烟台</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0030
                                                    " data-lg-tj-cid="idnull" data-id="864" class="more-city-name">兰州</a>
                                                                                <a rel="nofollow" href="javascript:;" data-lg-tj-id="8q00" data-lg-tj-no="
                                                            0031
                                                    " data-lg-tj-cid="idnull" data-id="685" class="more-city-name">泉州</a>
                                                            <a rel="nofollow" href="javascript:;" id="all_city">全部城市 &gt; </a>
                </li>
            </div>

            <!-- 处理工作地点深层选择 -->
            <div class="choose-detail">
                <li class="position-head">

                    <div class="current-handle-position">
                        <span class="title">工作地点：</span>
                                                    <a class="current_city current">全国</a>
                        
                                                

                                                                                
                                                
                    </div>

                    <div class="other-hot-city">
                        <div class="city-wrapper dn" style="margin-left: 132px; width: 740px; overflow: hidden; display: block;">
                                                                                                                                                                                                                                                                    <a data-id="5" class="hot-city-name">北京</a>
                                                                                                                                                                                                        <a data-id="6" class="hot-city-name">上海</a>
                                                                                                                                                                                                        <a data-id="765" class="hot-city-name">深圳</a>
                                                                                                                                                                                                        <a data-id="763" class="hot-city-name">广州</a>
                                                                                                                                                                                                        <a data-id="653" class="hot-city-name">杭州</a>
                                                                                                                                                                                                        <a data-id="801" class="hot-city-name">成都</a>
                                                                                                                                                                                                        <a data-id="635" class="hot-city-name">南京</a>
                                                                                                                                                                                                        <a data-id="736" class="hot-city-name">武汉</a>
                                                                                                                                                                                                        <a data-id="854" class="hot-city-name">西安</a>
                                                                                                                                                                                                        <a data-id="682" class="hot-city-name">厦门</a>
                                                                                                                                                                                                        <a data-id="749" class="hot-city-name">长沙</a>
                                                                                                                                                                                                        <a data-id="639" class="hot-city-name">苏州</a>
                                                                                                                                                                                                        <a data-id="7" class="hot-city-name">天津</a>
                                                                                                                        </div>
                        <a rel="nofollow" class="btn-more" href="javascript:;">更多 <i></i></a>
                    </div>

                </li>

                
                
                
                
                                

                
                

            </div>
        </div>
                <li class="multi-chosen"><span class="title">工作经验：</span>
                                                    <a rel="nofollow" href="javascript:;" class="active" data-lg-tj-id="8r00" data-lg-tj-no="
                                                            0001
                                                    " data-lg-tj-cid="idnull">不限
            </a>
                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8r00" data-lg-tj-no="
                                                                    0002
                                                            " data-lg-tj-cid="idnull">应届毕业生                            <i class="delete"></i>

                </a>
                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8r00" data-lg-tj-no="
                                                                    0003
                                                            " data-lg-tj-cid="idnull">3年及以下                            <i class="delete"></i>

                </a>
                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8r00" data-lg-tj-no="
                                                                    0004
                                                            " data-lg-tj-cid="idnull">3-5年                            <i class="delete"></i>

                </a>
                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8r00" data-lg-tj-no="
                                                                    0005
                                                            " data-lg-tj-cid="idnull">5-10年                            <i class="delete"></i>

                </a>
                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8r00" data-lg-tj-no="
                                                                    0006
                                                            " data-lg-tj-cid="idnull">10年以上                            <i class="delete"></i>

                </a>
                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8r00" data-lg-tj-no="
                                                                    0007
                                                            " data-lg-tj-cid="idnull">不要求                            <i class="delete"></i>

                </a>
                                                </li>

        <li class="multi-chosen"><span class="title">学历要求：</span>

                                    <a rel="nofollow" href="javascript:;" class="active" data-lg-tj-id="8s00" data-lg-tj-no="
                                                            0001
                                                    " data-lg-tj-cid="idnull">不限
            </a>
                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8s00" data-lg-tj-no="
                                                                    0002
                                                            " data-lg-tj-cid="idnull">大专
                            <i class="delete"></i>
                </a>
                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8s00" data-lg-tj-no="
                                                                    0003
                                                            " data-lg-tj-cid="idnull">本科
                            <i class="delete"></i>
                </a>
                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8s00" data-lg-tj-no="
                                                                    0004
                                                            " data-lg-tj-cid="idnull">硕士
                            <i class="delete"></i>
                </a>
                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8s00" data-lg-tj-no="
                                                                    0005
                                                            " data-lg-tj-cid="idnull">博士
                            <i class="delete"></i>
                </a>
                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8s00" data-lg-tj-no="
                                                                    0006
                                                            " data-lg-tj-cid="idnull">不要求
                            <i class="delete"></i>
                </a>
                                        
        </li>
        <li class="multi-chosen"><span class="title">融资阶段：</span>
                                    <a rel="nofollow" href="javascript:;" class="active" data-lg-tj-id="8t00" data-lg-tj-no="
                                                            0001
                                                    " data-lg-tj-cid="idnull">不限
            </a>
                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8t00" data-lg-tj-no="
                                                                    0002
                                                            " data-lg-tj-cid="idnull">未融资
                            <i class="delete"></i>
                </a>
                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8t00" data-lg-tj-no="
                                                                    0003
                                                            " data-lg-tj-cid="idnull">天使轮
                            <i class="delete"></i>
                </a>
                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8t00" data-lg-tj-no="
                                                                    0004
                                                            " data-lg-tj-cid="idnull">A轮
                            <i class="delete"></i>
                </a>
                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8t00" data-lg-tj-no="
                                                                    0005
                                                            " data-lg-tj-cid="idnull">B轮
                            <i class="delete"></i>
                </a>
                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8t00" data-lg-tj-no="
                                                                    0006
                                                            " data-lg-tj-cid="idnull">C轮
                            <i class="delete"></i>
                </a>
                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8t00" data-lg-tj-no="
                                                                    0007
                                                            " data-lg-tj-cid="idnull">D轮及以上
                            <i class="delete"></i>
                </a>
                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8t00" data-lg-tj-no="
                                                                    0008
                                                            " data-lg-tj-cid="idnull">上市公司
                            <i class="delete"></i>
                </a>
                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8t00" data-lg-tj-no="
                                                                    0009
                                                            " data-lg-tj-cid="idnull">不需要融资
                            <i class="delete"></i>
                </a>
                                                </li>
        <div class="has-more hy-area">
            <li class="multi-chosen">
                <span class="title">行业领域：</span>
                                                <a rel="nofollow" href="javascript:;" class="active" data-lg-tj-id="8u00" data-lg-tj-no="
                                                            0001
                                                    " data-lg-tj-cid="idnull">不限
                </a>
                                                                                        <a rel="nofollow" href="javascript:;" data-lg-tj-id="8u00" data-lg-tj-no="
                                                                    0002
                                                            " data-lg-tj-cid="idnull">移动互联网
                            <i class="delete"></i>
                    </a>
                                                                                                            <a rel="nofollow" href="javascript:;" data-lg-tj-id="8u00" data-lg-tj-no="
                                                                    0003
                                                            " data-lg-tj-cid="idnull">电子商务
                            <i class="delete"></i>
                    </a>
                                                                                                            <a rel="nofollow" href="javascript:;" data-lg-tj-id="8u00" data-lg-tj-no="
                                                                    0004
                                                            " data-lg-tj-cid="idnull">金融
                            <i class="delete"></i>
                    </a>
                                                                                                            <a rel="nofollow" href="javascript:;" data-lg-tj-id="8u00" data-lg-tj-no="
                                                                    0005
                                                            " data-lg-tj-cid="idnull">企业服务
                            <i class="delete"></i>
                    </a>
                                                                                                            <a rel="nofollow" href="javascript:;" data-lg-tj-id="8u00" data-lg-tj-no="
                                                                    0006
                                                            " data-lg-tj-cid="idnull">教育
                            <i class="delete"></i>
                    </a>
                                                                                                            <a rel="nofollow" href="javascript:;" data-lg-tj-id="8u00" data-lg-tj-no="
                                                                    0007
                                                            " data-lg-tj-cid="idnull">文化娱乐
                            <i class="delete"></i>
                    </a>
                                                                                                            <a rel="nofollow" href="javascript:;" data-lg-tj-id="8u00" data-lg-tj-no="
                                                                    0008
                                                            " data-lg-tj-cid="idnull">游戏
                            <i class="delete"></i>
                    </a>
                                                                                                            <a rel="nofollow" href="javascript:;" data-lg-tj-id="8u00" data-lg-tj-no="
                                                                    0009
                                                            " data-lg-tj-cid="idnull">O2O
                            <i class="delete"></i>
                    </a>
                                                                                                            <a rel="nofollow" href="javascript:;" data-lg-tj-id="8u00" data-lg-tj-no="
                                                                    0010
                                                            " data-lg-tj-cid="idnull">硬件
                            <i class="delete"></i>
                    </a>
                                                                    <span class="btn-more-hy" href="javascript:;">更多 <i></i></span>
            </li>
            <div class="more-hy more-fields">
                <li class="hot multi-chosen">
                    <span class="title">行业领域：</span>
                                                            <a rel="nofollow" href="javascript:;" class="active" data-lg-tj-id="8u00" data-lg-tj-no="
                                                                    0001
                                                            " data-lg-tj-cid="idnull">不限
                    </a>
                                                                                                            <a rel="nofollow" href="javascript:;" data-lg-tj-id="8v00" data-lg-tj-no="
                                                                    0002
                                                            " data-lg-tj-cid="idnull">移动互联网
                            <i class="delete"></i>
                        </a>
                                                                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8v00" data-lg-tj-no="
                                                                    0003
                                                            " data-lg-tj-cid="idnull">电子商务
                            <i class="delete"></i>
                        </a>
                                                                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8v00" data-lg-tj-no="
                                                                    0004
                                                            " data-lg-tj-cid="idnull">金融
                            <i class="delete"></i>
                        </a>
                                                                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8v00" data-lg-tj-no="
                                                                    0005
                                                            " data-lg-tj-cid="idnull">企业服务
                            <i class="delete"></i>
                        </a>
                                                                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8v00" data-lg-tj-no="
                                                                    0006
                                                            " data-lg-tj-cid="idnull">教育
                            <i class="delete"></i>
                        </a>
                                                                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8v00" data-lg-tj-no="
                                                                    0007
                                                            " data-lg-tj-cid="idnull">文化娱乐
                            <i class="delete"></i>
                        </a>
                                                                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8v00" data-lg-tj-no="
                                                                    0008
                                                            " data-lg-tj-cid="idnull">游戏
                            <i class="delete"></i>
                        </a>
                                                                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8v00" data-lg-tj-no="
                                                                    0009
                                                            " data-lg-tj-cid="idnull">O2O
                            <i class="delete"></i>
                        </a>
                                                                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8v00" data-lg-tj-no="
                                                                    0010
                                                            " data-lg-tj-cid="idnull">硬件
                            <i class="delete"></i>
                        </a>
                                                                                </li>
                <li class="other multi-chosen other-hy">
                                                                                        <a rel="nofollow" href="javascript:;" data-lg-tj-id="8w00" data-lg-tj-no="
                                                                    0001
                                                            " data-lg-tj-cid="idnull">社交网络
                            <i class="delete"></i>
                        </a>
                                                                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8w00" data-lg-tj-no="
                                                                    0002
                                                            " data-lg-tj-cid="idnull">旅游
                            <i class="delete"></i>
                        </a>
                                                                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8w00" data-lg-tj-no="
                                                                    0003
                                                            " data-lg-tj-cid="idnull">医疗健康
                            <i class="delete"></i>
                        </a>
                                                                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8w00" data-lg-tj-no="
                                                                    0004
                                                            " data-lg-tj-cid="idnull">生活服务
                            <i class="delete"></i>
                        </a>
                                                                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8w00" data-lg-tj-no="
                                                                    0005
                                                            " data-lg-tj-cid="idnull">信息安全
                            <i class="delete"></i>
                        </a>
                                                                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8w00" data-lg-tj-no="
                                                                    0006
                                                            " data-lg-tj-cid="idnull">数据服务
                            <i class="delete"></i>
                        </a>
                                                                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8w00" data-lg-tj-no="
                                                                    0007
                                                            " data-lg-tj-cid="idnull">广告营销
                            <i class="delete"></i>
                        </a>
                                                                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8w00" data-lg-tj-no="
                                                                    0008
                                                            " data-lg-tj-cid="idnull">分类信息
                            <i class="delete"></i>
                        </a>
                                                                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8w00" data-lg-tj-no="
                                                                    0009
                                                            " data-lg-tj-cid="idnull">招聘
                            <i class="delete"></i>
                        </a>
                                                                                                                                    <a rel="nofollow" href="javascript:;" data-lg-tj-id="8w00" data-lg-tj-no="
                                                                    0010
                                                            " data-lg-tj-cid="idnull">其他
                            <i class="delete"></i>
                        </a>
                                                                                </li>
            </div>
        </div>
    </div>
</ul>
<div class="btn-collapse-wrapper">
    <a rel="nofollow" class="btn-collapse " title="点击收起筛选项" href="javascript:"></a>
</div>




                    <!-- 排序 -->

                    <ul class="order" id="order">
    <li class="wrapper">
        <div class="item order">
            <span class="title">排序方式：</span>
                                    <a rel="nofollow" href="javascript:;" class="active" data-lg-tj-id="8x00" data-lg-tj-no="
                                                            0001
                                                    " data-lg-tj-cid="idnull">默认</a>
                                                <a rel="nofollow" href="https://www.lagou.com/jobs/list_Java?px=new&amp;city=全国#order" data-lg-tj-id="8x00" data-lg-tj-no="
                                                            0002
                                                    " data-lg-tj-cid="idnull">最新</a>
                                </div>
        <div class="item salary selectUI">
            <span class="title">月薪：</span>
                                                                                                                                                                                                                                                                                    <div class="selectUI-text text"><span>不限</span><i></i>
                            <ul>
                                        <li><a rel="nofollow" href="https://www.lagou.com/jobs/list_Java?px=default&amp;city=全国#order" data-lg-tj-id="8y00" data-lg-tj-no="
                                                            0001
                                                    " data-lg-tj-cid="idnull">不限</a></li>
                                        <li><a rel="nofollow" href="https://www.lagou.com/jobs/list_Java?px=default&amp;yx=2k以下&amp;city=全国#order" data-lg-tj-id="8y00" data-lg-tj-no="
                                                            0002
                                                    " data-lg-tj-cid="idnull">2k以下</a></li>
                                        <li><a rel="nofollow" href="https://www.lagou.com/jobs/list_Java?px=default&amp;yx=2k-5k&amp;city=全国#order" data-lg-tj-id="8y00" data-lg-tj-no="
                                                            0003
                                                    " data-lg-tj-cid="idnull">2k-5k</a></li>
                                        <li><a rel="nofollow" href="https://www.lagou.com/jobs/list_Java?px=default&amp;yx=5k-10k&amp;city=全国#order" data-lg-tj-id="8y00" data-lg-tj-no="
                                                            0004
                                                    " data-lg-tj-cid="idnull">5k-10k</a></li>
                                        <li><a rel="nofollow" href="https://www.lagou.com/jobs/list_Java?px=default&amp;yx=10k-15k&amp;city=全国#order" data-lg-tj-id="8y00" data-lg-tj-no="
                                                            0005
                                                    " data-lg-tj-cid="idnull">10k-15k</a></li>
                                        <li><a rel="nofollow" href="https://www.lagou.com/jobs/list_Java?px=default&amp;yx=15k-25k&amp;city=全国#order" data-lg-tj-id="8y00" data-lg-tj-no="
                                                            0006
                                                    " data-lg-tj-cid="idnull">15k-25k</a></li>
                                        <li><a rel="nofollow" href="https://www.lagou.com/jobs/list_Java?px=default&amp;yx=25k-50k&amp;city=全国#order" data-lg-tj-id="8y00" data-lg-tj-no="
                                                            0007
                                                    " data-lg-tj-cid="idnull">25k-50k</a></li>
                                        <li><a rel="nofollow" href="https://www.lagou.com/jobs/list_Java?px=default&amp;yx=50k以上&amp;city=全国#order" data-lg-tj-id="8y00" data-lg-tj-no="
                                                            0008
                                                    " data-lg-tj-cid="idnull">50k以上</a></li>
                                    </ul>
            </div>
        </div>
                <div class="item type selectUI">
            <span class="title">工作性质：</span>
                                                                                                                                                                    <div class="selectUI-text value text"><span>不限</span><i></i>
                            <ul>
                                        <li><a rel="nofollow" href="https://www.lagou.com/jobs/list_Java?px=default&amp;city=全国#order" data-lg-tj-id="8z00" data-lg-tj-no="
                                                            0001
                                                    " data-lg-tj-cid="idnull">不限</a></li>
                                        <li><a rel="nofollow" href="https://www.lagou.com/jobs/list_Java?px=default&amp;gx=全职&amp;city=全国#order" data-lg-tj-id="8z00" data-lg-tj-no="
                                                            0002
                                                    " data-lg-tj-cid="idnull">全职</a></li>
                                        <li><a rel="nofollow" href="https://www.lagou.com/jobs/list_Java?px=default&amp;gx=兼职&amp;city=全国#order" data-lg-tj-id="8z00" data-lg-tj-no="
                                                            0003
                                                    " data-lg-tj-cid="idnull">兼职</a></li>
                                        <li><a rel="nofollow" href="https://www.lagou.com/jobs/list_Java?px=default&amp;gx=实习&amp;city=全国&amp;isSchoolJob=1#order" data-lg-tj-id="8z00" data-lg-tj-no="
                                                            0004
                                                    " data-lg-tj-cid="idnull">实习</a></li>
                                    </ul>
            </div>
        </div>
                <div class="item page">
                                                <a class="prev_disabled prev ban" rel="nofollow" href="javascript:;">
                    &lt;
                    </a>
                                                                            <a class="next " href="https://www.lagou.com/zhaopin/Java/2/">
                    &gt;
                </a>
                                        <div class="page-number">
                <span class="curNum">1</span>
                /
                <span class="span totalNum">30</span>
            </div>
        </div>
    </li>
</ul>


                    <!--活动位-->

                </div>

                

                <!-- 公司列表 -->

                <div class="company_list dn" id="company_list">

	<ul class="item_con_list"><div class="empty_position">
        <div class="pic"></div>
        <div class="txt">
            <div>暂时没有符合该搜索条件的公司</div>
            <span>请重新修改搜索条件后再进行搜索</span>
        </div>
    </div></ul>

	<!-- 推荐公司、城市 -->
    <!-- <div class="recommend-comp-city dn">
    <div class="r_search_tit">相关搜索：</div>
    <ul class="r_search_con">

    </ul>
</div> -->


<div class="recommend-comp-city hide-recom dn" style="display: block;">
	<a rel="nofollow" href="javascript:;" class="expansion">展开<i></i></a>
    <div class="r_company_tit">推荐公司：</div>
    <ul class="r_company_con">
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/9251.html">美柚</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/1373.html">喜马拉雅fm</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/14229.html">微盟</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/49369.html">淘粉吧</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/107435.html">熊猫TV</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/2768.html">易到用车</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/40738.html">小红唇</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/97631.html">汽车超人</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/109.html">蚂蜂窝</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/36996.html">三好网</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/4760.html">唯品会</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/1686.html">爱奇艺</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/23014.html">快法务</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/1575.html">百度招聘</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/81491.html">蚂蚁金服</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/62.html">今日头条</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/2474.html">滴滴</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/20909.html">AcFun</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/23489.html">点点客</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/59251.html">映客</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/3712.html">京东</a></li>
    	    </ul>
    <div class="r_city_tit">推荐城市：</div>
    <ul class="r_city_con">
    	    		<li class="r_search_item"><a href="https://www.lagou.com/beijing/">北京找工作</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/beijing/">北京招聘</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/shanghai/">上海找工作</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/shanghai/">上海招聘</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/hangzhou/">杭州找工作</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/hangzhou/">杭州招聘</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/guangzhou/">广州找工作</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/guangzhou/">广州招聘</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/shenzhen/">深圳找工作</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/shenzhen/">深圳招聘</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/chengdu/">成都找工作</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/chengdu/">成都招聘</a></li>
    	    </ul>
</div>

	<!-- 分页 -->
	<div class="item_con_pager"></div>
    <input type="hidden" name="abtCode" value="dm-csearch-useUserAllInterest|0">
</div>

<script id="tpl-comp-list" type="text/html">
	{{each data as item i}}
	<li class="c_list_item" data-index="{{i + indexOffset}}" data-companyid="{{item.companyId}}">

		<div class="cl_left">
			<a href="https://www.lagou.com/gongsi/{{item.companyId}}.html" target="_blank" data-lg-tj-id="8B00" data-lg-tj-no="
             	{{if i<9}}
             		{{if item.curpage<10}}
                	0{{item.curpage}}0{{i+1}}
                	{{else}}
                	{{item.curpage}}0{{i+1}}
                	{{/if}}
                {{else}}
                	{{if item.curpage<10}}
                    0{{item.curpage}}{{i+1}}
                    {{else}}
                    {{item.curpage}}{{i+1}}
                    {{/if}}
               {{/if}}
                " data-lg-tj-cid="{{item.companyId}}" {{if extra.abt}}data-lg-tj-abt="{{extra.abt}}"{{/if}}><img src="//www.lgstatic.com/thumbnail_160x160/{{item.companyLogo}}" alt="{{item.companyFullName}}" width="80" height="80"></a>
		</div>

		<div class="cl_r">

			<div class="cl_r_top">
				<h3><a class="company_link" href="https://www.lagou.com/gongsi/{{item.companyId}}.html" target="_blank" data-lg-tj-id="8C00" data-lg-tj-no="
             	{{if i<9}}
             		{{if item.curpage<10}}
                	0{{item.curpage}}0{{i+1}}
                	{{else}}
                	{{item.curpage}}0{{i+1}}
                	{{/if}}
                {{else}}
                	{{if item.curpage<10}}
                    0{{item.curpage}}{{i+1}}
                    {{else}}
                    {{item.curpage}}{{i+1}}
                    {{/if}}
               {{/if}}
                " data-lg-tj-cid="{{item.companyId}}" {{if extra.abt}}data-lg-tj-abt="{{extra.abt}}"{{/if}}>{{item.companyShortName}}</a></h3>
				<div>“{{item.companyFeatures}}”</div>
			</div>

			<div class="cl_r_bot">
				<ul class="list_c">
					<li class="address"><span></span>{{item.city}}{{if item.district}},{{item.district}}{{/if}}</li>
					<li class="indu"><span></span>{{item.industryField}}</li>
					<li class="posi"><a href="https://www.lagou.com/gongsi/j{{item.companyId}}.html" target="_blank" data-lg-tj-id="8H00" data-lg-tj-no="
                {{if i<9}}
                    {{if item.curpage<10}}
                    0{{item.curpage}}0{{i+1}}
                    {{else}}
                    {{item.curpage}}0{{i+1}}
                    {{/if}}
                {{else}}
                    {{if item.curpage<10}}
                    0{{item.curpage}}{{i+1}}
                    {{else}}
                    {{item.curpage}}{{i+1}}
                    {{/if}}
               {{/if}}
                " data-lg-tj-cid="{{item.companyId}}" {{if extra.abt}}data-lg-tj-abt="{{extra.abt}}"{{/if}}><span></span>{{item.positionNum}}个在招职位</a></li>
					<li class="inter"><a href="https://www.lagou.com/gongsi/interviewExperiences.html?companyId={{item.companyId}}" target="_blank" data-lg-tj-id="8I00" data-lg-tj-no="
                {{if i<9}}
                    {{if item.curpage<10}}
                    0{{item.curpage}}0{{i+1}}
                    {{else}}
                    {{item.curpage}}0{{i+1}}
                    {{/if}}
                {{else}}
                    {{if item.curpage<10}}
                    0{{item.curpage}}{{i+1}}
                    {{else}}
                    {{item.curpage}}{{i+1}}
                    {{/if}}
               {{/if}}
                " data-lg-tj-cid="{{item.companyId}}" {{if extra.abt}}data-lg-tj-abt="{{extra.abt}}"{{/if}}><span></span>{{item.interviewRemarkNum}}个面试评价</a></li>
					<li class="c_btn"><a href="https://www.lagou.com/gongsi/{{item.companyId}}.html" target="_blank" data-lg-tj-id="8D00" data-lg-tj-no="
             	{{if i<9}}
             		{{if item.curpage<9}}
                	0{{item.curpage}}0{{i+1}}
                	{{else}}
                	{{item.curpage}}0{{i+1}}
                	{{/if}}
                {{else}}
                	{{if item.curpage<10}}
                    0{{item.curpage}}{{i+1}}
                    {{else}}
                    {{item.curpage}}{{i+1}}
                    {{/if}}
               {{/if}}
                " data-lg-tj-cid="{{item.companyId}}" {{if extra.abt}}data-lg-tj-abt="{{extra.abt}}"{{/if}}>公司主页&nbsp;<i></i></a></li>
				</ul>
			</div>
		</div>

	</li>
	{{/each}}
</script>

<script id="empty-comp" type="text/html">
    <div class="empty_position">
        <div class="pic"></div>
        <div class="txt">
            <div>暂时没有符合该搜索条件的公司</div>
            <span>请重新修改搜索条件后再进行搜索</span>
        </div>
    </div>
</script>


                <!-- 职位列表 -->

                <div class="s_position_list " id="s_position_list">
        
    <!-- 切换分站 -->
        
    
                        <ul class="item_con_list">
                                                        <li class="con_list_item default_list" data-index="0" data-positionid="2106073" data-salary="23k-35k" data-company="蚂蚁金服集团" data-positionname="Java" data-companyid="153849" data-hrid="5667387" data-adword="0">
                                         <div class="list_item_top">
                        <div class="position">
                            <div class="p_top">

                                <a class="position_link" href="https://www.lagou.com/jobs/2106073.html" target="_blank" data-index="0" data-lg-tj-id="8E00" data-lg-tj-no="
                                                                                                0101
                                                                                        " data-lg-tj-cid="2106073" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">
                                    <h3 style="max-width: 180px;">Java</h3>
                                                                                                                                                                        <span class="add">[<em>上海·陆家嘴</em>]</span>
                                                                                                                                                        </a>
                                <span class="format-time">15:35发布</span>
                            </div>
                            <div class="p_bot">
                                <div class="li_b_l">
                                    <span class="money">23k-35k</span>
                                    <!--<i></i>-->经验不限 / 不限
                                </div>
                            </div>
                        </div>
                        <div class="company">
                            <div class="company_name">
                                <a href="https://www.lagou.com/gongsi/153849.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="
                                                                                                0101
                                                                                        " data-lg-tj-cid="153849" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">蚂蚁金服集团</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                            </div>
                            <div class="industry">
                                金融,移动互联网 / B轮
                            </div>
                        </div>
                        <div class="com_logo">
                            <a href="https://www.lagou.com/gongsi/153849.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="
                                                                                                0101
                                                                                        " data-lg-tj-cid="153849" data-lg-tj-abt="dm-csearch-useUserAllInterest|0"><img src="//www.lgstatic.com/thumbnail_120x120/i/image/M00/1F/54/CgpFT1kRuMmASL74AAAg3WZnNI005.jpeg" alt="蚂蚁金服集团" width="60" height="60"></a>
                        </div>
                    </div>
                    <div class="list_item_bot">
                        <div class="li_b_l">
                                                                                                <span>支付</span>
                                                                    <span>银行</span>
                                                                    <span>电商</span>
                                                                    <span>架构</span>
                                                                    <span>期权高潜力</span>
                                                                                    </div>
                        <div class="li_b_r">“期权、好福利、绩效奖金、十三薪、国际化”</div>
                    </div>
                </li>
                                                            <li class="con_list_item default_list" data-index="1" data-positionid="4383913" data-salary="20k-25k" data-company="人人行(借贷宝)" data-positionname="Java工程师" data-companyid="61921" data-hrid="7134052" data-adword="0">
                                         <div class="list_item_top">
                        <div class="position">
                            <div class="p_top">

                                <a class="position_link" href="https://www.lagou.com/jobs/4383913.html" target="_blank" data-index="1" data-lg-tj-id="8E00" data-lg-tj-no="
                                                                                                0102
                                                                                        " data-lg-tj-cid="4383913" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">
                                    <h3 style="max-width: 180px;">Java工程师</h3>
                                                                                                                                                                                                                            <span class="add">[<em>北京·朝阳区</em>]</span>
                                                                                                                                                                                                        </a>
                                <span class="format-time">2天前发布</span>
                            </div>
                            <div class="p_bot">
                                <div class="li_b_l">
                                    <span class="money">20k-25k</span>
                                    <!--<i></i>-->经验3-5年 / 不限
                                </div>
                            </div>
                        </div>
                        <div class="company">
                            <div class="company_name">
                                <a href="https://www.lagou.com/gongsi/61921.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="
                                                                                                0102
                                                                                        " data-lg-tj-cid="61921" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">人人行(借贷宝)</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                            </div>
                            <div class="industry">
                                移动互联网,金融 / C轮
                            </div>
                        </div>
                        <div class="com_logo">
                            <a href="https://www.lagou.com/gongsi/61921.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="
                                                                                                0102
                                                                                        " data-lg-tj-cid="61921" data-lg-tj-abt="dm-csearch-useUserAllInterest|0"><img src="//www.lgstatic.com/thumbnail_120x120/i/image/M00/04/01/CgqKkVbFXXqAPo0fAAATqvTo2-I592.png" alt="人人行(借贷宝)" width="60" height="60"></a>
                        </div>
                    </div>
                    <div class="list_item_bot">
                        <div class="li_b_l">
                                                                                                                                        <span>年底双薪</span>
                                                                                                                                                <span>节日礼物</span>
                                                                                                                                                <span>绩效奖金</span>
                                                                                                                                                <span>岗位晋升</span>
                                                                                                                        </div>
                        <div class="li_b_r">“弹性工作,高并发系统,团队大牛多,工作氛”</div>
                    </div>
                </li>
                                                            <li class="con_list_item default_list" data-index="2" data-positionid="4477797" data-salary="15k-25k" data-company="拉勾网" data-positionname="java开发工程师" data-companyid="147" data-hrid="2848224" data-adword="0">
                                         <div class="list_item_top">
                        <div class="position">
                            <div class="p_top">

                                <a class="position_link" href="https://www.lagou.com/jobs/4477797.html" target="_blank" data-index="2" data-lg-tj-id="8E00" data-lg-tj-no="
                                                                                                0103
                                                                                        " data-lg-tj-cid="4477797" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">
                                    <h3 style="max-width: 180px;">java开发工程师</h3>
                                                                                                                                                                                                                            <span class="add">[<em>北京·海淀区</em>]</span>
                                                                                                                                                                                                        </a>
                                <span class="format-time">3天前发布</span>
                            </div>
                            <div class="p_bot">
                                <div class="li_b_l">
                                    <span class="money">15k-25k</span>
                                    <!--<i></i>-->经验3-5年 / 本科
                                </div>
                            </div>
                        </div>
                        <div class="company">
                            <div class="company_name">
                                <a href="https://www.lagou.com/gongsi/147.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="
                                                                                                0103
                                                                                        " data-lg-tj-cid="147" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">拉勾网</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                            </div>
                            <div class="industry">
                                企业服务,招聘 / D轮及以上
                            </div>
                        </div>
                        <div class="com_logo">
                            <a href="https://www.lagou.com/gongsi/147.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="
                                                                                                0103
                                                                                        " data-lg-tj-cid="147" data-lg-tj-abt="dm-csearch-useUserAllInterest|0"><img src="//www.lgstatic.com/thumbnail_120x120/i/image/M00/76/40/Cgp3O1g1TNOAB2yxAAA9bQUyc4g814.png" alt="拉勾网" width="60" height="60"></a>
                        </div>
                    </div>
                    <div class="list_item_bot">
                        <div class="li_b_l">
                                                                                                <span>分布式</span>
                                                                    <span>架构</span>
                                                                                    </div>
                        <div class="li_b_r">“技术挑战,成长空间”</div>
                    </div>
                </li>
                                                            <li class="con_list_item default_list" data-index="3" data-positionid="3155873" data-salary="4k-8k" data-company="小肚皮App" data-positionname="实习JAVA/PHP开发" data-companyid="41030" data-hrid="795835" data-adword="0">
                                         <div class="list_item_top">
                        <div class="position">
                            <div class="p_top">

                                <a class="position_link" href="https://www.lagou.com/jobs/3155873.html" target="_blank" data-index="3" data-lg-tj-id="8E00" data-lg-tj-no="
                                                                                                0104
                                                                                        " data-lg-tj-cid="3155873" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">
                                    <h3 style="max-width: 180px;">实习JAVA/PHP开发</h3>
                                                                                                                                                                        <span class="add">[<em>北京·大望路</em>]</span>
                                                                                                                                                        </a>
                                <span class="format-time">10:13发布</span>
                            </div>
                            <div class="p_bot">
                                <div class="li_b_l">
                                    <span class="money">4k-8k</span>
                                    <!--<i></i>-->经验应届毕业生 / 本科
                                </div>
                            </div>
                        </div>
                        <div class="company">
                            <div class="company_name">
                                <a href="https://www.lagou.com/gongsi/41030.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="
                                                                                                0104
                                                                                        " data-lg-tj-cid="41030" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">小肚皮App</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                            </div>
                            <div class="industry">
                                移动互联网 / A轮
                            </div>
                        </div>
                        <div class="com_logo">
                            <a href="https://www.lagou.com/gongsi/41030.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="
                                                                                                0104
                                                                                        " data-lg-tj-cid="41030" data-lg-tj-abt="dm-csearch-useUserAllInterest|0"><img src="//www.lgstatic.com/thumbnail_120x120/i/image/M00/65/83/CgpFT1mlFSWAJrrnAACWcSWNiu8425.png" alt="小肚皮App" width="60" height="60"></a>
                        </div>
                    </div>
                    <div class="list_item_bot">
                        <div class="li_b_l">
                                                                                                <span>游戏</span>
                                                                    <span>后端开发</span>
                                                                                    </div>
                        <div class="li_b_r">“转正机会,逗逼氛围,美女如云,餐补”</div>
                    </div>
                </li>
                                                            <li class="con_list_item default_list" data-index="4" data-positionid="4524750" data-salary="10k-20k" data-company="清鹤科技" data-positionname="Java开发工程师" data-companyid="205106" data-hrid="2258995" data-adword="0">
                                         <div class="list_item_top">
                        <div class="position">
                            <div class="p_top">

                                <a class="position_link" href="https://www.lagou.com/jobs/4524750.html" target="_blank" data-index="4" data-lg-tj-id="8E00" data-lg-tj-no="
                                                                                                0105
                                                                                        " data-lg-tj-cid="4524750" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">
                                    <h3 style="max-width: 180px;">Java开发工程师</h3>
                                                                                                                                                                                                                            <span class="add">[<em>上海·浦东新…</em>]</span>
                                                                                                                                                                                                        </a>
                                <span class="format-time">11:14发布</span>
                            </div>
                            <div class="p_bot">
                                <div class="li_b_l">
                                    <span class="money">10k-20k</span>
                                    <!--<i></i>-->经验1-3年 / 本科
                                </div>
                            </div>
                        </div>
                        <div class="company">
                            <div class="company_name">
                                <a href="https://www.lagou.com/gongsi/205106.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="
                                                                                                0105
                                                                                        " data-lg-tj-cid="205106" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">清鹤科技</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                            </div>
                            <div class="industry">
                                移动互联网 / 上市公司
                            </div>
                        </div>
                        <div class="com_logo">
                            <a href="https://www.lagou.com/gongsi/205106.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="
                                                                                                0105
                                                                                        " data-lg-tj-cid="205106" data-lg-tj-abt="dm-csearch-useUserAllInterest|0"><img src="//www.lgstatic.com/thumbnail_120x120/i/image/M00/28/55/CgpEMlkdLC6ALO_rAAAPAl8EZSg594.jpg" alt="清鹤科技" width="60" height="60"></a>
                        </div>
                    </div>
                    <div class="list_item_bot">
                        <div class="li_b_l">
                                                                                                <span>C/C++</span>
                                                                    <span>Python</span>
                                                                                    </div>
                        <div class="li_b_r">“公司多牛人,准IPO,年终奖金,自身发展好”</div>
                    </div>
                </li>
                                                            <li class="con_list_item default_list" data-index="5" data-positionid="4524693" data-salary="10K-15K" data-company="云沃客" data-positionname="Java开发工程师" data-companyid="15507" data-hrid="8172155" data-adword="0">
                                         <div class="list_item_top">
                        <div class="position">
                            <div class="p_top">

                                <a class="position_link" href="https://www.lagou.com/jobs/4524693.html" target="_blank" data-index="5" data-lg-tj-id="8E00" data-lg-tj-no="
                                                                                                0106
                                                                                        " data-lg-tj-cid="4524693" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">
                                    <h3 style="max-width: 180px;">Java开发工程师</h3>
                                                                                                                                                                                                                            <span class="add">[<em>上海·青浦区</em>]</span>
                                                                                                                                                                                                        </a>
                                <span class="format-time">10:26发布</span>
                            </div>
                            <div class="p_bot">
                                <div class="li_b_l">
                                    <span class="money">10K-15K</span>
                                    <!--<i></i>-->经验3-5年 / 大专
                                </div>
                            </div>
                        </div>
                        <div class="company">
                            <div class="company_name">
                                <a href="https://www.lagou.com/gongsi/15507.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="
                                                                                                0106
                                                                                        " data-lg-tj-cid="15507" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">云沃客</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                            </div>
                            <div class="industry">
                                移动互联网 / A轮
                            </div>
                        </div>
                        <div class="com_logo">
                            <a href="https://www.lagou.com/gongsi/15507.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="
                                                                                                0106
                                                                                        " data-lg-tj-cid="15507" data-lg-tj-abt="dm-csearch-useUserAllInterest|0"><img src="//www.lgstatic.com/thumbnail_120x120/i/image/M00/95/CC/CgqKkVib5lOAQfDkAARON1JPM1o797.png" alt="云沃客" width="60" height="60"></a>
                        </div>
                    </div>
                    <div class="list_item_bot">
                        <div class="li_b_l">
                                                                                                                                        <span>数字化开发</span>
                                                                                                                                                <span>软件众包事业</span>
                                                                                                                                                <span>结果付酬</span>
                                                                                                                                                <span>实践远程办公</span>
                                                                                                                        </div>
                        <div class="li_b_r">“五险一金”</div>
                    </div>
                </li>
                                                            <li class="con_list_item default_list" data-index="6" data-positionid="4524434" data-salary="9k-18k" data-company="青鹿教育" data-positionname="JAVA开发" data-companyid="277688" data-hrid="9201601" data-adword="0">
                                         <div class="list_item_top">
                        <div class="position">
                            <div class="p_top">

                                <a class="position_link" href="https://www.lagou.com/jobs/4524434.html" target="_blank" data-index="6" data-lg-tj-id="8E00" data-lg-tj-no="
                                                                                                0107
                                                                                        " data-lg-tj-cid="4524434" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">
                                    <h3 style="max-width: 180px;">JAVA开发</h3>
                                                                                                                                                                                                                            <span class="add">[<em>广州·天河区</em>]</span>
                                                                                                                                                                                                        </a>
                                <span class="format-time">1天前发布</span>
                            </div>
                            <div class="p_bot">
                                <div class="li_b_l">
                                    <span class="money">9k-18k</span>
                                    <!--<i></i>-->经验不限 / 本科
                                </div>
                            </div>
                        </div>
                        <div class="company">
                            <div class="company_name">
                                <a href="https://www.lagou.com/gongsi/277688.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="
                                                                                                0107
                                                                                        " data-lg-tj-cid="277688" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">青鹿教育</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                            </div>
                            <div class="industry">
                                教育,移动互联网 / 不需要融资
                            </div>
                        </div>
                        <div class="com_logo">
                            <a href="https://www.lagou.com/gongsi/277688.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="
                                                                                                0107
                                                                                        " data-lg-tj-cid="277688" data-lg-tj-abt="dm-csearch-useUserAllInterest|0"><img src="//www.lgstatic.com/thumbnail_120x120/i/image2/M00/14/E1/CgoB5lnylDOABMzqAAAJV7MGWX8491.jpg" alt="青鹿教育" width="60" height="60"></a>
                        </div>
                    </div>
                    <div class="list_item_bot">
                        <div class="li_b_l">
                                                                                                <span>web</span>
                                                                    <span>平台/后台</span>
                                                                    <span>J2EE</span>
                                                                    <span>SSH</span>
                                                                    <span>SSM</span>
                                                                                    </div>
                        <div class="li_b_r">“周末双休,带薪年假,团队活动,节日福利”</div>
                    </div>
                </li>
                                                            <li class="con_list_item default_list" data-index="7" data-positionid="3320102" data-salary="15k-30k" data-company="zilliz" data-positionname="Java开发工程师" data-companyid="225377" data-hrid="8396897" data-adword="0">
                                         <div class="list_item_top">
                        <div class="position">
                            <div class="p_top">

                                <a class="position_link" href="https://www.lagou.com/jobs/3320102.html" target="_blank" data-index="7" data-lg-tj-id="8E00" data-lg-tj-no="
                                                                                                0108
                                                                                        " data-lg-tj-cid="3320102" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">
                                    <h3 style="max-width: 180px;">Java开发工程师</h3>
                                                                                                                                                                        <span class="add">[<em>上海·徐家汇</em>]</span>
                                                                                                                                                        </a>
                                <span class="format-time">3天前发布</span>
                            </div>
                            <div class="p_bot">
                                <div class="li_b_l">
                                    <span class="money">15k-30k</span>
                                    <!--<i></i>-->经验3-5年 / 本科
                                </div>
                            </div>
                        </div>
                        <div class="company">
                            <div class="company_name">
                                <a href="https://www.lagou.com/gongsi/225377.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="
                                                                                                0108
                                                                                        " data-lg-tj-cid="225377" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">zilliz</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                            </div>
                            <div class="industry">
                                企业服务,数据服务 / A轮
                            </div>
                        </div>
                        <div class="com_logo">
                            <a href="https://www.lagou.com/gongsi/225377.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="
                                                                                                0108
                                                                                        " data-lg-tj-cid="225377" data-lg-tj-abt="dm-csearch-useUserAllInterest|0"><img src="//www.lgstatic.com/thumbnail_120x120/i/image2/M00/1C/A4/CgotOVoFtbyAGqlTAAA0wSOsjJc52.jpeg" alt="zilliz" width="60" height="60"></a>
                        </div>
                    </div>
                    <div class="list_item_bot">
                        <div class="li_b_l">
                                                                                                <span>软件开发</span>
                                                                    <span>大数据</span>
                                                                    <span>C++</span>
                                                                    <span>服务器端</span>
                                                                    <span>高性能</span>
                                                                                    </div>
                        <div class="li_b_r">“丰厚期权,行业高薪,前沿技术,精英团队”</div>
                    </div>
                </li>
                                                            <li class="con_list_item default_list" data-index="8" data-positionid="4524892" data-salary="12K-18K" data-company="博奥特科技" data-positionname="Java开发工程师" data-companyid="69152" data-hrid="4544192" data-adword="0">
                                         <div class="list_item_top">
                        <div class="position">
                            <div class="p_top">

                                <a class="position_link" href="https://www.lagou.com/jobs/4524892.html" target="_blank" data-index="8" data-lg-tj-id="8E00" data-lg-tj-no="
                                                                                                0109
                                                                                        " data-lg-tj-cid="4524892" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">
                                    <h3 style="max-width: 180px;">Java开发工程师</h3>
                                                                                                                                                                        <span class="add">[<em>深圳·益田村</em>]</span>
                                                                                                                                                        </a>
                                <span class="format-time">15:13发布</span>
                            </div>
                            <div class="p_bot">
                                <div class="li_b_l">
                                    <span class="money">12K-18K</span>
                                    <!--<i></i>-->经验3-5年 / 不限
                                </div>
                            </div>
                        </div>
                        <div class="company">
                            <div class="company_name">
                                <a href="https://www.lagou.com/gongsi/69152.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="
                                                                                                0109
                                                                                        " data-lg-tj-cid="69152" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">博奥特科技</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                            </div>
                            <div class="industry">
                                移动互联网,金融 / 未融资
                            </div>
                        </div>
                        <div class="com_logo">
                            <a href="https://www.lagou.com/gongsi/69152.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="
                                                                                                0109
                                                                                        " data-lg-tj-cid="69152" data-lg-tj-abt="dm-csearch-useUserAllInterest|0"><img src="//www.lgstatic.com/thumbnail_120x120/i/image3/M00/33/C4/Cgq2xlqmL1yAQ--9AAAqXWcpN_Y427.png" alt="博奥特科技" width="60" height="60"></a>
                        </div>
                    </div>
                    <div class="list_item_bot">
                        <div class="li_b_l">
                                                                                                <span>金融</span>
                                                                    <span>银行</span>
                                                                    <span>中级</span>
                                                                    <span>后端开发</span>
                                                                                    </div>
                        <div class="li_b_r">“金融IT行业”</div>
                    </div>
                </li>
                                                            <li class="con_list_item default_list" data-index="9" data-positionid="4261849" data-salary="15k-25k" data-company="金山云" data-positionname="Java开发工程师" data-companyid="956" data-hrid="5528" data-adword="0">
                                         <div class="list_item_top">
                        <div class="position">
                            <div class="p_top">

                                <a class="position_link" href="https://www.lagou.com/jobs/4261849.html" target="_blank" data-index="9" data-lg-tj-id="8E00" data-lg-tj-no="
                                                                                                0110
                                                                                        " data-lg-tj-cid="4261849" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">
                                    <h3 style="max-width: 180px;">Java开发工程师</h3>
                                                                                                                                                                        <span class="add">[<em>北京·西北旺</em>]</span>
                                                                                                                                                        </a>
                                <span class="format-time">3天前发布</span>
                            </div>
                            <div class="p_bot">
                                <div class="li_b_l">
                                    <span class="money">15k-25k</span>
                                    <!--<i></i>-->经验3-5年 / 本科
                                </div>
                            </div>
                        </div>
                        <div class="company">
                            <div class="company_name">
                                <a href="https://www.lagou.com/gongsi/956.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="
                                                                                                0110
                                                                                        " data-lg-tj-cid="956" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">金山云</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                            </div>
                            <div class="industry">
                                移动互联网,数据服务 / C轮
                            </div>
                        </div>
                        <div class="com_logo">
                            <a href="https://www.lagou.com/gongsi/956.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="
                                                                                                0110
                                                                                        " data-lg-tj-cid="956" data-lg-tj-abt="dm-csearch-useUserAllInterest|0"><img src="//www.lgstatic.com/thumbnail_120x120/image1/M00/00/04/Cgo8PFTUWACAWautAAAh6gMfsB0502.jpg" alt="金山云" width="60" height="60"></a>
                        </div>
                    </div>
                    <div class="list_item_bot">
                        <div class="li_b_l">
                                                                                                <span>高级</span>
                                                                    <span>中级</span>
                                                                    <span>MySQL</span>
                                                                    <span>架构</span>
                                                                                    </div>
                        <div class="li_b_r">“大厂,团队氛围好,三餐,成长快”</div>
                    </div>
                </li>
                                                            <li class="con_list_item default_list" data-index="10" data-positionid="3643587" data-salary="10k-15k" data-company="江苏亿科达" data-positionname="Java开发工程师" data-companyid="128998" data-hrid="8308770" data-adword="0">
                                         <div class="list_item_top">
                        <div class="position">
                            <div class="p_top">

                                <a class="position_link" href="https://www.lagou.com/jobs/3643587.html" target="_blank" data-index="10" data-lg-tj-id="8E00" data-lg-tj-no="
                                                                                                0111
                                                                                        " data-lg-tj-cid="3643587" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">
                                    <h3 style="max-width: 180px;">Java开发工程师</h3>
                                                                                                                                                                        <span class="add">[<em>上海·陆家嘴</em>]</span>
                                                                                                                                                        </a>
                                <span class="format-time">2天前发布</span>
                            </div>
                            <div class="p_bot">
                                <div class="li_b_l">
                                    <span class="money">10k-15k</span>
                                    <!--<i></i>-->经验3-5年 / 本科
                                </div>
                            </div>
                        </div>
                        <div class="company">
                            <div class="company_name">
                                <a href="https://www.lagou.com/gongsi/128998.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="
                                                                                                0111
                                                                                        " data-lg-tj-cid="128998" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">江苏亿科达</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                            </div>
                            <div class="industry">
                                移动互联网,金融 / 不需要融资
                            </div>
                        </div>
                        <div class="com_logo">
                            <a href="https://www.lagou.com/gongsi/128998.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="
                                                                                                0111
                                                                                        " data-lg-tj-cid="128998" data-lg-tj-abt="dm-csearch-useUserAllInterest|0"><img src="//www.lgstatic.com/thumbnail_120x120/i/image/M00/2A/A6/Cgp3O1cyziuAfM5AAAAe20ZOb-4754.png" alt="江苏亿科达" width="60" height="60"></a>
                        </div>
                    </div>
                    <div class="list_item_bot">
                        <div class="li_b_l">
                                                                                                <span>MySQL</span>
                                                                    <span>j2ee</span>
                                                                    <span>oracle</span>
                                                                    <span>架构</span>
                                                                    <span>SVN</span>
                                                                                    </div>
                        <div class="li_b_r">“五险一金,年终奖,体检旅游,过节费”</div>
                    </div>
                </li>
                                                            <li class="con_list_item default_list" data-index="11" data-positionid="4496287" data-salary="15k-25k" data-company="中民珠宝" data-positionname="JAVA工程师" data-companyid="374313" data-hrid="10688693" data-adword="0">
                                         <div class="list_item_top">
                        <div class="position">
                            <div class="p_top">

                                <a class="position_link" href="https://www.lagou.com/jobs/4496287.html" target="_blank" data-index="11" data-lg-tj-id="8E00" data-lg-tj-no="
                                                                                                0112
                                                                                        " data-lg-tj-cid="4496287" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">
                                    <h3 style="max-width: 180px;">JAVA工程师</h3>
                                                                                                                                                                        <span class="add">[<em>深圳·清水河</em>]</span>
                                                                                                                                                        </a>
                                <span class="format-time">07:58发布</span>
                            </div>
                            <div class="p_bot">
                                <div class="li_b_l">
                                    <span class="money">15k-25k</span>
                                    <!--<i></i>-->经验3-5年 / 本科
                                </div>
                            </div>
                        </div>
                        <div class="company">
                            <div class="company_name">
                                <a href="https://www.lagou.com/gongsi/374313.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="
                                                                                                0112
                                                                                        " data-lg-tj-cid="374313" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">中民珠宝</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                            </div>
                            <div class="industry">
                                移动互联网,其他 / 不需要融资
                            </div>
                        </div>
                        <div class="com_logo">
                            <a href="https://www.lagou.com/gongsi/374313.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="
                                                                                                0112
                                                                                        " data-lg-tj-cid="374313" data-lg-tj-abt="dm-csearch-useUserAllInterest|0"><img src="//www.lgstatic.com/thumbnail_120x120/i/image3/M00/4D/7C/Cgq2xlrlfu-AdjYhAAAXWPNSAJc229.png" alt="中民珠宝" width="60" height="60"></a>
                        </div>
                    </div>
                    <div class="list_item_bot">
                        <div class="li_b_l">
                                                                                                <span>金融</span>
                                                                    <span>资深</span>
                                                                    <span>大数据</span>
                                                                    <span>系统架构</span>
                                                                                    </div>
                        <div class="li_b_r">“五险一金,年底双薪,绩效奖金,餐补”</div>
                    </div>
                </li>
                                                            <li class="con_list_item default_list" data-index="12" data-positionid="2738872" data-salary="20k-35k" data-company="腾展叮咚（Dingtone）" data-positionname="Java开发工程师" data-companyid="24287" data-hrid="2946659" data-adword="0">
                                         <div class="list_item_top">
                        <div class="position">
                            <div class="p_top">

                                <a class="position_link" href="https://www.lagou.com/jobs/2738872.html" target="_blank" data-index="12" data-lg-tj-id="8E00" data-lg-tj-no="
                                                                                                0113
                                                                                        " data-lg-tj-cid="2738872" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">
                                    <h3 style="max-width: 180px;">Java开发工程师</h3>
                                                                                                                                                                        <span class="add">[<em>杭州·文三路</em>]</span>
                                                                                                                                                        </a>
                                <span class="format-time">11:31发布</span>
                            </div>
                            <div class="p_bot">
                                <div class="li_b_l">
                                    <span class="money">20k-35k</span>
                                    <!--<i></i>-->经验3-5年 / 本科
                                </div>
                            </div>
                        </div>
                        <div class="company">
                            <div class="company_name">
                                <a href="https://www.lagou.com/gongsi/24287.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="
                                                                                                0113
                                                                                        " data-lg-tj-cid="24287" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">腾展叮咚（Dingtone）</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                            </div>
                            <div class="industry">
                                移动互联网,社交网络 / 上市公司
                            </div>
                        </div>
                        <div class="com_logo">
                            <a href="https://www.lagou.com/gongsi/24287.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="
                                                                                                0113
                                                                                        " data-lg-tj-cid="24287" data-lg-tj-abt="dm-csearch-useUserAllInterest|0"><img src="//www.lgstatic.com/thumbnail_120x120/image1/M00/0B/7D/Cgo8PFTzIBOAEd2dAACMq9tQoMA797.png" alt="腾展叮咚（Dingtone）" width="60" height="60"></a>
                        </div>
                    </div>
                    <div class="list_item_bot">
                        <div class="li_b_l">
                                                                                                <span>平台/后台</span>
                                                                    <span>J2EE</span>
                                                                    <span>系统架构</span>
                                                                    <span>redis</span>
                                                                                    </div>
                        <div class="li_b_r">“全球化产品,海量用户,精英团队,股权激励”</div>
                    </div>
                </li>
                                                            <li class="con_list_item default_list" data-index="13" data-positionid="4353567" data-salary="12k-20k" data-company="金证股份" data-positionname="Java开发工程师" data-companyid="25317" data-hrid="5715150" data-adword="0">
                                         <div class="list_item_top">
                        <div class="position">
                            <div class="p_top">

                                <a class="position_link" href="https://www.lagou.com/jobs/4353567.html" target="_blank" data-index="13" data-lg-tj-id="8E00" data-lg-tj-no="
                                                                                                0114
                                                                                        " data-lg-tj-cid="4353567" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">
                                    <h3 style="max-width: 180px;">Java开发工程师</h3>
                                                                                                                                                                                                                            <span class="add">[<em>深圳·福田区</em>]</span>
                                                                                                                                                                                                        </a>
                                <span class="format-time">1天前发布</span>
                            </div>
                            <div class="p_bot">
                                <div class="li_b_l">
                                    <span class="money">12k-20k</span>
                                    <!--<i></i>-->经验3-5年 / 本科
                                </div>
                            </div>
                        </div>
                        <div class="company">
                            <div class="company_name">
                                <a href="https://www.lagou.com/gongsi/25317.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="
                                                                                                0114
                                                                                        " data-lg-tj-cid="25317" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">金证股份</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                            </div>
                            <div class="industry">
                                金融 / 上市公司
                            </div>
                        </div>
                        <div class="com_logo">
                            <a href="https://www.lagou.com/gongsi/25317.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="
                                                                                                0114
                                                                                        " data-lg-tj-cid="25317" data-lg-tj-abt="dm-csearch-useUserAllInterest|0"><img src="//www.lgstatic.com/thumbnail_120x120/image1/M00/00/34/Cgo8PFTUXJOAMEEpAAAroeFn454603.jpg" alt="金证股份" width="60" height="60"></a>
                        </div>
                    </div>
                    <div class="list_item_bot">
                        <div class="li_b_l">
                                                                                                <span>SVN</span>
                                                                                    </div>
                        <div class="li_b_r">“上市公司,大型项目,年度旅游,五险一金”</div>
                    </div>
                </li>
                                                            <li class="con_list_item default_list" data-index="14" data-positionid="4486580" data-salary="8k-15k" data-company="南京思酷通讯科技有限公司" data-positionname="Java开发工程师" data-companyid="75213" data-hrid="1854910" data-adword="0">
                                         <div class="list_item_top">
                        <div class="position">
                            <div class="p_top">

                                <a class="position_link" href="https://www.lagou.com/jobs/4486580.html" target="_blank" data-index="14" data-lg-tj-id="8E00" data-lg-tj-no="
                                                                                                0115
                                                                                        " data-lg-tj-cid="4486580" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">
                                    <h3 style="max-width: 180px;">Java开发工程师</h3>
                                                                                                                                                                                                                            <span class="add">[<em>苏州·吴江区</em>]</span>
                                                                                                                                                                                                        </a>
                                <span class="format-time">1天前发布</span>
                            </div>
                            <div class="p_bot">
                                <div class="li_b_l">
                                    <span class="money">8k-15k</span>
                                    <!--<i></i>-->经验1-3年 / 本科
                                </div>
                            </div>
                        </div>
                        <div class="company">
                            <div class="company_name">
                                <a href="https://www.lagou.com/gongsi/75213.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="
                                                                                                0115
                                                                                        " data-lg-tj-cid="75213" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">南京思酷通讯科技有限公司</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                            </div>
                            <div class="industry">
                                移动互联网,电子商务 / 不需要融资
                            </div>
                        </div>
                        <div class="com_logo">
                            <a href="https://www.lagou.com/gongsi/75213.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="
                                                                                                0115
                                                                                        " data-lg-tj-cid="75213" data-lg-tj-abt="dm-csearch-useUserAllInterest|0"><img src="//www.lgstatic.com/thumbnail_120x120/i/image/M00/39/A7/Cgp3O1dnk7qAUCgeAADQhX5eKPY798.png" alt="南京思酷通讯科技有限公司" width="60" height="60"></a>
                        </div>
                    </div>
                    <div class="list_item_bot">
                        <div class="li_b_l">
                                                                                                <span>金融</span>
                                                                    <span>后端开发</span>
                                                                    <span>J2EE</span>
                                                                                    </div>
                        <div class="li_b_r">“技术驱动,成长空间大,工作稳定”</div>
                    </div>
                </li>
                                        </ul>
            
    <!-- 推荐公司、城市 -->
    <!-- <div class="recommend-comp-city dn">
    <div class="r_search_tit">相关搜索：</div>
    <ul class="r_search_con">

    </ul>
</div> -->


<div class="recommend-comp-city hide-recom dn" style="display: block;">
	<a rel="nofollow" href="javascript:;" class="expansion">展开<i></i></a>
    <div class="r_company_tit">推荐公司：</div>
    <ul class="r_company_con">
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/9251.html">美柚</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/1373.html">喜马拉雅fm</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/14229.html">微盟</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/49369.html">淘粉吧</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/107435.html">熊猫TV</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/2768.html">易到用车</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/40738.html">小红唇</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/97631.html">汽车超人</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/109.html">蚂蜂窝</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/36996.html">三好网</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/4760.html">唯品会</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/1686.html">爱奇艺</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/23014.html">快法务</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/1575.html">百度招聘</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/81491.html">蚂蚁金服</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/62.html">今日头条</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/2474.html">滴滴</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/20909.html">AcFun</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/23489.html">点点客</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/59251.html">映客</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/gongsi/3712.html">京东</a></li>
    	    </ul>
    <div class="r_city_tit">推荐城市：</div>
    <ul class="r_city_con">
    	    		<li class="r_search_item"><a href="https://www.lagou.com/beijing/">北京找工作</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/beijing/">北京招聘</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/shanghai/">上海找工作</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/shanghai/">上海招聘</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/hangzhou/">杭州找工作</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/hangzhou/">杭州招聘</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/guangzhou/">广州找工作</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/guangzhou/">广州招聘</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/shenzhen/">深圳找工作</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/shenzhen/">深圳招聘</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/chengdu/">成都找工作</a></li>
    	    		<li class="r_search_item"><a href="https://www.lagou.com/chengdu/">成都招聘</a></li>
    	    </ul>
</div>


    <!-- 分页 -->
                    <div class="item_con_pager">
            <div class="pager_container">
                                
                                                    <a rel="nofollow" href="javascript:;" class="page_no pager_prev_disabled" data-index="">上一页</a>
                
                                
                                                                                                                <a rel="nofollow" href="javascript:;" class="page_no pager_is_current" data-index="1">1</a>
                                                                                                    <a href="https://www.lagou.com/zhaopin/Java/2/" class="page_no" data-index="2">2</a>
                                                                                                    <a href="https://www.lagou.com/zhaopin/Java/3/" class="page_no" data-index="3">3</a>
                                    
                                                    ···
                                                    <a href="https://www.lagou.com/zhaopin/Java/30/" class="page_no" data-index="30">30</a>
                
                                                    <a href="https://www.lagou.com/zhaopin/Java/2/" class="page_no" data-index="2">下一页</a>
                            </div>
        </div>
                <input id="isSEO" type="hidden" value="true">
    <input id="pageNoSEO" type="hidden" value="1">
    <input id="pageSizeSEO" type="hidden" value="15">
    <input id="totalPageCountSEO" type="hidden" value="1297">
    <input id="resultLengthSEO" type="hidden" value="15">
    <input type="hidden" name="abtCode" value="dm-csearch-useUserAllInterest|0">
</div>

<!-- template -->
<script id="tpl-position-list" type="text/html">
    {{each data as item i}}
    {{if i <= 14 }}
    <li class="con_list_item{{if i==0}} first_row{{/if}} default_list" data-index="{{i + indexOffset}}" data-positionid="{{item.positionId}}" data-salary="{{item.salary}}" data-company="{{item.companyShortName}}" data-positionname="{{item.positionName}}" data-companyid="{{item.companyId}}" data-hrid="{{item.publisherId}}" data-tpladword="{{item.adWord}}">
        {{if item.adWord == 9 }}
            <span class="hurry_up"></span>
        {{/if}}
        <div class="list_item_top">
            <div class="position">
                <div class="p_top">
                    <a class="position_link" href="https://www.lagou.com/jobs/{{item.positionId}}.html" target="_blank" data-index="{{i}}" data-lg-tj-id="8E00" data-lg-tj-no="
                {{if i<9}}
                    {{if item.curpage<10}}
                    0{{item.curpage}}0{{i+1}}
                    {{else}}
                    {{item.curpage}}0{{i+1}}
                    {{/if}}
                {{else}}
                    {{if item.curpage<10}}
                    0{{item.curpage}}{{i+1}}
                    {{else}}
                    {{item.curpage}}{{i+1}}
                    {{/if}}
               {{/if}}
                " data-lg-tj-cid="{{item.positionId}}" {{if extra.abt}}data-lg-tj-abt="{{extra.abt}}"{{/if}}>
                        <h3>{{item.positionName}}</h3>
                        {{if "" == item.city }}
                            {{if !item.city}}
                                <span class="add">[<em>{{item.province}}</em>]</span>
                            {{else}}
                                {{if item.businessZones && item.businessZones.length>0 && item.businessZones[0] != ''}}
                                    <span class="add">[<em>{{item.businessZones[0]}}</em>]</span>
                                {{else}}
                                    {{if item.district}}
                                        <span class="add">[<em>{{item.district}}</em>]</span>
                                    {{else}}
                                        <span class="add">[<em>{{item.city}}</em>]</span>
                                    {{/if}}
                                {{/if}}
                            {{/if}}
                        {{else}}
                            {{if !item.city}}
                                <span class="add">[<em>{{item.province}}</em>]</span>
                            {{else}}
                                {{if item.businessZones && item.businessZones.length>0 && item.businessZones[0] != ''}}
                                    <span class="add">[<em>{{item.city}}·{{item.businessZones[0]}}</em>]</span>
                                {{else}}
                                    {{if item.district}}
                                        <span class="add">[<em>{{item.city}}·{{item.district}}</em>]</span>
                                    {{else}}
                                        <span class="add">[<em>{{item.city}}</em>]</span>
                                    {{/if}}
                                {{/if}}
                            {{/if}}
                        {{/if}}

                    </a>
                    <span class="format-time">{{item.formatCreateTime}}</span>
                    {{each data.hrInfoMap as one}}
                        {{if one.key == item.positionId}}
                            <input type="hidden" class='hr_portrait' value='{{one.portrait}}'>
                            <input type="hidden" class='hr_name' value='{{one.realName}}'>
                            <input type="hidden" class='hr_position' value='{{one.positionName}}'>
                            <input type="hidden" class='target_hr' value='{{one.userId}}'>
                            <input type="hidden" class='target_position' value='{{item.positionId}}'>
                            {{if one.canTalk == true}}
                            <div class="chat_me" data-lg-tj-id="1WI0" data-lg-tj-no="{{if item.curpage < 10}}0{{item.curpage}}{{else}}{{item.curpage}}{{/if}}{{if i < 9}}0{{i + 1}}{{else}}{{i + 1}}{{/if}}" data-lg-tj-cid="{{item.companyId}}" data-lg-tj-track-code="search_code" data-lg-tj-track-type="1"></div>
                            {{/if}}
                        {{/if}}
                    {{/each}}
                </div>
                <div class="p_bot">
                    <div class="li_b_l">
                        <span class="money">{{item.salary}}</span>
                        <!--<i></i>-->经验{{item.workYear}} / {{item.education}}
                    </div>
                </div>
            </div>
            <div class="company">
                <div class="company_name">
                    <a href="https://www.lagou.com/gongsi/{{item.companyId}}.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="
                {{if i<9}}
                    {{if item.curpage<10}}
                    0{{item.curpage}}0{{i+1}}
                    {{else}}
                    {{item.curpage}}0{{i+1}}
                    {{/if}}
                {{else}}
                    {{if item.curpage<10}}
                    0{{item.curpage}}{{i+1}}
                    {{else}}
                    {{item.curpage}}{{i+1}}
                    {{/if}}
               {{/if}}
                " data-lg-tj-cid="{{item.companyId}}" {{if extra.abt}}data-lg-tj-abt="{{extra.abt}}"{{/if}}>{{item.companyShortName}}</a>
                </div>
                <div class="industry">
                    {{item.industryField}} / {{item.financeStage}}
                </div>
            </div>
            <div class="com_logo">
                <a href="https://www.lagou.com/gongsi/{{item.companyId}}.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="
                {{if i<9}}
                    {{if item.curpage<10}}
                    0{{item.curpage}}0{{i+1}}
                    {{else}}
                    {{item.curpage}}0{{i+1}}
                    {{/if}}
                {{else}}
                    {{if item.curpage<10}}
                    0{{item.curpage}}{{i+1}}
                    {{else}}
                    {{item.curpage}}{{i+1}}
                    {{/if}}
               {{/if}}
                " data-lg-tj-cid="{{item.companyId}}" {{if extra.abt}}data-lg-tj-abt="{{extra.abt}}"{{/if}}><img src="//www.lgstatic.com/thumbnail_120x120/{{item.companyLogo}}" alt="{{item.companyShortName}}" width="60" height="60"></a>
            </div>
        </div>
        <div class="list_item_bot">
            {{if item.positionLables && item.positionLables.length > 0}}
                <div class="li_b_l">
                    {{each item.positionLables as datas i}}
                        <span>{{datas}}</span>
                    {{/each}}
                </div>
            {{else}}
                <div class="li_b_l">
                    {{each item.companyLabelList as datas i }}
                        {{if i<4}}
                            <span>{{datas}}</span>
                        {{/if}}
                    {{/each}}
                </div>
            {{/if}}
            <div class="li_b_r">“{{item.positionAdvantage}}”</div>
        </div>
    </li>
    {{/if}}
    {{/each}}
</script>

<!-- 数据为空 template -->
<script id="empty-position" type="text/html">
    <div class="empty_position">
        <div class="pic"></div>
        <div class="txt">
            <div>暂时没有符合该搜索条件的职位</div>
            <span>请重新修改搜索条件后再进行搜索</span>
        </div>
    </div>
</script>


            </div>
'''

def parse_text():
    htmlElement = etree.HTML(text)
    print(etree.tostring(htmlElement,encoding="utf-8").decode("utf-8"))

def parse_renre_file():
    parse = etree.HTMLParser(encoding="utf-8")#默认解析格式为xml，容易报错，需要手动设置解析格式为HTML,不报错可以不设置
    htmlElement =etree.parse('renren.html',parser=parse)
    print(etree.tostring(htmlElement, encoding="utf-8").decode("utf-8"))#如果输出字符串开头为b则为byte类型数据，需要decode解码成字符串后可以正常显示



if __name__ == '__main__':
    # parse_text()
    parse_renre_file()