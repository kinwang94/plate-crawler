# Plate Crawler

## Getting Started

### Prerequisites 

- [Chrome](https://www.google.com/chrome/)

### Installation

```shell
pip install selenium
```

## Usage

Launch Chrome via Command Prompt (cmd):

```text
<path_of_chrome> --remote-debugging-port=9222 --user-data-dir=<path_of_user_data>
```

Example:

```bash
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="D:\Chrome"
```

`--remote-debugging-port` 指定 selenium 透過特定的 port 與 Chrome Debugging Protocol (CDP) 通訊。

`--user-data-dir` 用作隔離瀏覽器記錄，以免污染原本的使用。

```bash
python main.py
```

初次使用時，可能會被 Cloudflare 檢測到並阻擋，可以在同一個 Chrome 中開新分頁，開啟 `https://platesmania.com/us/informer` 手動完成 Cloudflare 驗證，再重新執行，後續大部份時間應該不會再出現驗證。