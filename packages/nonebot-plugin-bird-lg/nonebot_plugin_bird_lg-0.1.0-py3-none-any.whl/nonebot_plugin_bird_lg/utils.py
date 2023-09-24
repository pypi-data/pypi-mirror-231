import pandas as pd
import matplotlib.pyplot as plt
# import base64
from io import BytesIO

def generate_image(data: dict) -> BytesIO:
    """将传入的数据转换为图片。

    Args:
        data (dict): 字典数据。

    Returns:
        str: 图片的 `base64`。
    """
    df = pd.DataFrame(data)
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.axis('tight')
    ax.axis('off')
    ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')
    image = BytesIO()
    plt.savefig(image, format='png', bbox_inches='tight', pad_inches=0.1, dpi=300)
    image.seek(0)
    # b64_image = base64.b64encode(image.read()).decode('utf-8')
    # return b64_image
    return image

def convert_data(data: str) -> dict:
    """将传入的数据转换为绘图需要的字典数据。

    Args:
        data (str): 数据内容。

    Returns:
        dict: 字典数据。
    """
    lines = data.strip().split('\n')
    headers = lines[0].split()
    convert = {header: [] for header in headers}
    for line in lines[1:]:
        values = line.split()
        for i in range(len(headers)):
            convert[headers[i]].append(values[i] if i < len(values) else '')
    return convert