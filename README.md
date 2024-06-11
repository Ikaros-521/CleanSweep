# 前言

## 软件名称

CleanSweep

## 中文使用说明和功能讲解

### 1. 软件介绍

CleanSweep 是一个用于清理Windows系统上无用文件和文件夹的小工具。该软件可以帮助用户释放硬盘空间，提升系统性能。它支持从本地txt文件中读取要删除的文件和文件夹路径，并且在删除操作前提示用户确认，确保删除操作的安全性。

### 2. 功能

读取路径文件：从用户提供的txt文件中读取要删除的文件和文件夹路径。
删除临时文件：删除指定路径下的临时文件、日志文件、备份文件等。
删除临时文件夹：删除指定路径下的临时文件夹、缓存文件夹等。
清空回收站：提示用户是否清空回收站。
日志记录：记录删除操作的详细信息，包括删除的文件和文件夹路径、删除失败的原因等。

### 3. 使用说明

#### 3.1. 准备路径文件

创建一个txt文件，例如 cleanup_paths.txt。
将要删除的文件和文件夹路径逐行写入该文件。

#### 3.2. 运行软件

确保系统安装了Python环境和pywin32库。可以通过以下命令安装pywin32：`pip install pywin32`
运行以下Python脚本：`python main.py`

输入包含要删除路径的txt文件路径，例如 C:\path\to\cleanup_paths.txt。

程序会逐行读取txt文件中的路径，并提示用户确认是否删除。如果用户确认删除，程序将删除相应的文件或文件夹，并记录日志。

程序还会提示用户是否清空回收站。

### 4. 注意事项

运行该程序需要管理员权限。
清空回收站功能需要安装pywin32库。
请确保在运行此程序之前了解它的作用，并在适当的时候进行备份。
删除操作不可逆，请谨慎确认删除操作。
通过CleanSweep，您可以轻松、安全地清理系统上的无用文件和文件夹，从而释放更多的硬盘空间，提升系统性能。  

## 文件夹用途说明

### C:\Windows\Temp

存储内容：临时文件，安装程序和系统过程创建的临时文件。
删除影响：通常可以安全删除，可能会导致正在进行的安装或更新失败。

### C:\Windows\Prefetch

存储内容：Windows启动和程序启动时的预取文件，用于加速启动过程。
删除影响：删除后，启动速度可能暂时变慢，系统会重新生成这些文件。

### C:\Users%USERNAME%\AppData\Local\Temp

存储内容：用户临时文件，由应用程序和系统过程创建的临时文件。
删除影响：通常可以安全删除，可能会导致正在运行的应用程序出现问题。

### C:\Users%USERNAME%\AppData\Local\Microsoft\Windows\INetCache

存储内容：Internet Explorer和其他浏览器的缓存文件。
删除影响：删除后，浏览器会重新下载网页内容，可能会导致网站加载时间稍长。

### C:\Users%USERNAME%\AppData\Local\Microsoft\Windows\Explorer

存储内容：文件资源管理器的缓存文件和临时数据。
删除影响：删除后，文件资源管理器可能需要重新生成缓存，但通常不会影响系统性能。

### C:\Users%USERNAME%\AppData\Local\CrashDumps

存储内容：应用程序崩溃时生成的转储文件。
删除影响：删除后，无法用于诊断应用程序崩溃的问题，通常可以安全删除。

### C:\Users%USERNAME%\AppData\Local\Temp*.tmp

存储内容：临时文件。
删除影响：通常可以安全删除。

### C:\Users%USERNAME%\AppData\Local\Temp*.log

存储内容：日志文件。
删除影响：通常可以安全删除。

### C:\Users%USERNAME%\AppData\Local\Temp*.bak

存储内容：备份文件。
删除影响：通常可以安全删除。

### C:\Users%USERNAME%\AppData\Local\Temp*.old

存储内容：旧版本的文件。
删除影响：通常可以安全删除。

### C:\Users%USERNAME%\AppData\Local\Temp~*

存储内容：临时文件。
删除影响：通常可以安全删除。
