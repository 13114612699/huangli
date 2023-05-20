#!/bin/bash

# 询问要搜索的内容
read -p "请输入要搜索的内容: " search_content

# 询问用户要搜索的文件路径
read -p "请输入要搜索的文件所在路径: " file_path

# 将搜索结果保存到的文件路径
read -p "请输入搜索结果保存路径: " result_file_path

# 执行字符匹配并保存结果到文件
grep -n "$search_content" "$file_path" > "$result_file_path"

# 输出搜索结果
while read line ; do
    echo "$line"
done < "$result_file_path"