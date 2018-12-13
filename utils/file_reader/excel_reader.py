import os
from xlrd import open_workbook

class ExcelReader(object):
    """
        读取excel文件中的内容。返回list。

        如：
        excel中内容为：
        | A  | B  | C  |
        | A1 | B1 | C1 |
        | A2 | B2 | C2 |

        如果 print(ExcelReader(excel, title_line=True).data)，输出结果：
        [{A: A1, B: B1, C:C1}, {A:A2, B:B2, C:C2}]

        如果 print(ExcelReader(excel, title_line=False).data)，输出结果：
        [[A,B,C], [A1,B1,C1], [A2,B2,C2]]

        可以指定sheet，通过index或者name：
        ExcelReader(excel, sheet=2)
        ExcelReader(excel, sheet='BaiDuTest')
        """

    def __init__(self,excel,sheet=0,title_line=True):
        if os.path.exists(excel):
            self.excel = excel
        else:
            raise FileNotFoundError('文件不存在！')
        self.sheet = sheet
        self.title_line = title_line
        self._data = list()

    @property
    def data(self):
        if not self._data:
            workbook = open_workbook(self.excel)
            if type(self.sheet) not in [int, str]:
                raise TypeError('Please pass in <type int> or <type str>, not {0}'.format(type(self.sheet)))
            elif type(self.sheet) == int:
                s = workbook.sheet_by_index(self.sheet)
            else:
                s = workbook.sheet_by_name(self.sheet)

            if self.title_line:
                title = s.row_values(0) # 首行为title
                for col in range(1, s.nrows):
                    # 依次遍历其余行，与首行组成dict，拼到self._data中
                    self._data.append(dict(zip(title, s.row_values(col))))

            else:
                for col in range(0,s.nrows):
                     # 遍历所有行，拼到self._data中
                    self._data.append(s.row_values(col))

        return self._data

# if __name__ == '__main__':
#     e = 'E:\EBCAutoTestingProjects\TestFramework\data\baidu.xlsx\baidu.xlsx'
#     reader = ExcelReader(e, title_line=True)
#     print(reader.data)

"""
 我们添加title_line参数，用来声明是否在excel表格里有标题行，如果有标题行，返回dict列表，否则返回list列表，如下：
 excel表格如下:
 | title1 | title2 |
 | value1 | value2 |
 | value3 | value4 |

 如果title_line=True
 [{"title1": "value1", "title2": "value2"}, {"title1": "value3", "title2": "value4"}]

 如果title_line=False
 [["title1", "title2"], ["value1", "value2"], ["value3", "value4"]]
"""