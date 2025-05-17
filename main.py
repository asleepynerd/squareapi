from quart import Quart, request, send_file, jsonify
from PIL import Image
import io

app = Quart(__name__)

@app.route('/square', methods=['GET'])
async def square_image():
    mode = (request.args.get('mode') or 'center').lower()
    size_param = request.args.get('size')
    size_param = int(size_param) if size_param and size_param.isdigit() else None

    if 'file' in (await request.files):
        file = (await request.files)['file']
        img = Image.open(file.stream)
    elif 'url' in request.args:
        import requests
        img_url = request.args['url']
        resp = requests.get(img_url)
        img = Image.open(io.BytesIO(resp.content))
    else:
        return jsonify({'error': 'no image, provide url with ?url'}), 400

    width, height = img.size
    min_dim = min(width, height)
    if mode == 'center':
        left = (width - min_dim) // 2
        top = (height - min_dim) // 2
    elif mode == 'top':
        left = (width - min_dim) // 2
        top = 0
    elif mode == 'bottom':
        left = (width - min_dim) // 2
        top = height - min_dim
    elif mode == 'left':
        left = 0
        top = (height - min_dim) // 2
    elif mode == 'right':
        left = width - min_dim
        top = (height - min_dim) // 2
    else:
        left = (width - min_dim) // 2
        top = (height - min_dim) // 2
    right = left + min_dim
    bottom = top + min_dim
    squared = img.crop((left, top, right, bottom))
    if size_param:
        squared = squared.resize((size_param, size_param), Image.LANCZOS)
    buf = io.BytesIO()
    squared.save(buf, format='PNG')
    buf.seek(0)
    return await send_file(buf, mimetype='image/png', as_attachment=True, attachment_filename='squared.png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)