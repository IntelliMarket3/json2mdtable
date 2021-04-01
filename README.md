# json2mdtable
文档小工具，json转换为md文档中的表格。

## 使用方法

```bash
python3 main.py -f <json文件的路径>
```

## 输出

默认在执行目录下的output文件夹下。

md文件结构

```markdown
# table: <table名，根json为origin，value为Objecy就是key的值>

| 参数 | 类型 | 示例 | 含义 | 
| :-- | :-- | :-- | :-- |
... 表格剩下结构

```

参数填充的json的key，示例填充json的value。
类型如果是数字填充`Number`，字符串填充`String`，json对象填充`Object`，json列表填充Object。
遇到对象和列表两种情况，会再次对这个对象或`列表一个元素`新生成一个markdown文件描述其结构。
