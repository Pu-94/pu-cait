import os
import json
from datetime import datetime
from github import Github

def backup():
    g = Github(os.getenv('GITHUB_TOKEN'))
    repo = g.get_repo(f"{os.getenv('GITHUB_REPOSITORY')}")
    
    # 获取所有书籍数据
    books = []
    for file in os.listdir('novels/_books/approved'):
        if file.endswith('.md'):
            with open(f"novels/_books/approved/{file}") as f:
                books.append(f.read())
    
    # 创建备份Release
    timestamp = datetime.now().strftime('%Y%m%d-%H%M')
    repo.create_git_release(
        title=f"Backup {timestamp}",
        tag_name=f"backup-{timestamp}",
        message="Automatic books backup",
        draft=False
    ).upload_asset(
        name='books.json',
        asset=json.dumps(books).encode()
    )

if __name__ == '__main__':
    backup()