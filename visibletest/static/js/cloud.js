$(function(){
    var db = [
    {"word":"女装","freq":70},
    {"word":"男装","freq":38},
    {"word":"内衣","freq":38},
    {"word":"鞋靴","freq":28},
    {"word":"箱包","freq":26},
    {"word":"配件","freq":22},
    {"word":"童装玩具","freq":80},
    {"word":"孕产","freq":20},
    {"word":"用品","freq":20},
    {"word":"家电","freq":18},
    {"word":"数码","freq":18},
    {"word":"手机","freq":18},
    {"word":"美妆","freq":17},
    {"word":"洗护","freq":16},
    {"word":"保健品","freq":15},
    {"word":"珠宝","freq":15},
    {"word":"眼镜","freq":15},
    {"word":"手表","freq":15},
    {"word":"运动","freq":14},
    {"word":"户外","freq":14},
    {"word":"乐器","freq":14},
    {"word":"游戏","freq":14},
    {"word":"动漫","freq":13},
    {"word":"影视","freq":13},
    {"word":"美食","freq":13},
    {"word":"生鲜","freq":12},
    {"word":"零食","freq":12},
    {"word":"鲜花","freq":12},
    {"word":"鲜花","freq":12},
    {"word":"农资","freq":12},
    {"word":"房产","freq":11},
    {"word":"装修","freq":11},
    {"word":"建材","freq":10},
    {"word":"家具","freq":10},
    {"word":"家饰","freq":10},
    {"word":"家纺","freq":10},
    {"word":"汽车","freq":10},
    {"word":"二手车","freq":9},
    {"word":"用品","freq":9},
    {"word":"办公","freq":9},
    {"word":"DIY","freq":9},
    {"word":"五金电子","freq":8},
    {"word":"百货","freq":8},
    {"word":"餐厨","freq":8},
    {"word":"家庭保健","freq":8},
    {"word":"学习","freq":8},
    {"word":"卡券","freq":8},
    {"word":"本地服务","freq":8}]

    list = [];
    for (var i in db) {
      list.push([db[i]["word"], db[i]["freq"]])
    }

    WordCloud.minFontSize = "15px"
    WordCloud($('#word_cloud'), { list: list} );
})
