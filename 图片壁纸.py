from PIL import Image

# 获取用户输入（整合为一行）
try:
    color_code, aspect_ratio, resolution, file_extension = input(
        "请输入颜色代码（如 #FF5733 或 rgb(255,87,51)）、图片比例（如 16:9）、分辨率（如 1920x1080）、图片后缀名（jpg 或 png），以空格分隔："
    ).split()
    file_extension = file_extension.lower()  # 确保后缀小写
except ValueError:
    print("输入有误，请确保提供所有四项内容并用空格分隔！")
    exit()

# 验证颜色代码
if color_code.startswith("#") and len(color_code) == 7:
    fill_color = color_code
elif color_code.startswith("rgb") and color_code[3] == '(' and color_code[-1] == ')':
    try:
        fill_color = tuple(map(int, color_code[4:-1].split(',')))
        if not all(0 <= c <= 255 for c in fill_color):
            raise ValueError
    except ValueError:
        print("RGB 颜色代码格式不正确，请使用 rgb(255,87,51) 格式！")
        exit()
else:
    print("颜色代码格式不正确，请使用 # 或 rgb 格式！")
    exit()

# 验证比例和分辨率
try:
    ratio_width, ratio_height = map(int, aspect_ratio.split(':'))
    width, height = map(int, resolution.split('x'))
except ValueError:
    print("比例或分辨率输入格式不正确，请使用 16:9 和 1920x1080 格式！")
    exit()

# 计算目标高度以保持比例
target_width = width
target_height = int(width / ratio_width * ratio_height)

# 创建图片
image = Image.new("RGB", (target_width, target_height), fill_color)

# 验证文件扩展名并保存图片
if file_extension not in ["jpg", "png"]:
    print("图片后缀名必须是 jpg 或 png！")
    exit()

output_file = f"generated_wallpaper.{file_extension}"
try:
    image.save(output_file)
    print(f"壁纸已成功生成并保存为：{output_file}")
except Exception as e:
    print(f"保存图片时出错：{e}")
