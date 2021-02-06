import para

# 创建SSH对象
ssh = para.SSHClient()
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(para.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='139.186.201.199', port=6000, username='ubuntu', password='Kevin==Smart722.+-')

# 执行命令
stdin, stdout, stderr = ssh.exec_command('ls')
# 获取命令结果
result = stdout.read()
print(result)
# 关闭连接
ssh.close()