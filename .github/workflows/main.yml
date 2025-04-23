name: Scheduled Task for hh.py

on:
  push:  # 上传后立即运行第一次
    branches: [ main ]  # 替换为你的默认分支
  schedule:
    - cron: '0 */6 * * *'  # 每6小时运行一次（无限循环）
  workflow_dispatch:  # 允许手动触发

jobs:
  run_script:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install requests pytz  # 安装requests和pytz

      - name: Run script
        run: |
          echo "当前UTC时间: $(date -u)"
          echo "开始执行hh.py脚本..."
          python hh.py  # 运行根目录下的hh.py文件
          echo "脚本执行完成！无限循环任务已激活。"
