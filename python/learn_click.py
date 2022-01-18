'''
python的click用法
click: 一个python的命令行工具
中文文档: https://click-docs-zh-cn.readthedocs.io/zh/latest/index.html
'''


# 实现python接收指定参数，并且可以自动补全参数


from urllib.parse import uses_fragment
import click

@click.group()
def main():
    pass

# 所有命令都从属main组，即任何参数命令都不加


@main.group()
def cli():
    click.echo('main')


@main.group()
def backup():
    pass

@backup.command(help='backup dcs')
def dcs():
    pass

@backup.command()
def gtm():
    pass

@backup.command()
def coordinator():
    pass

@backup.command()
def datanode():
    pass

@backup.command()
def topo():
    pass


if __name__ == "__main__":
    main()