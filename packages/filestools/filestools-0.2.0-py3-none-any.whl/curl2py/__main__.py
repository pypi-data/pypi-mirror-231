import os

import pyperclip

from curl2py.curlParseTool import *


def main(**kwargs):
    parser = argparse.ArgumentParser(description="将curl网络请求命令转换成python的requests库请求代码，-f/-t/-o三个参数均没有指定时，结果将保存到剪切板中")
    parser.add_argument('-f', '--file', help="被转换的curl命令文件，-o和-t参数均没有指定将保存到对应的同名py脚本中，不指定则从直接对剪切板操作")
    parser.add_argument('-o', '--out', help="生成py脚本的保存位置")
    parser.add_argument('-t', '--tmp', action='store_true', help="py脚本是否保存到当前目录的tmp.py中")
    parser.add_argument('-c', '--copy', action='store_true', help="始终copy结果到剪切板")

    args = parser.parse_args()
    if args.file:
        with open(args.file, encoding="u8") as f:
            curl_cmd = f.read()
    else:
        curl_cmd = str(pyperclip.paste())
        if not curl_cmd.startswith("curl "):
            rich.print('[red]剪切板中未找到curl命令开头的文本，请先从浏览器中复制curl请求。')
            return
    output = curlCmdGenPyScript(curl_cmd)
    colorPrintPyCode(output)
    rich.print('[green]转换完成，上面的打印结果是生成的代码预览')
    output_path = None
    if args.file:
        output_path = os.path.splitext(args.file)[0] + '.py'
    if args.out:
        output_path = args.out
    if output_path:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(output)
        rich.print(f'[green]python脚本已保存到 {output_path} 中')
    if args.tmp:
        with open("tmp.py", 'w', encoding='utf-8') as f:
            f.write(output)
        rich.print(f'[green]python脚本已保存到 tmp.py 中')
    if (output_path is None and args.tmp == False) or args.copy:
        pyperclip.copy(output)
        rich.print('[green]生成的python脚本已经复制到剪贴板中')
    print('作者：小小明，博客地址：https://blog.csdn.net/as604049322')


if __name__ == '__main__':
    main()
