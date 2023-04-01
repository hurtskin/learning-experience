# learning-experience
*用python解析xml文件，并将内容插入进单链表中，再进行单链表的遍历功能*


home.xml是这次需要解析的xml文件


一、先用import xml.etree.cElementTree as ET将xml文件用elementree的方法进行解析


二、定义一个取出节点的大体步骤的函数，并在里面引用其他的具体步骤函数
    定义一个get_xml_content(path)的函数将xml文件进行导入
    这样做的方式可以灵活的引入不同的xml文件
    在get_xml_content函数中，使解析出来的树形数据存入tree中，然后用get.root解析出根节点root


三、取出xml的所有子节点
    
    def get_all(father):
    xml_strcture = []
    for child in father:
        attrib_list = dict_to_list(child.attrib)
        tag_name = child.tag
        xml_strcture.append([tag_name, attrib_list])

        children = get_all(child)
        if len(children) != 0:
            for item in children:
                xml_strcture.append(item)

    return xml_strcture
    
    利用for循环将所有父节点以[tag_name, attrib_list]的形式存入已经定义好的xml_strcture列表中
    再利用递归调用重新调用原函数将所有子节点都取出
    这里定义dict_to_list函数
    
    def dict_to_list(temp_dict):
    temp_list = []
    for key, val in temp_dict.items():
        temp_list.append([key, val])
    return temp_list
    
    将xml里的元素从dict形式转换成list形式
    具体过程是将key：val以[key, val]的list形式存入list再进行return取出
    
    在get_content函数中引用此函数，至此将所有的节点以及节点属性存入xml_strcture并取出
    
    
四、单链表的实现
    单链表的特点是不要求地址连续，每个结点存有下一个结点地址的指针的线性表
    将单链表进行类的封装，以便调用和管理
    1.首先需要一个存有第一个地址的指针的头节点
    
        def __init__(self):
        self._head = None
        
    2.向单链表添加元素
      1)向链表头部添加元素
        链表头部添加元素只需要创建一个新空间并将他的next指向原头节点，使原头节点存入元素
        
      2)向链表尾部添加元素
        创建一个新空间，利用for循环遍历至链表尾部，然后将尾部节点的next指向新空间的地址
        
      3)向链表中间添加元素
        创建一个新空间，和一个计数器，利用for循环遍历并判断计数器是否和需要添加元素的位置的前一个位置是否相等，最后将前一个位置的next指向新空间，将新空间的next指向原要求位置的节点
        
    3.遍历单链表
      利用for循环判断元素的next是否为空，并用yield取出每一个节点元素
      
      
五、引入单链表并遍历
    import引入已经写好的单链表
    对单链表进行初始化
    利用for循环将return xml_strcture中的每一个元素向单链表尾部添加
    利用for循环遍历单链表并用print打印出每次取出的元素
