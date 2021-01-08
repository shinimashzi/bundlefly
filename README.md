论文中的配置有两种：

```
k = 25	k = 25
q = 7	q = 7
a = 13	a = 17
p = 8	p = 6
```

1. 创建bundlefly拓扑：
更改config.ini
cd bundlefly_topology
python bundlefly.py

2. 运行generator_config_file.py 生成配置文件

3. 在booksim2环境下进行模拟
- 在booksim2/src 下编译，make
- 运行 ./booksim config_path
    - 可以考虑使用bundlefly.sh，需要将它移放在src目录下，bundlefly_config目录同理。


