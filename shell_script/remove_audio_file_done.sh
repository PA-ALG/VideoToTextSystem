#!/bin/bash

# 获取脚本所在的绝对路径
SCRIPT_DIR=$(cd $(dirname $0) && pwd)
# 获取脚本所在目录的上级目录
PARENT_DIR=(dirname $SCRIPT_DIR)
# 指定含有文件的文件夹路径
SOURCE_DIR="$PARENT_DIR/output"
# 指定含有子文件夹的文件夹路径
DEST_DIR="$PARENT_DIR/files/videos"
DEST_DIR_1="$PARENT_DIR/files/output_audio"
DEST_DIR_2="$PARENT_DIR/files/split_audio"
DEST_DIR_3="$PARENT_DIR/files/results"

# 创建一个空的关联数组(哈希表)来存储文件名(不含扩展名)
declare -A file_names

# 遍历文件夹中的所有文件，并提取不含扩展名的文件名
for file in "$SOURCE_DIR"/*;do
  if [ -f "$file" ]; then
    # 提取文件名,并去除扩展名
    base_name=$(basename "$file" | sed 's/\(.*\)\..*/\1/')
    # 将文件名存入关联数组
    file_names["$base_name"]=1
  fi
done

# 遍历文件夹中的所有子文件夹
for file in "$DEST_DIR"/*;do
  if [ -f "$file" ]; then
    # 提取wav文件名称
    file_name=$(basename "$file")
    file_name_without_extension="$(file_name%.*)"
    # 检查子文件夹名称是否在文件名列表中
    if [[ -n ${file_names["$file_name_without_extension"]} ]]; then
      # 如果在列表中找到了匹配的文件名称, 则删除该文件
      rm -rf "$file"
      echo "Delete mp4 file: $file"
    fi
  fi
done

# 遍历文件夹中的所有子文件夹
for file in "$DEST_DIR_1"/*;do
  if [ -f "$file" ]; then
    # 提取wav文件名称
    file_name=$(basename "$file")
    file_name_without_extension="$(file_name%.*)"
    # 检查子文件夹名称是否在文件名列表中
    if [[ -n ${file_names["$file_name_without_extension"]} ]]; then
      # 如果在列表中找到了匹配的文件名称, 则删除该文件
      rm -rf "$file"
      echo "Delete source wav file: $file"
    fi
  fi
done

# 遍历文件夹中的所有子文件夹
for dir in "$DEST_DIR_2"/*;do
  if [ -d "$file" ]; then
    # 提取wav文件名称
    dir_name=$(basename "$dir")
    # 检查子文件夹名称是否在文件名列表中
    if [[ -n ${file_names["$dir_name"]} ]]; then
      # 如果在列表中找到了匹配的文件名称, 则删除该文件
      rm -rf "$dir"
      echo "Delete folder split_audio/: $dir"
    fi
  fi
done

# 遍历文件夹中的所有子文件夹
for dir in "$DEST_DIR_3"/*;do
  if [ -d "$file" ]; then
    # 提取wav文件名称
    dir_name=$(basename "$dir")
    # 检查子文件夹名称是否在文件名列表中
    if [[ -n ${file_names["$dir_name"]} ]]; then
      # 如果在列表中找到了匹配的文件名称, 则删除该文件
      rm -rf "$dir"
      echo "Delete folder results/: $dir"
    fi
  fi
done

echo "Script execution completed."
