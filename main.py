import os
import shutil

# 从txt文件中读取要删除的文件和文件夹路径
def read_paths_from_file(file_path):
    import chardet
    detected_encoding = chardet.detect(open(file_path, 'rb').read())['encoding']
    with open(file_path, 'r', encoding=detected_encoding) as file:
        paths = [line.strip() for line in file if line.strip()]
    return paths

# 获取路径的描述
def get_path_description(path):
    descriptions = {
        r'C:\Windows\Temp': "Windows临时文件夹，存储安装程序和系统过程创建的临时文件。",
        r'C:\Windows\Prefetch': "Windows预取文件夹，用于加速启动过程。",
        r'C:\Users\%USERNAME%\AppData\Local\Temp': "用户临时文件夹，存储应用程序和系统过程创建的临时文件。",
        r'C:\Users\%USERNAME%\AppData\Local\Microsoft\Windows\INetCache': "浏览器缓存文件夹，存储浏览器的缓存文件。",
        r'C:\Users\%USERNAME%\AppData\Local\Microsoft\Windows\Explorer': "文件资源管理器缓存文件夹，存储文件资源管理器的缓存文件。",
        r'C:\Users\%USERNAME%\AppData\Local\CrashDumps': "崩溃转储文件夹，存储应用程序崩溃时生成的转储文件。",
        r'C:\Users\%USERNAME%\AppData\Local\Temp\*.tmp': "临时文件。",
        r'C:\Users\%USERNAME%\AppData\Local\Temp\*.log': "日志文件。",
        r'C:\Users\%USERNAME%\AppData\Local\Temp\*.bak': "备份文件。",
        r'C:\Users\%USERNAME%\AppData\Local\Temp\*.old': "旧版本文件。",
        r'C:\Users\%USERNAME%\AppData\Local\Temp\~*': "临时文件。",
    }
    return descriptions.get(path, "未知路径")

# 删除文件
def delete_file(file):
    try:
        os.remove(file)
        print(f"已删除文件: {file} - {get_path_description(file)}")
    except Exception as e:
        print(f"删除文件失败: {file}。原因: {e}")

# 删除目录
def delete_directory(directory):
    try:
        shutil.rmtree(directory)
        print(f"已删除目录: {directory} - {get_path_description(directory)}")
    except Exception as e:
        print(f"删除目录失败: {directory}。原因: {e}")

# 清理指定的路径
def clean_paths(paths):
    for path in paths:
        # 处理路径中的环境变量，例如 %USERNAME%
        path = os.path.expandvars(path)
        
        if os.path.exists(path):
            description = get_path_description(path)
            confirm = input(f"是否删除路径 {path} ({description})? (y/n): ")
            if confirm.lower() == 'y':
                if os.path.isfile(path):
                    delete_file(path)
                elif os.path.isdir(path):
                    delete_directory(path)
                else:
                    print(f"未知类型的路径: {path}")
            else:
                print(f"跳过清理路径: {path}")
        else:
            print(f"路径不存在: {path}")

# 清空回收站
def empty_recycle_bin():
    try:
        import win32com.client
        shell = win32com.client.Dispatch("Shell.Application")
        recycle_bin = shell.NameSpace(10)
        recycle_bin_items = recycle_bin.Items()
        item_count = recycle_bin_items.Count
        if item_count > 0:
            confirm = input(f"回收站中有 {item_count} 个项目。是否清空回收站？ (y/n): ")
            if confirm.lower() == 'y':
                shell.NameSpace(10).Items().InvokeVerb("empty")
                print(f"已清空回收站中的 {item_count} 个项目。")
            else:
                print("跳过清空回收站。")
                print("回收站未清空。")
        else:
            print("回收站已为空。")
    except ImportError:
        print("未安装pywin32库，无法清空回收站。")

# 执行清理
if __name__ == "__main__":
    file_path = input("请输入包含要删除路径的txt文件路径(默认：清理配置.txt): ")
    if file_path == '':
        file_path = "清理配置.txt"
    if os.path.isfile(file_path):
        paths_to_clean = read_paths_from_file(file_path)
        clean_paths(paths_to_clean)
        empty_recycle_bin()
    else:
        print("输入的文件路径无效。")
