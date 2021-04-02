import json
import os
import re
import sys


table_header_template = """
| 参数 | 类型 | 示例 | 含义 | 
| :-- | :-- | :-- | :-- |
"""


table_line_template = """| %s | %s | %s | %s |
"""

default_explain = "default"


raw_json_input = """
{
    "id":233633425860867,
    "openId":"1FaJr4xmIt",
    "phone":"8h0fTosM6W",
    "stuName":"RvAz5kWTFx",
    "stuNo":"NtULw5Njll",
    "thirdId":"mlDsFhpqr8"
}
"""


default_output_dir = "./ouput"


def json_obj_ouput_md_table(table_name, json_obj):
    output = ""
    output += table_header_template

    if type(json_obj) == dict:
        for k, v in json_obj.items():

            if type(v) == int:
                output += table_line_template % (str(k), "Number", v, default_explain)
            elif type(v) == str:
                output += table_line_template % (str(k), "String", v, default_explain)
            elif type(v) == bool:
                output += table_line_template % (str(k), "Boolean", v, default_explain)
            elif type(v) == dict:
                output += table_line_template % (str(k), "Object", "{ ... }", default_explain)
                json_obj_ouput_md_table(table_name + "_" + re.sub("/", "", str(k)), v)
            elif type(v) == list:
                if len(v) != 0:
                    example = v[0]
                    json_obj_ouput_md_table(table_name + "_" + re.sub("/", "", str(k)), example)
                output += table_line_template % (str(k), "List", "[ ... ]", default_explain)

            pass
    else:
        if type(json_obj) == int:
                output += table_line_template % ("type:int", "Number", json_obj, default_explain)
        elif type(json_obj) == str:
                output += table_line_template % ("type:str", "String", json_obj, default_explain)
        elif type(json_obj) == bool:
                output += table_line_template % ("type:bool", "Boolean", json_obj, default_explain)
        elif type(json_obj) == list:
            if len(json_obj) != 0:
                example = v[0]
                json_obj_ouput_md_table(table_name + "_" + re.sub("/", "", str(k)), example)
            output += table_line_template % (str(k), "List", "[ ... ]", default_explain)

        pass
    
    if not os.path.exists(default_output_dir):
        os.mkdir(default_output_dir)
        pass
    file_name = default_output_dir + "/" + table_name + ".md"
    with open(file_name, "w") as f:
        f.write("# table: " + table_name + "\n")
        f.write(output)
        f.write("\n# raw json object\n\n")
        f.write(str(json_obj))
    pass


def main(input_json_str):
    json_obj = json.loads(input_json_str)
    json_obj_ouput_md_table("origin", json_obj)
    pass


if __name__ == '__main__':
    if len(sys.argv) <= 2:
        main(raw_json_input)
    else:
        mode = sys.argv[1]
        if mode != "-f":
            print("not support mode '%s'" % mode)
        with open(sys.argv[2], "r") as f:
            json_input = f.read()
        main(json_input)
